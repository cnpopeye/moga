moga
====

Browser films and photos infomation with your local storeage(etc,NAS, USB Disk, FDD, HDD,SSD and so on).

依赖：
python 2.7.x
flask 
sqlite3

  feild     | type   | comment
------------|--------|----------
  id        |  int   |  auto id
film_name   | string | film name
full_path   | string | full path
intro_md    | string | INTRO.md path
intro_jpg   | string | intro.jpg path
tags        | string | tags ',' split




功能：

- 设置用户
- 浏览电影
- 浏览照片
- 重建索引（每当有新电影、照片加入后），索引保存为文本文件
  扫描指定（配置）目录，递归扫描  
- 抓取信息（根据索引，从互联网抓取影片信息），信息保存到INTRO.md
- TAG管理（）



电影：
一个电影一个文件夹，结构如下：

```
.
├── INTRO.md(require)
├── film file.mkv(require)
├── film sample file.mkv(optional)
└── intro.jpg(require)
```

其中INTRO.md文件为电影描述文件，包括如下结构：
封面图片：<intro.jpg>
影片基本：
演职员信息：
影片简介：




照片：
