#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","123456","ebook" )
cursor = db.cursor()
# SQL 插入语句
sql = 'INSERT INTO bookinfo (book_name,book_author,book_pubdate,book_type) VALUES ("三生三世十里桃花","唐七公子","2009-1","言情")'
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