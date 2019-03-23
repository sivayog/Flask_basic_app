drop table if exist country;
create table country(
 id integer primary key autoincrement;
 name text not null
 );


  drop table if exists member;
create table member (
  id integer primary key autoincrement,
  country_id integer,
  name text not null
);

drop table if exists member_info;
create table member_info (
  id integer primary key autoincrement,
  member_id integer,
  address text not null,
  city text
);
