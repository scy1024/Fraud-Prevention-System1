
--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUSTOMER` (
  `CID` CHAR(9) NOT NULL,
  `FNAME` VARCHAR(50) NOT NULL,
  `LNAME` VARCHAR(50) NOT NULL,
  `EMAIL` VARCHAR(50) NOT NULL,
  `ADDRESS` VARCHAR(50) NOT NULL,
  `PHONE` CHAR(10) NOT NULL,
  `STATUS` INT(11) NOT NULL,
  `PASSWORD` VARCHAR(16) DEFAULT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=INNODB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER`
--


LOCK TABLES `CUSTOMER` WRITE;
/*!40000 ALTER TABLE `CUSTOMER` DISABLE KEYS */;
INSERT INTO `CUSTOMER` VALUES ('100000000','admin','manager','espoyao@gmail.com','Nutley','0000000000',9,'12345'),('100000001','Shibo','Yao','sy123@njit.edu','567 Central Ave, Harrison, NJ','1233211234',0,'1234'),('100000002','Shaobo','Liu','sl638@njit.edu','435 Forest St, Kearny, NJ','2012732585',1,NULL),('100000003','Jeremy','Hui','jh123@njit.edu','Harrison','1234567890',0,'123'),('100000004','test','T','test@gmail.com','NJIT','6666777888',0,'6666777888'),('100000005','YanYi','Fong','yan@gmail.com','NY','7778889999',0,'17778889999'),('100000006','Jim','Yao','jy@gmail.com','China','1333333333',2,'1234'),('100000007','Dimitri','Theodo','dt@njit.edu','NJIT','2222333444',0,'2222333444'),('100000008','Lilian','Kuo','lk@njit.edu','NJIT','2222999900',0,'222'),('100000009','Yan','Shu','sy@ucsd.edu','Walmart','2222333333',0,'2222'),('100000010','test21','t','sy372','njit','1111111111',0,'123'),('100000011','ShaoBo','Liu','sliu36@stevens.edu','412 Central Ave, Newark','2132421111',0,'111');
/*!40000 ALTER TABLE `CUSTOMER` ENABLE KEYS */;
UNLOCK TABLES;