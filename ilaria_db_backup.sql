-- MySQL dump 10.13  Distrib 8.4.8, for Linux (x86_64)
--
-- Host: localhost    Database: ILARIA_DB
-- ------------------------------------------------------
-- Server version	8.4.8

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
-- Table structure for table `about`
--

DROP TABLE IF EXISTS `about`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `about` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about`
--

LOCK TABLES `about` WRITE;
/*!40000 ALTER TABLE `about` DISABLE KEYS */;
INSERT INTO `about` VALUES (1,'<p>Hi! I’m Alex Parker, a passionate photographer with a love for capturing life’s most memorable moments. From striking landscapes to intimate portraits, I strive to tell stories through every frame. Photography isn’t just what I do—it’s how I see the world.</p><p>Over the years, I’ve worked on a variety of projects, from personal artistic explorations to professional commissions, always aiming to blend creativity with authenticity. This portfolio showcases my journey, my projects, and my thoughts on photography through my blog.</p><p>Whether you’re looking to collaborate on a project or just exploring the art of photography, I hope my work inspires you and sparks your imagination.</p>');
/*!40000 ALTER TABLE `about` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('714c3c6f2c22');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `image` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (3,'dvfs',NULL,'paisage1.jpeg'),(11,'bloggg','<p>serhehwehwa4</p>','blog2.jpeg'),(12,'more blog',NULL,'blog1.jpeg'),(13,'other post','<p>kletdyujiawsa</p>','aboutme_alexmore.jpeg'),(14,'sdfsa','<p>sdhsejheryhw</p>','paisage2.jpeg'),(16,'leonn',NULL,'fb54aad365e344449f903a80a85ab259_animals_lion.jpeg'),(17,'rghdrh','<p>sdjhsejse</p>','41fd3465df794b5d98b3d318968b5f07_paisage1.jpeg'),(18,'ghdjkhj,u','<p>sdfhsdjhs</p>','859285fe621947a7b593cc2495b4a7d0_aboutme_camera.jpeg'),(19,'drj,rsj','<p>sdhfsdhsd</p>','7ec14c9060b14253a9ca147bb2585cc1_home_cards_2.jpeg'),(20,'dfgbd',NULL,'73aeac23f9de4f439becfa2163a91588_paisage1.jpeg'),(21,'sghsdfjhftjsr','<p>sdfjhsjaes</p>','89695853e00b43c5be3a3b2b5921d650_animals_fox.jpg'),(22,'fhsdh','<p>teawrtyseah</p>','a3d38978f4374a48a7852083d757a1d4_blog2.jpeg'),(23,'gsdgs','<p>yjredtyjrsdj</p>','0d03cc9ad4d848da9bdeda063dcc082c_home_cards_1.jpeg'),(24,'sdfgs','<p>asfasfasdf</p>','e8c1047c9d4e4e0a86646ee0e6b83311_animals_fox.jpg'),(25,'wef','<p>erger</p>','3cc1500affdf479894c4b6fd3f99f357_aboutme_alexmore.jpeg');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `image` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (10,'project 235e423','<p>asdfasnf asdfasjvipjdb0p asvpjasvc sapvsa</p>','paisage2.jpeg'),(12,'fasdfasfasd','asdvasdasdfa','aboutme_camera.jpeg'),(14,'fgawfg','aerawerf','ea6143f609a6461392321932d372248c_blog2.jpeg'),(15,'dxvbdsvhd123123','<p>11112sdfghsdhsdfhsdfhsdfh</p><p>sdfgsdfg</p><p>sdfg</p><p>sdfg</p><p>sdf</p><p>gsdfgsdfgs</p><p>&nbsp;</p>','bbadbac6d5864df7a9e2181bc738061a_home_cards_4.jpeg'),(16,'hedhedr','<p>terger</p>','785575e208694721a500b11991cbdd35_home_hero_camera.jpeg'),(17,'gsdfgsd','<p>sdfgsdfgsdfg</p><p>sdfgsdfgs</p><p>sdfgsd</p><p>gsdfg</p><p>sdfg</p><p>sdfg</p><p>sdfgsdfgsdfgsdfgsdf</p><p>sdfgsd</p>','f2f751e3607a4216ab22708916d47a4d_aboutme_alexmore.jpeg'),(18,'sdafgsdrfhtn','<p>jsrtjhnserjhes<strong>gsdfgsd</strong></p><figure class=\"table\"><table><tbody><tr><td>sdfgsd</td><td><blockquote><p>sdfgsdg</p></blockquote><p>&nbsp;</p><p>&nbsp;</p></td></tr></tbody></table></figure><blockquote><p>youtube.com</p></blockquote>','62e573bd1bc941b59e12b31594899b3f_animals_lion.jpeg'),(19,'fvnbdfgb','<p>dsfgsdafgdfsasdf11</p>','528e62045c854f71b3b4873f42ec1551_paisage2.jpeg'),(20,'esdfgsdsdfgs','<h2>sdghsdfgsdfgsd</h2><p>dgsdgsdgd</p><p>sdgffsdgsdf</p>','df633b63d80b4007bea6a6436a145c6f_blog2.jpeg'),(21,'fsdgsd','<p>sdfgsd</p>','e278e028a726429e852236fad4730d1e_paisage1.jpeg'),(22,'rtywertyyerwter','<p>erwtyeryer</p>','5d2346ed9b564bb3a7416e6f7b3324c6_paisage2.jpeg'),(23,'teyerthrjhtgjmdgf','<p>dfsjmdtguk,sy,ksrtkjmsr</p>','5b388280698240b38a5f05a718727770_home_cards_4.jpeg'),(24,'fasdfas','<p>asdfgasfasf</p>','ae8ff6fd4631492a9dde08fd8c939394_home_cards_3.jpeg');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'user',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','scrypt:32768:8:1$78TJNcIlPTs2WtiI$31cd14497df9cadeb7d094b19a999ee467f2b9786df1b68c7e98b3b9fce644cec90da5c6089d5cd36be0de7eebee1b5d811fb22e56e36613b4ff635bb56612cf','admin'),(2,'user','scrypt:32768:8:1$6JBi0lUJ4AyAal06$e3777ff70217d15289ac7594ee9d3386fa5790df94f1593f977589facea829c9de72b20b3923238592b5a3c3cc12cbc97b54ccf4406ba51520d879561c4619c6','user'),(3,'user1','scrypt:32768:8:1$0YwEzEizV4wlXmlk$3f4a77cb7700ddfbddffef60f1ea9d65e450e087775f42d88a2fc2e95237ac1a27e8321936db901d09351b0b4726eef64fb3800019684cfecee143d74441e16f','user'),(4,'user2','scrypt:32768:8:1$AHhCl89GtErGi3L4$ee92aad85b1021a1d7e01192c332a427d9e244184cce784964acf13f0434040d1301ea9433ec7c73ce3aec2984fe84bdcc47d0db39b7c72ff5b7510d924b718a','user'),(5,'user23','scrypt:32768:8:1$daGUZwYHPrurYSPE$19ad9f719fa6334132258efa2390b60b3b30cbee604559778e973480f1fc2979bb64ee285fae58967d6ceb8ee68bfaf5518c958c4c80e8e31ea1bc7652a1c1ce','user'),(6,'user24','scrypt:32768:8:1$CfVPLUjnkqjB4H8u$5df545a0548269f8aa7f1b0e57a44b4ffbff4a10080285810cfe884b9cbcb7c7677c5d753201f963d2b4b2925f7ae5f0a7e408a5b8a0b11932975bb98dddc993','user');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-19  1:39:28
