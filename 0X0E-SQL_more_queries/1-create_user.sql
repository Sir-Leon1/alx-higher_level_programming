-- Create server user user_0d_1
CREATE USER IF USER NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PREVILEGES ON *.* TO 'user_0d_1'@'localhost';
