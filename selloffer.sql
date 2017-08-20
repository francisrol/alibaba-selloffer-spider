CREATE DATABASE alibaba CHARSET utf8;
CREATE USER 'alibaba'@'%' IDENTIFIED BY 'alibaba';
GRANT ALL ON alibaba.* TO 'alibaba';

USE alibaba;

CREATE TABLE category(
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT UNIQUE,
name VARCHAR(30) UNIQUE,
link VARCHAR(512),
shortcut VARCHAR(100)
)ENGINE=INNODB;

CREATE TABLE sub_category(
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT UNIQUE,
name VARCHAR(63) UNIQUE,
link VARCHAR(512),
parent VARCHAR(30),
shortcut VARCHAR(100),
FOREIGN KEY (parent) REFERENCES category(name)
)ENGINE=INNODB;


CREATE TABLE selloffer(
`id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT UNIQUE,
`name` VARCHAR(63),
`url` VARCHAR(512),
`shortcut` VARCHAR(31),
`business_model` VARCHAR(15),
`linkman` VARCHAR(15),
`landline_phone` VARCHAR(63),
`mobile_phone` VARCHAR(63),
`address` VARCHAR(512),
`zipcode` VARCHAR(31),
`create_time` DATETIME ,
`category_id` INT UNSIGNED,
`sub_category_id` INT UNSIGNED,
FOREIGN KEY (category_id) REFERENCES category(id),
FOREIGN KEY (sub_category_id) REFERENCES sub_category(id),
KEY (category_id),
KEY (sub_category_id),
KEY (shortcut)
)ENGINE=INNODB;