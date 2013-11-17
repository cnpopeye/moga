#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 
 AUTHOR: zc  
 HOST: zc@zctekiMacBook-Pro.local
 PATH: /Users/zc/workspace/moga/ensure_index.py
 DATE: 2013-11-17 09:34:58  
 
   
 INTRODUCTION:
   递归遍历2级深度目录，过滤有隐藏目录（.开头目录）
     
 CHANGLOG:
    # FORMAT: DATE TIME AUTHOR COMMENT
    # etc. 2013-11-17 09:34:58 zc  # comment on here.
    
    <<changelog write on here>> 
    
  
'''

import os
import sqlite3

from config import root_dir, maxdept, db_name


films = []
def ensure_index():
    "建立film 索引数据"
#    films=[]
    films_=[]
    find_dir(root_dir)
    inc = 0
    for f in films:
        inc = inc +1
        item = list(f)
        item.insert(0, str(inc))
        films_.append( tuple(item) )
    res = into_db(films_)
    return res


def find_dir(rootDir, level = 1):
    "遍历指定目录所有子目录"
    for item in os.listdir(rootDir):
        path = os.path.join(rootDir, item)
        if level==maxdept and item[:1]<>".":
            films.append((item,path))
        #print '│  '*(level-1)+'│--'+dir_ 
        if os.path.isdir(path) and level <maxdept and item[:1]<>".": 
            find_dir(path, level+1)


def into_db(data):
    "存入sqlite"
    conn = sqlite3.connect(db_name)
    conn.text_factory = str
    c = conn.cursor()
    rowcount = 0
    try:
        try:
            #Drop Table
            c.execute('''DROP TABLE film''')
        except:
            pass

        # Create table 
        c.execute('''CREATE TABLE film(id, film_name, full_path, intro_md, intro_jpg, tags)''')
        c.executemany("INSERT INTO film(id, film_name, full_path) VALUES (?,?,?)", data)
        rowcount = c.rowcount
    except Exception,e:
        print e
        conn.rollback()
    else:
        conn.commit()
    finally:
        conn.close()
    return rowcount



