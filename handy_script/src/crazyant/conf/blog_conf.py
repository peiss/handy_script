# coding: utf8
'''
Created on 2016年1月5日

@author: crazyant
'''

import MySQLdb

# 链接本地的博客数据库
conn_czt = MySQLdb.Connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='pssftpuser')

# 项目的路径
PROJECT_CODES_HOME = "D:/workbench/python/handy_script"
