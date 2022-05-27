drop database if exists pets ;

create database pets;

\c pets

create table adopt
(
    id serial primary key,
    name text not null,
    species text not null,
    photo_url text,
    age integer,
    notes text,
    available boolean not null default True
);

insert into adopt (name, species, age, notes, available, photo_url)
values ('Roger', 'Beagle', 8, 'Really likes bacon', True, 'https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg')
