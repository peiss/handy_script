# coding: utf8
'''
Created on 2016年1月5日

@author: crazyant
'''

from crazyant.conf import blog_conf
import MySQLdb

output_fpath = "%s/src/crazyant/output/blog_article_list.html" % blog_conf.PROJECT_CODES_HOME

def query_all_articles():
    sql = """ SELECT ID as id,post_title,post_date 
                FROM wp_posts 
                WHERE 
                    post_status='publish' 
                    AND post_type='post' 
                ORDER BY post_date DESC;"""
    cursor = blog_conf.conn_czt.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("set names utf8;")
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

def write_html(out_fpath, articles):
    fout = open(out_fpath, "w")
    for row in articles:
        article_id = row['id']
        article_title = row['post_title']
        article_time = str(row['post_date'])[:10]
        
        fout.write('%s <a href="http://www.crazyant.net/%s.html" target="_blank">%s</a> <br /> \n' % (article_time, article_id, article_title))
        

articles = query_all_articles()
write_html(output_fpath, articles)

