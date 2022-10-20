-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (arm64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `like_list`
--

DROP TABLE IF EXISTS `like_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_list` (
  `who_likes_it` varchar(255) NOT NULL,
  `how_many` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`how_many`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_list`
--

LOCK TABLES `like_list` WRITE;
/*!40000 ALTER TABLE `like_list` DISABLE KEYS */;
INSERT INTO `like_list` VALUES ('Maggie',1),('Amy',2);
/*!40000 ALTER TABLE `like_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `username_index` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',10,'2022-10-17 16:10:10'),(2,'Mike','mike123','mike123',20,'2022-10-17 16:14:04'),(3,'Jim','jim123','jim123',50,'2022-10-17 16:14:47'),(4,'Maggie','maggie123','maggie123',500,'2022-10-17 16:16:09'),(5,'Amy','amy123','amy123',5,'2022-10-17 16:17:02'),(6,'Jush','test','test',30,'2022-10-18 11:39:27'),(7,'Amber','test','test',70,'2022-10-18 11:39:47'),(8,'Patty','test','test',2,'2022-10-18 11:40:17');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_msg`
--

DROP TABLE IF EXISTS `member_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_msg` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_like` bigint NOT NULL,
  `message_like` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `member_like` (`member_like`),
  KEY `message_like` (`message_like`),
  CONSTRAINT `member_msg_ibfk_1` FOREIGN KEY (`member_like`) REFERENCES `member` (`id`),
  CONSTRAINT `member_msg_ibfk_2` FOREIGN KEY (`message_like`) REFERENCES `message` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_msg`
--

LOCK TABLES `member_msg` WRITE;
/*!40000 ALTER TABLE `member_msg` DISABLE KEYS */;
INSERT INTO `member_msg` VALUES (4,4,6),(5,2,2),(6,1,2),(7,2,3),(8,4,1),(9,1,4),(10,4,1),(11,5,1);
/*!40000 ALTER TABLE `member_msg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'安安',15,'2022-10-18 11:27:25'),(2,2,'你好',3,'2022-10-18 11:36:06'),(3,3,'哈哈',50,'2022-10-18 11:37:07'),(4,6,'呵呵',10,'2022-10-18 11:44:34'),(5,7,'嘻嘻',90,'2022-10-18 11:45:01'),(6,8,'UU',40,'2022-10-18 11:45:34'),(7,4,'讚',20,'2022-10-18 12:01:55'),(8,5,'讚讚',10,'2022-10-18 12:02:13');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-20 15:03:52
