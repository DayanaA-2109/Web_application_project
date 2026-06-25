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
-- Table structure for table `tracking`
--

DROP TABLE IF EXISTS `tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracking` (
  `tracking_record_id` int NOT NULL AUTO_INCREMENT,
  `tracking_id` varchar(20) NOT NULL,
  `current_location` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `hub_name` varchar(100) DEFAULT NULL,
  `delivery_agent` varchar(100) DEFAULT NULL,
  `vehicle_number` varchar(30) DEFAULT NULL,
  `estimated_delivery_date` date DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`tracking_record_id`),
  KEY `tracking_id` (`tracking_id`),
  CONSTRAINT `tracking_ibfk_1` FOREIGN KEY (`tracking_id`) REFERENCES `parcel` (`tracking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracking`
--

LOCK TABLES `tracking` WRITE;
/*!40000 ALTER TABLE `tracking` DISABLE KEYS */;
INSERT INTO `tracking` VALUES (1,'TRK1001','Chennai','Booked','Chennai Hub',NULL,NULL,'2026-06-30','Parcel booked successfully','2026-06-24 21:14:03'),(2,'TRK1002','Madurai','Picked Up','Madurai Hub','Karthik','TN58AB1234','2026-06-29','Parcel collected from sender','2026-06-24 21:14:03'),(3,'TRK1003','Trichy','In Transit','Trichy Hub',NULL,'TN45CD5678','2026-06-30','Parcel moving to next hub','2026-06-24 21:14:03'),(4,'TRK1004','Salem','Reached Hub','Salem Hub',NULL,'TN30EF9876','2026-07-01','Parcel arrived at Salem hub','2026-06-24 21:14:03'),(5,'TRK1005','Coimbatore','Dispatched','Coimbatore Hub',NULL,'TN37GH5432','2026-07-01','Parcel dispatched from hub','2026-06-24 21:14:03'),(6,'TRK1006','Bangalore','Out for Delivery','Bangalore Hub','Ravi Kumar','KA01JK1122','2026-06-28','Delivery agent assigned','2026-06-24 21:14:03'),(7,'TRK1007','Hyderabad','Delivered','Hyderabad Hub','Suresh','TS09LM3344','2026-06-27','Parcel delivered successfully','2026-06-24 21:14:03'),(8,'TRK1008','Vellore','Delayed','Vellore Hub',NULL,'TN23PQ5566','2026-07-02','Delivery delayed due to weather','2026-06-24 21:14:03'),(9,'TRK1009','Erode','Returned','Erode Hub','Manoj','TN33RS7788','2026-07-03','Receiver unavailable','2026-06-24 21:14:03'),(10,'TRK1010','Tirunelveli','Cancelled','Tirunelveli Hub',NULL,NULL,'2026-07-04','Shipment cancelled by sender','2026-06-24 21:14:03');
/*!40000 ALTER TABLE `tracking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-25 11:19:00
