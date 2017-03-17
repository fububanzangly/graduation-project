#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def writeIntoDataBase(name,author,pubdate,type):

    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","123456","ebook")
    cursor = db.cursor()
    # SQL 插入语句
    sql = 'INSERT INTO bookinfo (book_name,book_author,book_pubdate,book_type) VALUES ("%s","%s","%s","%s")' % (name,author,pubdate,type)
    try:
    # 执行sql语句
        cursor.execute(sql)
    # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接

    db.close()


