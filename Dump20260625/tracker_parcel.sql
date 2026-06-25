-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: tracker
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `parcel`
--

DROP TABLE IF EXISTS `parcel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parcel` (
  `parcel_id` int NOT NULL AUTO_INCREMENT,
  `tracking_id` varchar(20) NOT NULL,
  `parcel_type` enum('Courier','Ecommerce') NOT NULL,
  `sender_name` varchar(100) DEFAULT NULL,
  `sender_phone` varchar(15) DEFAULT NULL,
  `receiver_name` varchar(100) DEFAULT NULL,
  `receiver_phone` varchar(15) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `weight` decimal(5,2) DEFAULT NULL,
  `booking_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `current_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`parcel_id`),
  UNIQUE KEY `tracking_id` (`tracking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parcel`
--

LOCK TABLES `parcel` WRITE;
/*!40000 ALTER TABLE `parcel` DISABLE KEYS */;
INSERT INTO `parcel` VALUES (1,'TRK1001','Courier','Dayana','9876543210','John','9123456780',NULL,1.20,'2025-06-20 10:00:00','Booked'),(2,'TRK1002','Courier','Arun','9876543211','Priya','9123456781',NULL,2.50,'2025-06-20 11:00:00','Picked Up'),(3,'TRK1003','Courier','Kavin','9876543212','Meena','9123456782',NULL,0.80,'2025-06-21 09:30:00','In Transit'),(4,'TRK1004','Courier','Rahul','9876543213','Sneha','9123456783',NULL,3.40,'2025-06-21 12:00:00','Delivered'),(5,'TRK1005','Courier','Vijay','9876543214','Anitha','9123456784',NULL,1.75,'2025-06-22 08:45:00','Out For Delivery'),(6,'TRK1006','Ecommerce','Amazon','180030009009','David','9123456785','Wireless Mouse',0.60,'2025-06-22 10:15:00','Booked'),(7,'TRK1007','Ecommerce','Flipkart','18002089898','Riya','9123456786','Smartphone',0.45,'2025-06-22 11:20:00','In Transit'),(8,'TRK1008','Ecommerce','Myntra','18004193500','Akhil','9123456787','T-Shirt',0.30,'2025-06-23 09:00:00','Delivered'),(9,'TRK1009','Ecommerce','Ajio','18008899999','Nisha','9123456788','Shoes',1.10,'2025-06-23 10:45:00','Picked Up'),(10,'TRK1010','Ecommerce','Snapdeal','18001027777','Karthik','9123456789','Bluetooth Speaker',1.80,'2025-06-23 01:30:00','Out For Delivery');
/*!40000 ALTER TABLE `parcel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-25 11:19:01
