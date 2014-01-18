#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 
 AUTHOR: zc  
 HOST: zc@zctekiMacBook-Pro.local
 PATH: /Users/zc/workspace/moga/utils.py
 DATE: 2014-01-18 13:00:17  
 
   
 INTRODUCTION:
    scanning files of special dir.
     
 CHANGLOG:
    # FORMAT: DATE TIME AUTHOR COMMENT
    # etc. 2014-01-18 13:00:17 zc  # comment on here.
    
    <<changelog write on here>> 
    
  
'''
import os

def scan_file(the_dir):
    "扫描指定目录文件"
    # 获取目录下所有项目
    for item in os.listdir(the_dir):
        path = os.path.join(the_dir, item)
        # 如果还是文件夹，则递归扫描
        if os.path.isdir(path):
            scan_file(path)

