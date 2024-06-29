-- Pay Attention : you should test this in MYSQL Workbench

-- in order to see all the privileges in DB do this:
-- show privileges

-- in order to get the connection via Arousha_Azad you can create a connection with the username and password
-- of Arousha, then you can use these functions:
-- 1- use db;   -> you should add this in order to connect to your special DataBase(via its name) through Arousha
-- 2- drop table contacts; -> when you run this, It will not be excecuted, because there is no delete permission to Arousha
-- 3- show grants; -> you can run this in order to see the permission given to Arousha

CREATE ROLE just_read_user;
GRANT SELECT ON db.* TO just_read_user;
CREATE USER 'Arousha_Azad' IDENTIFIED BY 'Arousha2000azad' DEFAULT ROLE 'just_read_user';