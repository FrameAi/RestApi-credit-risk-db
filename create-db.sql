CREATE TABLE `companies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1



CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `created_at` timestamp(2) NULL DEFAULT NULL,
  `related_company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_related_company_id_idx` (`related_company_id`),
  CONSTRAINT `fk_users_companies_related_company_id` FOREIGN KEY (`related_company_id`) REFERENCES `companies` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1



CREATE TABLE `customer_results` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `probability_of_default_next_month` decimal(2,0) DEFAULT NULL,
  `feedback_did_default` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `credit_limit_balance` int(11) DEFAULT NULL,
  `education` enum('graduate school','university','high school','others') DEFAULT NULL,
  `marriage` enum('married','single','other') DEFAULT NULL,
  `age` smallint(2) DEFAULT NULL,
  `repayment_status_month_1` tinyint(1) DEFAULT NULL,
  `repayment_status_month_2` tinyint(1) DEFAULT NULL,
  `repayment_status_month_3` tinyint(1) DEFAULT NULL,
  `repayment_status_month_4` tinyint(1) DEFAULT NULL,
  `repayment_status_month_5` tinyint(1) DEFAULT NULL,
  `repayment_status_month_6` tinyint(1) DEFAULT NULL,
  `bill_amount_month_1` int(11) DEFAULT NULL,
  `bill_amount_month_2` int(11) DEFAULT NULL,
  `bill_amount_month_3` int(11) DEFAULT NULL,
  `bill_amount_month_4` int(11) DEFAULT NULL,
  `bill_amount_month_5` int(11) DEFAULT NULL,
  `bill_amount_month_6` int(11) DEFAULT NULL,
  `payment_amount_month_1` int(11) DEFAULT NULL,
  `payment_amount_month_2` int(11) DEFAULT NULL,
  `payment_amount_month_3` int(11) DEFAULT NULL,
  `payment_amount_month_4` int(11) DEFAULT NULL,
  `payment_amount_month_5` int(11) DEFAULT NULL,
  `payment_amount_month_6` int(11) DEFAULT NULL,
  `related_user_id` int(11) DEFAULT NULL,
  `customer_result_id` int(11) DEFAULT NULL,
  `created_at` timestamp(2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customers_users_related_user_id_idx` (`related_user_id`),
  KEY `fk_customers_customer_results_customer_result_id_idx` (`customer_result_id`),
  CONSTRAINT `fk_customers_customer_results_customer_result_id` FOREIGN KEY (`customer_result_id`) REFERENCES `customer_results` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_customers_users_related_user_id` FOREIGN KEY (`related_user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1


