-- Drop Tables===========>
-- SET FOREIGN_KEY_CHECKS = 0;
-- drop table if exists user;
-- drop table if exists company;
-- drop table if exists jobposted;
-- SET FOREIGN_KEY_CHECKS = 1;

-- ************************************** `Product` >>
CREATE TABLE `product`
(
 `p_id`       INT NOT NULL AUTO_INCREMENT ,
 `pname`     VARCHAR(50) NOT NULL ,
 `type`     VARCHAR(20) NOT NULL ,
 `pack`     INT NOT NULL ,
 `c_id`       INT NOT NULL,
 `sh_id`       INT NOT NULL,
 PRIMARY KEY (`p_id`),
 FOREIGN KEY (c_id) REFERENCES company(c_id),
 FOREIGN KEY (sh_id) REFERENCES shelf(sh_id)
);

-- ************************************** `company`>>

CREATE TABLE `company`
(
 `c_id`       INT NOT NULL AUTO_INCREMENT,
 `cname`     VARCHAR(50) NOT NULL ,
 PRIMARY KEY (`c_id`)
);


-- ************************************** `shelf`>>

CREATE TABLE `shelf`
(
 `sh_id`       INT NOT NULL AUTO_INCREMENT,
 `shelf`     VARCHAR(50) NOT NULL ,
 PRIMARY KEY (`sh_id`)
);


-- ************************************** `user` >>
CREATE TABLE `user`
(
 `u_id`       INT NOT NULL AUTO_INCREMENT ,
 `uname`     VARCHAR(20) NOT NULL ,
 `email`     VARCHAR(50) NOT NULL ,
 `password`  VARCHAR(100) NOT NULL ,
 PRIMARY KEY (`u_id`)
 );


 -- ************************************** `Distributor` >>
CREATE TABLE `distributor`
(
 `d_id`       INT NOT NULL AUTO_INCREMENT ,
 `dname`     VARCHAR(30) NOT NULL ,
 `contact`     VARCHAR(20) NOT NULL ,
 `descript`  VARCHAR(500) NOT NULL ,
 PRIMARY KEY (`d_id`)
 );

--============================================='Booker'>>

CREATE TABLE `booker`
(
 `b_id`       INT NOT NULL AUTO_INCREMENT ,
 `bname`     VARCHAR(50) NOT NULL ,
 `phone`     VARCHAR(20) NOT NULL ,
 `descript`  VARCHAR(500) NOT NULL ,
 `d_id`       INT NOT NULL,
 PRIMARY KEY (`b_id`),
 FOREIGN KEY (d_id) REFERENCES distributor(d_id)
);



--============================================='Stock'>>

CREATE TABLE `stock`
(
 `s_id`       INT NOT NULL AUTO_INCREMENT ,
 `pprice`     DOUBLE NOT NULL,
 `sprice`     DOUBLE NOT NULL,
 `p_id`       INT NOT NULL,
 `b_id`       INT NOT NULL,
  `time`     DATETIME DEFAULT CURRENT_TIMESTAMP,
 `descript`  VARCHAR(500) NOT NULL ,
 PRIMARY KEY (`s_id`),
 FOREIGN KEY (b_id) REFERENCES booker(b_id),
 FOREIGN KEY (p_id) REFERENCES product(p_id)
);

