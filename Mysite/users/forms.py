# coding=utf-8
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .fields import HoneyPotField, PasswordField, UsersEmailField


class UserCreationForm(forms.ModelForm):

    error_messages = {
        'duplicate_email': _(u'用户名已存在！'),
        'password_mismatch': _(u'两次密码不相同'),
    }

    email = UsersEmailField(label=_(u'电子邮件地址'), max_length=255)
    password1 = PasswordField(label=_(u'密码'))
    password2 = PasswordField(
        label=_(u'确认密码'),
        help_text=_(u'输入和第一次密码相同的密码进行确认'))

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):

        # Since User.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data['email']
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = not settings.USERS_VERIFY_EMAIL
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(label=_('Password'), help_text=_(
        u'密码经过加密，因此不可见 ,'
        u'但是使用 <a href=\"/accounts/password_change/\">这个</a>'
        u'链接可以修改密码.'
    ))

    class Meta:
        model = get_user_model()
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial['password']


class RegistrationForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(
        label=_('我已阅读并同意注册'),
        widget=forms.CheckboxInput,
        error_messages={
            'required': _('你必须同意注册')
        })


class RegistrationFormHoneypot(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a honeypot field
    for Spam Prevention

    """
    accept_terms = HoneyPotField()
