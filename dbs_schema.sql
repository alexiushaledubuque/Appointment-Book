drop table if exists apptTable;
create table apptTable (
id integer primary key autoincrement,
apptDate text not null,
apptTime text not null,
description text not null
);
