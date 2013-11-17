drop table if exists films;
create table films(
       id integer primary key autoincrement, 
       film_name text not null, 
       full_path text not null, 
       intro_md text, 
       intro_jpg text, 
       tags text
);
