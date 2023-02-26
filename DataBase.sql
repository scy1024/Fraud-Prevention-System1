
CREATE TABLE `employees` (
  `employee_id` int(6) NOT NULL DEFAULT '0',
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `hire_date` date NOT NULL,
  `salary` double(8,2) DEFAULT NULL,

  `PASSWORD` varchar(16) DEFAULT NULL,
  `loginTime` date DEFAULT NULL,
  `facaData` mediumblob  DEFAULT NULL,
  `Employ_type` char(4) check(Employ_type='admin_emp' or Employ_type='normal_emp') not null,
   
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `emp_email_uk` (`email`),
  UNIQUE KEY `emp_emp_id_pk` (`employee_id`),
  

) ENGINE=InnoDB DEFAULT CHARSET=utf8;



