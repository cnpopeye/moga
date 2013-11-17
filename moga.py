#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 
 AUTHOR: zc  
 HOST: zc@zctekiMacBook-Pro.local
 PATH: /Users/zc/workspace/moga/moga.py
 DATE: 2013-11-17 13:47:43  
 
   
 INTRODUCTION:
    <<introduction write on here>>
     
 CHANGLOG:
    # FORMAT: DATE TIME AUTHOR COMMENT
    # etc. 2013-11-17 13:47:43 zc  # comment on here.
    
    <<changelog write on here>> 
    
  
'''
import os
import sqlite3
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, g, request, session, redirect, url_for, \
     abort, render_template


app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE='./moga.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    MAXDEPT=2,
    ROOT_DIR="/Users/zc/n2200/Movie",
    TAGS = ["科幻","动作","战争","动画","故事","爱情","悬疑",\
            "喜剧","灾难","恐怖","魔幻"]
))
app.config.from_envvar('MOGA_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.text_factory = str
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

films=[]

def find_dir(rootDir, level = 1):
    "遍历指定目录所有子目录"
    maxdept = app.config["MAXDEPT"]
    for item in os.listdir(rootDir):
        path = os.path.join(rootDir, item)
        if level==maxdept and item[:1]<>".":
            films.append((item,path))
        #print '│  '*(level-1)+'│--'+dir_ 
        if os.path.isdir(path) and level <maxdept \
          and item[:1]<>".": 
            find_dir(path, level+1)


def into_db(data):
    "存入sqlite"
    db = get_db()
    rowcount = 0
    try:
        db.execute("delete from films")
        cur = db.executemany("INSERT INTO films(film_name, full_path) VALUES (?,?)", data)
        rowcount = cur.rowcount
    except Exception,e:
        print "into_db:",e
        db.rollback()
    else:
        db.commit()
    return rowcount


@app.route('/ensureindex')
def ensure_index():
    "建立film 索引数据"
    global films
    films = []
    find_dir(app.config['ROOT_DIR'])
    res = 0
    if films:
        res = into_db(films)
    return str(res)


@app.route('/')
def show_films():
    db = get_db()
    cur = db.execute('select id, film_name, tags from films')
    films = cur.fetchall()
    return render_template('index.html', films = films)

# main function
if __name__ == '__main__':
    #init_db()
    app.run()


