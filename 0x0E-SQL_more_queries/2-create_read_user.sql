-- Creates a user and a database
-- Grant select privileges to user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_d';
GRANT SELECT ON hbtn_0d_2 . * TO 'user_0d_2'@'localhost';
