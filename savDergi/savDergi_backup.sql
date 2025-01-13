-- MySQL dump 10.13  Distrib 9.0.1, for macos15.1 (arm64)
--
-- Host: localhost    Database: savDergi
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `admin_honeypot_loginattempt`
--

DROP TABLE IF EXISTS `admin_honeypot_loginattempt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_honeypot_loginattempt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `session_key` varchar(50) DEFAULT NULL,
  `user_agent` longtext,
  `timestamp` datetime(6) NOT NULL,
  `path` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_honeypot_loginattempt`
--

LOCK TABLES `admin_honeypot_loginattempt` WRITE;
/*!40000 ALTER TABLE `admin_honeypot_loginattempt` DISABLE KEYS */;
INSERT INTO `admin_honeypot_loginattempt` VALUES (1,'furkanvarol','127.0.0.1','zmui5sw6mtd0mrdk6m8zg5hnwses9ojy','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','2024-12-30 12:18:30.599626','/admin/login/?next=/admin/'),(2,'furkanvarol','127.0.0.1','zmui5sw6mtd0mrdk6m8zg5hnwses9ojy','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','2024-12-30 12:18:38.773380','/admin/login/?next=/admin/');
/*!40000 ALTER TABLE `admin_honeypot_loginattempt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add album',7,'add_album'),(26,'Can change album',7,'change_album'),(27,'Can delete album',7,'delete_album'),(28,'Can view album',7,'view_album'),(29,'Can add duyuru',8,'add_duyuru'),(30,'Can change duyuru',8,'change_duyuru'),(31,'Can delete duyuru',8,'delete_duyuru'),(32,'Can view duyuru',8,'view_duyuru'),(33,'Can add embedded video',9,'add_embeddedvideo'),(34,'Can change embedded video',9,'change_embeddedvideo'),(35,'Can delete embedded video',9,'delete_embeddedvideo'),(36,'Can view embedded video',9,'view_embeddedvideo'),(37,'Can add makale',10,'add_makale'),(38,'Can change makale',10,'change_makale'),(39,'Can delete makale',10,'delete_makale'),(40,'Can view makale',10,'view_makale'),(41,'Can add sayi',11,'add_sayi'),(42,'Can change sayi',11,'change_sayi'),(43,'Can delete sayi',11,'delete_sayi'),(44,'Can view sayi',11,'view_sayi'),(45,'Can add duyuru image',12,'add_duyuruimage'),(46,'Can change duyuru image',12,'change_duyuruimage'),(47,'Can delete duyuru image',12,'delete_duyuruimage'),(48,'Can view duyuru image',12,'view_duyuruimage'),(49,'Can add duyuru text',13,'add_duyurutext'),(50,'Can change duyuru text',13,'change_duyurutext'),(51,'Can delete duyuru text',13,'delete_duyurutext'),(52,'Can view duyuru text',13,'view_duyurutext'),(53,'Can add image',14,'add_image'),(54,'Can change image',14,'change_image'),(55,'Can delete image',14,'delete_image'),(56,'Can view image',14,'view_image'),(57,'Can add makale anahtar',15,'add_makaleanahtar'),(58,'Can change makale anahtar',15,'change_makaleanahtar'),(59,'Can delete makale anahtar',15,'delete_makaleanahtar'),(60,'Can view makale anahtar',15,'view_makaleanahtar'),(61,'Can add makale kaynak',16,'add_makalekaynak'),(62,'Can change makale kaynak',16,'change_makalekaynak'),(63,'Can delete makale kaynak',16,'delete_makalekaynak'),(64,'Can view makale kaynak',16,'view_makalekaynak'),(65,'Can add makale text',17,'add_makaletext'),(66,'Can change makale text',17,'change_makaletext'),(67,'Can delete makale text',17,'delete_makaletext'),(68,'Can view makale text',17,'view_makaletext'),(69,'Can add makale yazar',18,'add_makaleyazar'),(70,'Can change makale yazar',18,'change_makaleyazar'),(71,'Can delete makale yazar',18,'delete_makaleyazar'),(72,'Can view makale yazar',18,'view_makaleyazar'),(73,'Can add portre',19,'add_portre'),(74,'Can change portre',19,'change_portre'),(75,'Can delete portre',19,'delete_portre'),(76,'Can view portre',19,'view_portre'),(77,'Can add konferans',20,'add_konferans'),(78,'Can change konferans',20,'change_konferans'),(79,'Can delete konferans',20,'delete_konferans'),(80,'Can view konferans',20,'view_konferans'),(81,'Can add metodoloji',21,'add_metodoloji'),(82,'Can change metodoloji',21,'change_metodoloji'),(83,'Can delete metodoloji',21,'delete_metodoloji'),(84,'Can view metodoloji',21,'view_metodoloji'),(85,'Can add sava',22,'add_sava'),(86,'Can change sava',22,'change_sava'),(87,'Can delete sava',22,'delete_sava'),(88,'Can view sava',22,'view_sava'),(89,'Can add album image',14,'add_albumimage'),(90,'Can change album image',14,'change_albumimage'),(91,'Can delete album image',14,'delete_albumimage'),(92,'Can view album image',14,'view_albumimage'),(93,'Can add konferans image',23,'add_konferansimage'),(94,'Can change konferans image',23,'change_konferansimage'),(95,'Can delete konferans image',23,'delete_konferansimage'),(96,'Can view konferans image',23,'view_konferansimage'),(97,'Can add metodoloji image',24,'add_metodolojiimage'),(98,'Can change metodoloji image',24,'change_metodolojiimage'),(99,'Can delete metodoloji image',24,'delete_metodolojiimage'),(100,'Can view metodoloji image',24,'view_metodolojiimage'),(101,'Can add sava image',25,'add_savaimage'),(102,'Can change sava image',25,'change_savaimage'),(103,'Can delete sava image',25,'delete_savaimage'),(104,'Can view sava image',25,'view_savaimage'),(105,'Can add login attempt',26,'add_loginattempt'),(106,'Can change login attempt',26,'change_loginattempt'),(107,'Can delete login attempt',26,'delete_loginattempt'),(108,'Can view login attempt',26,'view_loginattempt');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$IAg0SmJap2SXa6psT0nzVH$kJrhVeo63zR23xugjykUdw1rr9TmxUuMD6OFcMjb1zY=','2024-12-30 11:58:14.000000',1,'furkanvarol','','','3756furkan@gmail.com',1,1,'2024-12-06 01:31:31.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_album`
--

DROP TABLE IF EXISTS `base_album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_album` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_album`
--

LOCK TABLES `base_album` WRITE;
/*!40000 ALTER TABLE `base_album` DISABLE KEYS */;
INSERT INTO `base_album` VALUES (1,'cart curt','2024-12-08 13:43:54.763330','2024-12-12 19:44:11.216696','cart-curt'),(2,'kart kurt','2024-12-13 01:54:30.150291','2024-12-13 01:54:30.150307','kart-kurt'),(3,'part purt','2024-12-13 03:12:17.475483','2024-12-13 03:12:17.475541','part-purt'),(4,'lap lup','2024-12-13 03:20:44.291419','2024-12-13 03:20:44.291452','lap-lup'),(5,'çatara patara','2024-12-13 03:25:19.678696','2024-12-13 03:25:19.678743','catara-patara');
/*!40000 ALTER TABLE `base_album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_albumimage`
--

DROP TABLE IF EXISTS `base_albumimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_albumimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `name_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_image_name_id_7bbf23b4_fk_base_album_id` (`name_id`),
  CONSTRAINT `base_image_name_id_7bbf23b4_fk_base_album_id` FOREIGN KEY (`name_id`) REFERENCES `base_album` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_albumimage`
--

LOCK TABLES `base_albumimage` WRITE;
/*!40000 ALTER TABLE `base_albumimage` DISABLE KEYS */;
INSERT INTO `base_albumimage` VALUES (1,'images/IMG_2244_iyMB5d3.JPG','2024-12-08 13:43:54.773593',1),(2,'images/IMG_3762_Iqn87Dh.JPG','2024-12-08 13:43:54.777306',1),(3,'images/IMG_0349_XeyoPK5.JPG','2024-12-12 19:44:11.225214',1),(4,'images/IMG_2064_dUe0vg8.JPG','2024-12-12 19:44:11.227244',1),(5,'images/IMG_0504_sM8uxOX.JPG','2024-12-12 19:44:11.228263',1),(6,'images/efa72e67-8e7d-4123-9865-295948346a37_c2Fr0b4.jpg','2024-12-13 01:54:30.159283',2),(7,'images/FkHCUPsX0AEb8_d.jpeg','2024-12-13 01:54:30.160121',2),(8,'images/IMG_0349_qwfeuq9.JPG','2024-12-13 01:54:30.160682',2),(9,'images/IMG_2781_iK4Zpro.JPG','2024-12-13 01:54:30.161342',2),(10,'images/IMG_6604_PqgIPvR.JPG','2024-12-13 01:54:30.161857',2),(11,'images/IMG_5863.JPG','2024-12-13 01:54:30.162471',2),(12,'images/IMG_4564.JPG','2024-12-13 03:12:17.487263',3),(13,'images/IMG_3591.PNG','2024-12-13 03:12:17.489780',3),(14,'images/IMG_9985_Qwnj155.JPG','2024-12-13 03:12:17.491993',3),(15,'images/IMG_3598.JPG','2024-12-13 03:20:44.302129',4),(16,'images/IMG_3596.JPG','2024-12-13 03:25:19.690392',5);
/*!40000 ALTER TABLE `base_albumimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_duyuru`
--

DROP TABLE IF EXISTS `base_duyuru`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_duyuru` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `topic` varchar(200) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `created` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_duyuru`
--

LOCK TABLES `base_duyuru` WRITE;
/*!40000 ALTER TABLE `base_duyuru` DISABLE KEYS */;
INSERT INTO `base_duyuru` VALUES (1,'annen','2024-12-09 02:45:02.887340','2024-12-09 02:45:02.887382','annen'),(2,'baban','2024-12-09 02:45:15.800944','2024-12-09 02:45:15.801029','baban'),(3,'duyuru 3','2024-12-13 01:38:37.424679','2024-12-11 20:46:56.893948','duyuru-3'),(4,'duyuru 4','2024-12-16 18:05:02.456636','2024-12-16 18:05:02.456659','duyuru-4');
/*!40000 ALTER TABLE `base_duyuru` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_duyuruimage`
--

DROP TABLE IF EXISTS `base_duyuruimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_duyuruimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `topic_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_duyuruimage_topic_id_9d6f93de_fk_base_duyuru_id` (`topic_id`),
  CONSTRAINT `base_duyuruimage_topic_id_9d6f93de_fk_base_duyuru_id` FOREIGN KEY (`topic_id`) REFERENCES `base_duyuru` (`id`),
  CONSTRAINT `base_duyuruimage_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_duyuruimage`
--

LOCK TABLES `base_duyuruimage` WRITE;
/*!40000 ALTER TABLE `base_duyuruimage` DISABLE KEYS */;
INSERT INTO `base_duyuruimage` VALUES (1,'images/1714413551733.jpeg','2024-12-11 20:46:56.896492',2,3),(2,'images/Adsız_tasarım.png','2024-12-16 18:05:02.467296',0,4);
/*!40000 ALTER TABLE `base_duyuruimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_duyurutext`
--

DROP TABLE IF EXISTS `base_duyurutext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_duyurutext` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext,
  `created` datetime(6) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `topic_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_duyurutext_topic_id_8822409b_fk_base_duyuru_id` (`topic_id`),
  CONSTRAINT `base_duyurutext_topic_id_8822409b_fk_base_duyuru_id` FOREIGN KEY (`topic_id`) REFERENCES `base_duyuru` (`id`),
  CONSTRAINT `base_duyurutext_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_duyurutext`
--

LOCK TABLES `base_duyurutext` WRITE;
/*!40000 ALTER TABLE `base_duyurutext` DISABLE KEYS */;
INSERT INTO `base_duyurutext` VALUES (1,'Lorem ipsum odor amet, consectetuer adipiscing elit. Vulputate conubia dolor ultricies litora adipiscing platea. Eget enim per adipiscing netus finibus, rhoncus cras. Elit neque nibh facilisis pulvinar potenti ultricies tempus. Fermentum quisque facilisi felis vulputate venenatis. Habitasse consequat quam morbi cras ullamcorper lacinia. Pharetra semper ex integer ornare dignissim. Nisi fringilla pretium habitant tempor arcu. Purus turpis mus himenaeos metus mattis magnis vel dictum primis.\r\n\r\nSed pretium sollicitudin mus eleifend ex cursus. Ridiculus pellentesque vestibulum pulvinar consequat ad ultricies dignissim consectetur. Aliquet tristique tincidunt vivamus lectus molestie varius. Risus ut velit; efficitur elementum duis montes justo suscipit consectetur. Natoque leo potenti quisque, penatibus dolor eleifend a. Blandit scelerisque non aenean maximus per vestibulum ipsum. Diam senectus commodo congue bibendum per pulvinar posuere auctor iaculis.\r\n\r\nLectus pellentesque vel scelerisque lacus consectetur netus. Lacus hendrerit vel dis sem fringilla per amet curae nec. Eu sagittis tellus in enim; magnis viverra. Nisi aptent augue erat nisi euismod augue. Ac euismod eget elementum, taciti non torquent. Elementum aptent nullam curae cras dapibus. Habitasse maximus posuere fusce gravida ultricies rhoncus fermentum. Dolor faucibus magna enim, sit aliquet tincidunt. Nisi sodales tempus primis ultrices conubia purus aliquet ligula.','2024-12-09 02:45:02.894950',0,1),(2,'Lorem ipsum odor amet, consectetuer adipiscing elit. Lobortis nisl augue lorem mi rhoncus molestie. Tempus magnis nascetur tristique torquent per at per. Purus erat purus risus pretium vitae diam. Odio dictum justo euismod hac vestibulum non venenatis. Lectus lobortis libero porta auctor; taciti imperdiet ridiculus. Lacus duis ultricies id elementum cursus potenti maximus potenti ligula. Phasellus praesent facilisi eros at malesuada montes diam magnis porttitor. Porta condimentum lacinia nec eget eleifend libero suscipit.','2024-12-09 02:45:15.802196',0,2),(3,'Lorem ipsum odor amet, consectetuer adipiscing elit. Ridiculus porttitor augue maecenas erat morbi. Nulla varius metus aliquet libero ad feugiat. Id magnis convallis a ante sollicitudin rhoncus. Aptent pretium hendrerit massa est arcu inceptos diam rhoncus. Amet senectus quis ex, egestas magnis pulvinar parturient sociosqu! Ultrices gravida euismod pharetra in nisi consectetur. Vel eros lobortis nec vel interdum pulvinar tempor adipiscing.\r\n\r\nPotenti netus convallis; morbi facilisis elit arcu vivamus vel. Ridiculus fusce orci arcu morbi hac commodo dapibus nisi. Primis tellus ad libero platea facilisis ultrices est nisl. Parturient ultrices mus ornare inceptos sit himenaeos lacinia consectetur. In nisi cursus tristique curabitur tristique. Auctor neque consectetur scelerisque hac risus. Posuere cubilia scelerisque erat morbi at penatibus torquent. Enim platea montes tempor lectus; vehicula aliquam. Sollicitudin turpis eros felis tortor sollicitudin tortor ligula.','2024-12-11 20:46:56.895345',1,3),(4,'Lorem ipsum odor amet, consectetuer adipiscing elit. Laoreet torquent montes parturient lectus morbi aliquet praesent. Lobortis eu aliquet non suspendisse pellentesque vulputate. Aproin magnis et curabitur cras sagittis cursus mi fusce. Dui hac parturient nisi curae conubia feugiat non. Ligula lectus leo eros diam ex ipsum porta. Dui pharetra ex placerat litora non cras amet convallis eleifend.\r\n\r\nAliquet libero sociosqu blandit amet; himenaeos fringilla. Sociosqu cras consectetur curae elementum porttitor nunc natoque. Vitae fringilla vehicula sem, orci mus class. Tellus imperdiet natoque rhoncus semper, commodo dignissim mattis curabitur. Sit risus cubilia senectus vel praesent lacinia. Volutpat tempor cursus penatibus himenaeos taciti magnis. Mattis vestibulum vulputate vitae suspendisse cubilia etiam. Mattis penatibus euismod parturient sed pretium praesent. Arcu cursus facilisi sed elementum massa porta inceptos. Hendrerit faucibus elit lectus molestie; scelerisque felis proin.','2024-12-11 20:46:56.896129',3,3),(5,'sdşaglkmsdlgkmalsdkgmasldögm sdşklsmnrjkvlmösv akdv kldjfsnjdnjvknsKDJVNSKJVNDHJSHFGWIOURHJGFDSGHIUERANKDJVAIUERNVKJDSANVIRAUENVKJDFNOVISUFBNVAJDNFBIUAEDNBVKJDFNBIFSDNBJFANDBJKNDSF\r\n\r\n\r\nSDŞLFBNSKJDLFNBJKDFNBDKSJNBIOSEJBNFUIPSENOB','2024-12-16 18:05:02.464193',0,4);
/*!40000 ALTER TABLE `base_duyurutext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_konferans`
--

DROP TABLE IF EXISTS `base_konferans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_konferans` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `baslik` varchar(100) NOT NULL,
  `text` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_konferans`
--

LOCK TABLES `base_konferans` WRITE;
/*!40000 ALTER TABLE `base_konferans` DISABLE KEYS */;
INSERT INTO `base_konferans` VALUES (1,'Başlık1','konferans text1','2024-12-16 18:22:51.820135','2024-12-16 18:22:51.820192','baslk1');
/*!40000 ALTER TABLE `base_konferans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_konferansimage`
--

DROP TABLE IF EXISTS `base_konferansimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_konferansimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `baslik_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_konferansimage_baslik_id_b1af6c51_fk_base_konferans_id` (`baslik_id`),
  CONSTRAINT `base_konferansimage_baslik_id_b1af6c51_fk_base_konferans_id` FOREIGN KEY (`baslik_id`) REFERENCES `base_konferans` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_konferansimage`
--

LOCK TABLES `base_konferansimage` WRITE;
/*!40000 ALTER TABLE `base_konferansimage` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_konferansimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_makale`
--

DROP TABLE IF EXISTS `base_makale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_makale` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Oz` longtext NOT NULL,
  `bolum` varchar(100) NOT NULL,
  `birinci_dil` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `pdf` varchar(100) DEFAULT NULL,
  `slug` varchar(50) NOT NULL,
  `sayi_id` bigint NOT NULL,
  `baslik` varchar(100) NOT NULL,
  `tur` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `base_makale_sayi_id_236cbcc3_fk_base_sayi_id` (`sayi_id`),
  CONSTRAINT `base_makale_sayi_id_236cbcc3_fk_base_sayi_id` FOREIGN KEY (`sayi_id`) REFERENCES `base_sayi` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_makale`
--

LOCK TABLES `base_makale` WRITE;
/*!40000 ALTER TABLE `base_makale` DISABLE KEYS */;
INSERT INTO `base_makale` VALUES (2,'ne bilim 2','2. bölüm','ingilizce','2024-12-06 02:43:22.515870','2024-12-08 23:11:16.780671','pdfs/Zorunluluk_Formu_temp_8PR7yj9.doc','konusdfkajslsf',2,'baslik','tür'),(3,'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum penatibus montes fringilla ultricies nullam proin augue. Libero parturient accumsan iaculis mattis penatibus ac scelerisque. Dis et et metus porta efficitur aliquet magna viverra. Platea suspendisse facilisi condimentum pulvinar urna fames risus. Laoreet potenti ridiculus aliquam ligula varius phasellus posuere volutpat. Duis erat bibendum urna maximus feugiat augue; lorem luctus est.\r\n\r\nAnte cras lobortis dignissim, vitae odio cras erat. Habitant id fringilla maximus aptent in efficitur conubia egestas magna. Maximus porta interdum sit turpis litora congue leo nam vivamus. Fusce etiam dignissim congue nulla congue duis netus. Faucibus himenaeos feugiat fermentum elementum molestie adipiscing pretium. Leo conubia facilisi placerat ullamcorper natoque taciti potenti tempus. Porta platea nostra sem penatibus sem torquent augue aliquet ipsum. Ornare suscipit vel nec, fames himenaeos curabitur. Fusce aliquam enim accumsan feugiat condimentum duis. Maecenas bibendum turpis maecenas blandit convallis.\r\n\r\nLaoreet laoreet habitant leo nam pellentesque laoreet condimentum dis senectus. Adipiscing diam pharetra lectus convallis euismod enim. Ac faucibus gravida imperdiet proin ultrices aliquet hac. Orci facilisis lobortis inceptos scelerisque eget hendrerit lobortis morbi quam. Habitasse curabitur habitasse tincidunt faucibus platea mi, nullam eros facilisi. Sodales duis nostra euismod consectetur luctus lobortis. Ligula semper bibendum mattis hac facilisis risus integer dolor fringilla. Aliquam mollis mus ipsum ex nulla. Urna facilisi maecenas pharetra tortor viverra aliquet etiam lacinia.','1. bölüm','türkçe','2024-12-06 02:43:49.834946','2024-12-11 00:19:26.541222','pdfs/682900761-barkodlu-belge.pdf','konufasfasf',2,'Çatara Patara','tür'),(4,'Öz2','bölüm2','birinci dil2','2024-12-08 01:14:56.041616','2024-12-08 01:14:56.041662','','konu2',3,'baslik','tür'),(5,'Öz 3','bölüm 3','türkçe','2024-12-08 22:36:53.559370','2024-12-08 22:36:53.559417','','makale-3',4,'baslik','tür'),(6,'Özsdlgkfmsdalkgşnsdlgkndaslkgnsdlgkadsg','bölüm 4','türkçe','2024-12-11 20:45:36.035238','2024-12-11 20:45:36.035270','','vaslk-4',5,'vaşlık 4','tür'),(7,'Özsdf','bölüm','birinci dil','2024-12-12 19:36:13.449766','2024-12-12 19:36:13.449777','','basliksdf',6,'basliksdf','tür'),(8,'Özasfasf','bölümasfasf','birinci dilasf','2024-12-12 19:37:12.809781','2024-12-12 19:37:12.809805','pdfs/682900761-barkodlu-belge_1pQDGTc.pdf','basasdassojfslaksf',4,'basasdaşsojfşlaksf','tür'),(9,'ÖÖÖÖöÖÖÖÖ','ÇÇÇÇÇÇÇ','birinci di','2024-12-16 23:42:56.710597','2024-12-16 23:42:56.710635','','ssssssss',6,'ŞŞŞşşŞŞŞ','tür'),(11,'Öz','bölüm','birinci dil','2024-12-16 23:46:22.425000','2024-12-16 23:46:22.425066','','ooooooiiiccccuuuuu',6,'ÖÖÖÖÖÖİİİÇÇÇÇÜÜÜÜÜ','tür');
/*!40000 ALTER TABLE `base_makale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_makaleanahtar`
--

DROP TABLE IF EXISTS `base_makaleanahtar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_makaleanahtar` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anahtar` varchar(50) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `baslik_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_makaleanahtar_baslik_id_9dfa08b5_fk_base_makale_id` (`baslik_id`),
  CONSTRAINT `base_makaleanahtar_baslik_id_9dfa08b5_fk_base_makale_id` FOREIGN KEY (`baslik_id`) REFERENCES `base_makale` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_makaleanahtar`
--

LOCK TABLES `base_makaleanahtar` WRITE;
/*!40000 ALTER TABLE `base_makaleanahtar` DISABLE KEYS */;
INSERT INTO `base_makaleanahtar` VALUES (1,'anahtar deneme2','2024-12-08 01:18:34.883960','2024-12-08 01:18:34.883970',4),(2,'anahtar 3','2024-12-08 22:36:53.561855','2024-12-08 22:36:53.561888',5),(3,'anahtar 2','2024-12-09 00:58:55.639954','2024-12-09 00:58:55.639967',2),(6,'anahtarlar','2024-12-11 00:22:11.918569','2024-12-11 00:22:11.918588',3),(7,'koltuğun','2024-12-11 00:22:11.919794','2024-12-11 00:22:11.919811',3),(8,'altında','2024-12-11 00:22:11.920258','2024-12-11 00:22:11.920273',3),(9,'kalık','2024-12-11 00:22:11.920652','2024-12-11 00:22:11.920665',3),(10,'beni','2024-12-11 00:22:11.921045','2024-12-11 00:22:11.921058',3),(11,'ara','2024-12-11 00:22:11.921472','2024-12-11 00:22:11.921490',3),(12,'anahtar4','2024-12-11 20:45:36.039370','2024-12-11 20:45:36.039400',6),(13,'anahtar31','2024-12-11 20:45:36.040210','2024-12-11 20:45:36.040261',6),(14,'sşldkjglskdjgkalgjlkssadgja','2024-12-11 21:54:50.308971','2024-12-11 21:54:50.308999',3),(15,'sdlkfmlaksjflşkajsdfklasdlf','2024-12-11 21:54:59.595153','2024-12-11 21:54:59.595172',3);
/*!40000 ALTER TABLE `base_makaleanahtar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_makalekaynak`
--

DROP TABLE IF EXISTS `base_makalekaynak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_makalekaynak` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `kaynak` varchar(50) DEFAULT NULL,
  `baslik_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_makalekaynak_baslik_id_8a2f20c9_fk_base_makale_id` (`baslik_id`),
  CONSTRAINT `base_makalekaynak_baslik_id_8a2f20c9_fk_base_makale_id` FOREIGN KEY (`baslik_id`) REFERENCES `base_makale` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_makalekaynak`
--

LOCK TABLES `base_makalekaynak` WRITE;
/*!40000 ALTER TABLE `base_makalekaynak` DISABLE KEYS */;
INSERT INTO `base_makalekaynak` VALUES (1,'2024-12-08 01:13:30.991692','2024-12-09 02:32:49.243663','www.wikipedia.com',3),(2,'2024-12-08 01:18:34.883387','2024-12-08 01:18:34.883402','kaynak deneme2',4),(3,'2024-12-08 22:36:53.560454','2024-12-08 22:36:53.560484','kaynak 3',5),(4,'2024-12-09 00:58:55.637716','2024-12-09 00:58:55.637739','kaynak 2',2),(5,'2024-12-11 00:00:57.020911','2024-12-11 00:00:57.020954','www.bombabomba.com',3),(6,'2024-12-11 00:00:57.022793','2024-12-11 00:00:57.022824','türksigara.net',3),(7,'2024-12-11 20:45:36.037288','2024-12-11 20:45:36.037328','dslfkjdslkgfalskdgj',6),(8,'2024-12-11 20:45:36.038647','2024-12-11 20:45:36.038676','kaynak2',6);
/*!40000 ALTER TABLE `base_makalekaynak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_makaletext`
--

DROP TABLE IF EXISTS `base_makaletext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_makaletext` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `text` longtext NOT NULL,
  `ordering` int unsigned NOT NULL,
  `konu_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_makaletext_konu_id_90c97cf9_fk_base_makale_id` (`konu_id`),
  CONSTRAINT `base_makaletext_konu_id_90c97cf9_fk_base_makale_id` FOREIGN KEY (`konu_id`) REFERENCES `base_makale` (`id`),
  CONSTRAINT `base_makaletext_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_makaletext`
--

LOCK TABLES `base_makaletext` WRITE;
/*!40000 ALTER TABLE `base_makaletext` DISABLE KEYS */;
INSERT INTO `base_makaletext` VALUES (1,'2024-12-08 01:18:34.881198','2024-12-08 01:18:34.881212','text deneme 2',0,4);
/*!40000 ALTER TABLE `base_makaletext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_makaleyazar`
--

DROP TABLE IF EXISTS `base_makaleyazar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_makaleyazar` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `yazar` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `baslik_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_makaleyazar_baslik_id_6728d0c2_fk_base_makale_id` (`baslik_id`),
  CONSTRAINT `base_makaleyazar_baslik_id_6728d0c2_fk_base_makale_id` FOREIGN KEY (`baslik_id`) REFERENCES `base_makale` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_makaleyazar`
--

LOCK TABLES `base_makaleyazar` WRITE;
/*!40000 ALTER TABLE `base_makaleyazar` DISABLE KEYS */;
INSERT INTO `base_makaleyazar` VALUES (1,'yazar deneme2','2024-12-08 01:18:34.884824','2024-12-08 01:18:34.884832',4),(2,'yazar 3','2024-12-08 22:36:53.563630','2024-12-08 22:36:53.563672',5),(3,'fikibamba','2024-12-08 22:55:35.431481','2024-12-09 02:32:49.247717',3),(5,'hikolitonyum','2024-12-11 00:00:57.024245','2024-12-11 00:00:57.024271',3),(6,'furkan varol','2024-12-11 20:45:36.041006','2024-12-11 20:45:36.041032',6),(8,'yazar2','2024-12-11 22:19:00.979665','2024-12-11 22:19:00.979688',2);
/*!40000 ALTER TABLE `base_makaleyazar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_metodoloji`
--

DROP TABLE IF EXISTS `base_metodoloji`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_metodoloji` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `baslik` varchar(100) NOT NULL,
  `text` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_metodoloji`
--

LOCK TABLES `base_metodoloji` WRITE;
/*!40000 ALTER TABLE `base_metodoloji` DISABLE KEYS */;
INSERT INTO `base_metodoloji` VALUES (1,'Metodoloji başlık1','metodoloji text1','2024-12-16 18:23:04.863765','2024-12-16 18:23:04.863842','metodoloji-baslk1');
/*!40000 ALTER TABLE `base_metodoloji` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_metodolojiimage`
--

DROP TABLE IF EXISTS `base_metodolojiimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_metodolojiimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `baslik_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_metodolojiimage_baslik_id_9e69b34e_fk_base_metodoloji_id` (`baslik_id`),
  CONSTRAINT `base_metodolojiimage_baslik_id_9e69b34e_fk_base_metodoloji_id` FOREIGN KEY (`baslik_id`) REFERENCES `base_metodoloji` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_metodolojiimage`
--

LOCK TABLES `base_metodolojiimage` WRITE;
/*!40000 ALTER TABLE `base_metodolojiimage` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_metodolojiimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_portre`
--

DROP TABLE IF EXISTS `base_portre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_portre` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `baslik` varchar(100) NOT NULL,
  `roportaj` longtext NOT NULL,
  `link` varchar(200) NOT NULL,
  `video` varchar(200) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `oz_gecmis_img` varchar(100) DEFAULT NULL,
  `oz_gecmis` longtext NOT NULL DEFAULT (_utf8mb3'öz geçmiş'),
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_portre`
--

LOCK TABLES `base_portre` WRITE;
/*!40000 ALTER TABLE `base_portre` DISABLE KEYS */;
INSERT INTO `base_portre` VALUES (1,'Başlık1','röportaj1','https://open.spotify.com/show/2HE4WPETsojDxh9GRFIiZP?si=8cf043f5e13d41bb',NULL,'2024-12-13 05:21:48.697558','2024-12-13 05:22:16.957592','IMG_0504.JPG','öz geçmiş 1','slug'),(2,'Başlıkasdasd','Lorem ipsum odor amet, consectetuer adipiscing elit. Ac aenean hac non tortor nec mattis augue imperdiet. Sollicitudin donec scelerisque congue vel natoque rutrum. Sed proin id suspendisse nisi potenti; vel tempus duis tortor. Volutpat ligula vestibulum accumsan himenaeos gravida sagittis luctus. Iaculis justo pellentesque torquent sociosqu, morbi ornare maecenas mi. Nulla himenaeos est tristique mattis sit risus, tristique et. Nisi dictum in suspendisse fermentum blandit velit interdum gravida.\r\n\r\nSapien arcu faucibus finibus semper at sit ex primis condimentum. Mus luctus id nascetur pretium, imperdiet varius nulla cras. Nascetur quisque sem magnis imperdiet venenatis ut. Dictum enim consequat tempus potenti urna porta gravida sem. Nam vel justo curae consectetur dictumst platea. Integer risus laoreet orci, magnis tellus phasellus ipsum curae. Nibh rhoncus cubilia himenaeos ante platea.\r\n\r\nAmus fusce blandit scelerisque pharetra etiam ut. Porta nibh adipiscing taciti vestibulum vehicula cursus etiam. Lacinia viverra rhoncus purus lobortis; fermentum semper suspendisse malesuada penatibus. In nascetur massa arcu mus, ligula fermentum potenti dolor. Cubilia quis gravida rutrum mattis vulputate mi porttitor platea. Tempus egestas egestas porttitor tristique fringilla. Fames facilisis iaculis nisi et habitant curae. Cras pharetra neque non volutpat phasellus urna amet velit praesent. Venenatis lacinia pellentesque; fringilla turpis pretium amet.','https://open.spotify.com/show/2HE4WPETsojDxh9GRFIiZP?si=8cf043f5e13d41bb','https://www.youtube.com/watch?v=EROritwpwEk','2024-12-16 23:48:46.472767','2024-12-17 23:08:33.160408','IMG_1213.JPG','Lorem ipsum odor amet, consectetuer adipiscing elit. Morbi risus fusce laoreet commodo fames. Consequat semper suspendisse nascetur placerat parturient netus, ipsum vivamus sapien. Purus nulla facilisi nibh nisl ipsum proin. Suscipit ex litora porttitor ut ridiculus. Turpis scelerisque magna molestie mi proin egestas. Euismod diam est ultrices a feugiat tellus fames cras. Luctus gravida mus ridiculus diam egestas molestie.\r\n\r\nSapien orci nascetur pellentesque; facilisi scelerisque pulvinar. Vehicula nunc velit eros integer dis; mi finibus. Efficitur parturient donec ullamcorper eget facilisi eget. Convallis volutpat ridiculus in etiam lectus arcu lacus. Egestas fames potenti egestas non conubia. Curabitur aliquet ullamcorper eget fringilla etiam a at tristique. Et eget varius lacinia ultrices lacinia viverra sed quis. Eget sed in lectus, lectus sociosqu aliquet.\r\n\r\nNisi inceptos praesent justo proin consequat elit ac. Facilisi maecenas tellus nec pulvinar vivamus integer eget. Malesuada erat facilisis nisi nisl quisque suscipit porttitor. Cursus vivamus maximus accumsan tempus metus neque magnis id. Sit senectus praesent etiam velit pretium lobortis neque orci. Leo elit fames pulvinar ante vel eleifend suscipit. Lectus litora parturient ultricies porttitor; cursus sodales rutrum. Aenean tincidunt scelerisque lacinia placerat cubilia ullamcorper. Consectetur torquent porta finibus natoque risus augue.\r\n\r\nNatoque bibendum odio congue fames ultrices sociosqu. Taciti lacus turpis nostra urna mauris primis placerat. Id accumsan dui vestibulum torquent felis eu. Urna lobortis efficitur condimentum fusce taciti integer eget volutpat. Urna class adipiscing platea facilisis urna primis, ultricies mollis litora. In venenatis tristique iaculis; dignissim congue nullam urna. Nascetur a cursus pretium rhoncus morbi luctus tincidunt. Facilisis porttitor magnis morbi fusce hac sed feugiat finibus. Mus imperdiet pharetra cursus, volutpat eget molestie.\r\n\r\nTristique urna cras vel leo; feugiat ac. Libero potenti auctor class vel nisi nec gravida. Rutrum bibendum nam ipsum luctus eu dignissim. Congue luctus ac dignissim nulla nibh quis. Vehicula efficitur lorem dignissim rhoncus consequat. Justo egestas imperdiet turpis; fusce justo litora torquent. Orci inceptos ex; tortor sodales placerat euismod sagittis vel! Torquent dis dis at adipiscing torquent. Tincidunt placerat dictum, posuere tellus interdum purus. Cubilia vel mattis porttitor aptent morbi dis senectus tempor tincidunt.','baslkasdasd');
/*!40000 ALTER TABLE `base_portre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_sava`
--

DROP TABLE IF EXISTS `base_sava`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_sava` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `baslik` varchar(100) NOT NULL,
  `text` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_sava`
--

LOCK TABLES `base_sava` WRITE;
/*!40000 ALTER TABLE `base_sava` DISABLE KEYS */;
INSERT INTO `base_sava` VALUES (1,'SAVA başlık1','SAVA text1','2024-12-16 18:22:38.965935','2024-12-16 18:22:38.965996','sava-baslk1'),(2,'SAVA başlık2','SAVA text2','2024-12-16 23:53:10.122900','2024-12-16 23:57:46.997581','sava-baslk2');
/*!40000 ALTER TABLE `base_sava` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_savaimage`
--

DROP TABLE IF EXISTS `base_savaimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_savaimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `baslik_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_savaimage_baslik_id_4e6626eb_fk_base_sava_id` (`baslik_id`),
  CONSTRAINT `base_savaimage_baslik_id_4e6626eb_fk_base_sava_id` FOREIGN KEY (`baslik_id`) REFERENCES `base_sava` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_savaimage`
--

LOCK TABLES `base_savaimage` WRITE;
/*!40000 ALTER TABLE `base_savaimage` DISABLE KEYS */;
INSERT INTO `base_savaimage` VALUES (3,'images/7550a2c5-90c7-489a-95a6-7794fd01876c_oKAyPgJ.jpg','2024-12-16 23:57:47.000220','2024-12-16 23:57:47.000230',2),(4,'images/1714413551733_6SpKbZT.jpeg','2024-12-16 23:57:47.001973','2024-12-16 23:57:47.001980',2),(5,'images/efa72e67-8e7d-4123-9865-295948346a37_mI9ZKr6.jpg','2024-12-16 23:57:47.002919','2024-12-16 23:57:47.002930',2);
/*!40000 ALTER TABLE `base_savaimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_sayi`
--

DROP TABLE IF EXISTS `base_sayi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_sayi` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sayi` int NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sayi` (`sayi`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_sayi`
--

LOCK TABLES `base_sayi` WRITE;
/*!40000 ALTER TABLE `base_sayi` DISABLE KEYS */;
INSERT INTO `base_sayi` VALUES (2,1,'2024-12-06 02:43:22.511861','2024-12-11 22:19:00.977019','1'),(3,2,'2024-12-08 01:14:56.037620','2024-12-08 01:18:34.879343','2'),(4,3,'2024-12-08 22:36:53.551264','2024-12-08 22:36:53.551308','3'),(5,4,'2024-12-11 20:45:36.021536','2024-12-11 20:46:01.828669','4'),(6,5,'2024-12-12 19:34:59.230378','2024-12-12 19:36:28.676513','5');
/*!40000 ALTER TABLE `base_sayi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-12-06 01:38:25.218173','1','sayi: 1',1,'[{\"added\": {}}]',11,1),(2,'2024-12-06 02:38:41.130137','1','sayi: 1',2,'[]',11,1),(3,'2024-12-06 02:40:06.757418','1','sayi: 1',2,'[{\"added\": {\"name\": \"makale\", \"object\": \"makale: konu2\"}}]',11,1),(4,'2024-12-06 02:43:13.275626','1','sayi: 1',3,'',11,1),(5,'2024-12-06 02:43:22.516569','2','sayi: 1',1,'[{\"added\": {}}, {\"added\": {\"name\": \"makale\", \"object\": \"makale: konusdfkajsl\\u015ff\"}}]',11,1),(6,'2024-12-06 02:43:49.835772','2','sayi: 1',2,'[{\"added\": {\"name\": \"makale\", \"object\": \"makale: konufasfasf\"}}]',11,1),(7,'2024-12-06 02:44:01.041996','2','sayi: 1',2,'[]',11,1),(8,'2024-12-08 01:02:06.561269','2','sayi: 1',2,'[]',11,1),(9,'2024-12-08 01:04:48.150694','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale: annen\", \"fields\": [\"Konu\", \"Oz\", \"Bolum\", \"Birinci dil\"]}}, {\"changed\": {\"name\": \"makale\", \"object\": \"makale: baban\", \"fields\": [\"Konu\", \"Oz\", \"Bolum\", \"Birinci dil\"]}}]',11,1),(10,'2024-12-08 01:13:31.000558','1','kaynak :kaynak deneme',1,'[{\"added\": {}}]',16,1),(11,'2024-12-08 01:14:56.043183','3','sayi: 2',1,'[{\"added\": {}}, {\"added\": {\"name\": \"makale\", \"object\": \"makale: konu2\"}}]',11,1),(12,'2024-12-08 01:17:18.226808','3','sayi: 2',2,'[]',11,1),(13,'2024-12-08 01:18:34.886428','3','sayi: 2',2,'[]',11,1),(14,'2024-12-08 13:43:54.778319','1','cart curt',1,'[{\"added\": {}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_2244_iyMB5d3.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_3762_Iqn87Dh.JPG\"}}]',7,1),(15,'2024-12-08 22:36:53.565017','4','sayi: 3',1,'[{\"added\": {}}, {\"added\": {\"name\": \"makale\", \"object\": \"makale: makale 3\"}}]',11,1),(16,'2024-12-08 22:45:57.883722','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: ba\\u015fl\\u0131k\", \"fields\": [\"Baslik\"]}}]',11,1),(17,'2024-12-08 22:55:35.435383','2','sayi: 1',2,'[]',11,1),(18,'2024-12-08 22:58:43.397870','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: ba\\u015fl\\u0131k\", \"fields\": [\"Pdf\"]}}]',11,1),(19,'2024-12-08 23:11:16.787281','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: baslik\", \"fields\": [\"Pdf\"]}}]',11,1),(20,'2024-12-09 00:58:55.641586','2','sayi: 1',2,'[]',11,1),(21,'2024-12-09 02:32:49.251182','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: \\u00c7atara Patara\", \"fields\": [\"Baslik\", \"Oz\"]}}]',11,1),(22,'2024-12-09 02:45:02.902584','1','annen',1,'[{\"added\": {}}, {\"added\": {\"name\": \"duyuru text\", \"object\": \"annen text\"}}]',8,1),(23,'2024-12-09 02:45:15.802945','2','baban',1,'[{\"added\": {}}, {\"added\": {\"name\": \"duyuru text\", \"object\": \"baban text\"}}]',8,1),(24,'2024-12-11 00:00:57.025520','2','sayi: 1',2,'[]',11,1),(25,'2024-12-11 00:19:16.275387','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: \\u00c7atara Patara\", \"fields\": [\"Pdf\"]}}]',11,1),(26,'2024-12-11 00:19:26.544395','2','sayi: 1',2,'[{\"changed\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: \\u00c7atara Patara\", \"fields\": [\"Pdf\"]}}]',11,1),(27,'2024-12-11 00:21:42.879399','2','sayi: 1',2,'[]',11,1),(28,'2024-12-11 00:22:11.922174','2','sayi: 1',2,'[]',11,1),(29,'2024-12-11 20:45:36.043290','5','sayi: 4',1,'[{\"added\": {}}, {\"added\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: va\\u015fl\\u0131k 4\"}}]',11,1),(30,'2024-12-11 20:46:01.833646','5','sayi: 4',2,'[]',11,1),(31,'2024-12-11 20:46:56.897360','3','duyuru 3',1,'[{\"added\": {}}, {\"added\": {\"name\": \"duyuru text\", \"object\": \"duyuru 3 text\"}}, {\"added\": {\"name\": \"duyuru text\", \"object\": \"duyuru 3 text\"}}, {\"added\": {\"name\": \"duyuru image\", \"object\": \"duyuru 3 image\"}}]',8,1),(32,'2024-12-11 20:47:22.273928','3','duyuru 3',2,'[]',8,1),(33,'2024-12-11 20:47:47.487630','3','duyuru 3',2,'[{\"changed\": {\"name\": \"duyuru image\", \"object\": \"duyuru 3 image\", \"fields\": [\"Image\"]}}]',8,1),(34,'2024-12-11 21:54:50.311779','2','sayi: 1',2,'[]',11,1),(35,'2024-12-11 21:54:59.596005','2','sayi: 1',2,'[]',11,1),(36,'2024-12-11 22:18:55.138692','2','sayi: 1',2,'[]',11,1),(37,'2024-12-11 22:19:00.980499','2','sayi: 1',2,'[]',11,1),(38,'2024-12-12 19:34:59.240806','6','sayi: 5',1,'[{\"added\": {}}]',11,1),(39,'2024-12-12 19:36:13.451102','6','sayi: 5',2,'[{\"added\": {\"name\": \"makale\", \"object\": \"makale ba\\u015fl\\u0131\\u011f\\u0131: basliksdf\"}}]',11,1),(40,'2024-12-12 19:36:28.678591','6','sayi: 5',2,'[]',11,1),(41,'2024-12-12 19:37:12.813689','8','makale başlığı: basasdaşsojfşlaksf',1,'[{\"added\": {}}]',10,1),(42,'2024-12-12 19:44:11.228757','1','cart curt',2,'[{\"added\": {\"name\": \"image\", \"object\": \"images/IMG_0349_XeyoPK5.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_2064_dUe0vg8.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_0504_sM8uxOX.JPG\"}}]',7,1),(43,'2024-12-13 01:38:37.440630','3','duyuru 3',2,'[{\"changed\": {\"name\": \"duyuru text\", \"object\": \"duyuru 3 text\", \"fields\": [\"Text\"]}}, {\"changed\": {\"name\": \"duyuru text\", \"object\": \"duyuru 3 text\", \"fields\": [\"Text\"]}}]',8,1),(44,'2024-12-13 01:54:30.162826','2','kart kurt',1,'[{\"added\": {}}, {\"added\": {\"name\": \"image\", \"object\": \"images/efa72e67-8e7d-4123-9865-295948346a37_c2Fr0b4.jpg\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/FkHCUPsX0AEb8_d.jpeg\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_0349_qwfeuq9.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_2781_iK4Zpro.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_6604_PqgIPvR.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_5863.JPG\"}}]',7,1),(45,'2024-12-13 03:12:17.493096','3','part purt',1,'[{\"added\": {}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_4564.JPG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_3591.PNG\"}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_9985_Qwnj155.JPG\"}}]',7,1),(46,'2024-12-13 03:20:44.303727','4','lap lup',1,'[{\"added\": {}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_3598.JPG\"}}]',7,1),(47,'2024-12-13 03:25:19.691743','5','çatara patara',1,'[{\"added\": {}}, {\"added\": {\"name\": \"image\", \"object\": \"images/IMG_3596.JPG\"}}]',7,1),(48,'2024-12-13 05:21:48.705874','1','Başlık1',1,'[{\"added\": {}}]',19,1),(49,'2024-12-13 05:22:16.960557','1','Başlık1',2,'[{\"changed\": {\"fields\": [\"Oz gecmis img\"]}}]',19,1),(50,'2024-12-16 18:05:02.468826','4','duyuru 4',1,'[{\"added\": {}}, {\"added\": {\"name\": \"duyuru text\", \"object\": \"duyuru 4 text\"}}, {\"added\": {\"name\": \"duyuru image\", \"object\": \"duyuru 4 image\"}}]',8,1),(51,'2024-12-16 18:22:38.975045','1','SAVA: SAVA başlık1',1,'[{\"added\": {}}]',22,1),(52,'2024-12-16 18:22:51.822060','1','Konferans: Başlık1',1,'[{\"added\": {}}]',20,1),(53,'2024-12-16 18:23:04.865377','1','Metodoloji: Metodoloji başlık1',1,'[{\"added\": {}}]',21,1),(54,'2024-12-16 23:42:56.712856','9','makale başlığı: ŞŞŞşşŞŞŞ',1,'[{\"added\": {}}]',10,1),(55,'2024-12-16 23:45:00.688461','10','makale başlığı: ŞŞŞŞÖÖÖÖÜÜÜÜİİİİİÇÇÇÇ',1,'[{\"added\": {}}]',10,1),(56,'2024-12-16 23:46:08.106457','10','makale başlığı: lkasfjalskfjalksf',2,'[{\"changed\": {\"fields\": [\"Baslik\"]}}]',10,1),(57,'2024-12-16 23:46:22.426319','11','makale başlığı: ÖÖÖÖÖÖİİİÇÇÇÇÜÜÜÜÜ',1,'[{\"added\": {}}]',10,1),(58,'2024-12-16 23:46:26.782196','10','makale başlığı: lkasfjalskfjalksf',3,'',10,1),(59,'2024-12-16 23:48:46.474255','2','Başlıkasdasd',1,'[{\"added\": {}}]',19,1),(60,'2024-12-16 23:53:10.135685','2','SAVA: SAVA başlık2',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}, {\"added\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}]',22,1),(61,'2024-12-16 23:54:51.587841','2','SAVA: SAVA başlık2',2,'[]',22,1),(62,'2024-12-16 23:57:30.586328','2','SAVA: SAVA başlık2',2,'[{\"deleted\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}, {\"deleted\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}]',22,1),(63,'2024-12-16 23:57:47.003454','2','SAVA: SAVA başlık2',2,'[{\"added\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}, {\"added\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}, {\"added\": {\"name\": \"sava image\", \"object\": \"SAVA: SAVA ba\\u015fl\\u0131k2 image\"}}]',22,1),(64,'2024-12-17 22:15:39.403435','2','Başlıkasdasd',2,'[{\"changed\": {\"fields\": [\"Video\"]}}]',19,1),(65,'2024-12-17 22:32:24.684816','2','Başlıkasdasd',2,'[{\"changed\": {\"fields\": [\"Roportaj\", \"Oz gecmis\", \"Oz gecmis img\"]}}]',19,1),(66,'2024-12-17 23:08:33.170169','2','Başlıkasdasd',2,'[{\"changed\": {\"fields\": [\"Oz gecmis img\"]}}]',19,1),(67,'2024-12-30 12:02:45.200250','1','furkanvarol',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(26,'admin_honeypot','loginattempt'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'base','album'),(14,'base','albumimage'),(8,'base','duyuru'),(12,'base','duyuruimage'),(13,'base','duyurutext'),(9,'base','embeddedvideo'),(20,'base','konferans'),(23,'base','konferansimage'),(10,'base','makale'),(15,'base','makaleanahtar'),(16,'base','makalekaynak'),(17,'base','makaletext'),(18,'base','makaleyazar'),(21,'base','metodoloji'),(24,'base','metodolojiimage'),(19,'base','portre'),(22,'base','sava'),(25,'base','savaimage'),(11,'base','sayi'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-12-06 01:30:57.877845'),(2,'auth','0001_initial','2024-12-06 01:30:57.994462'),(3,'admin','0001_initial','2024-12-06 01:30:58.018569'),(4,'admin','0002_logentry_remove_auto_add','2024-12-06 01:30:58.022359'),(5,'admin','0003_logentry_add_action_flag_choices','2024-12-06 01:30:58.024628'),(6,'contenttypes','0002_remove_content_type_name','2024-12-06 01:30:58.044846'),(7,'auth','0002_alter_permission_name_max_length','2024-12-06 01:30:58.056348'),(8,'auth','0003_alter_user_email_max_length','2024-12-06 01:30:58.065997'),(9,'auth','0004_alter_user_username_opts','2024-12-06 01:30:58.068428'),(10,'auth','0005_alter_user_last_login_null','2024-12-06 01:30:58.078685'),(11,'auth','0006_require_contenttypes_0002','2024-12-06 01:30:58.079315'),(12,'auth','0007_alter_validators_add_error_messages','2024-12-06 01:30:58.081934'),(13,'auth','0008_alter_user_username_max_length','2024-12-06 01:30:58.098655'),(14,'auth','0009_alter_user_last_name_max_length','2024-12-06 01:30:58.111980'),(15,'auth','0010_alter_group_name_max_length','2024-12-06 01:30:58.117881'),(16,'auth','0011_update_proxy_permissions','2024-12-06 01:30:58.120452'),(17,'auth','0012_alter_user_first_name_max_length','2024-12-06 01:30:58.134352'),(18,'base','0001_initial','2024-12-06 01:30:58.248969'),(19,'sessions','0001_initial','2024-12-06 01:30:58.255143'),(20,'base','0002_alter_sayi_sayi','2024-12-06 01:33:30.600011'),(21,'base','0003_alter_album_slug_alter_duyuru_slug_alter_makale_slug_and_more','2024-12-06 01:38:18.108115'),(22,'base','0004_alter_sayi_sayi','2024-12-06 02:20:28.736973'),(23,'base','0002_rename_konu_makaleanahtar_baslik_and_more','2024-12-08 22:44:13.570535'),(24,'base','0003_alter_makaleanahtar_options','2024-12-11 00:22:37.367580'),(25,'base','0004_alter_makalekaynak_options_alter_makaleyazar_options','2024-12-11 00:23:08.607717'),(26,'base','0005_portre_delete_embeddedvideo','2024-12-13 05:07:23.296531'),(27,'base','0006_portre_image_portre_text_alter_portre_roportaj','2024-12-13 05:17:07.014001'),(28,'base','0007_rename_text_portre_oz_gecmis_and_more','2024-12-13 05:20:56.664331'),(29,'base','0008_alter_portre_video','2024-12-13 05:21:46.198300'),(30,'base','0009_konferans_metodoloji_sava_rename_image_albumimage_and_more','2024-12-13 05:58:21.076942'),(31,'base','0010_makale_tur','2024-12-16 23:42:20.483910'),(32,'admin_honeypot','0001_initial','2024-12-30 12:17:57.693188'),(33,'admin_honeypot','0002_auto_20160208_0854','2024-12-30 12:17:57.708205');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('64b6kbbjo4n3uswaict70lbxxh69ensg','.eJxVjDsOwjAQBe_iGlnZzfoTSvqcwbLXDg4gW4qTCnF3EikFtG9m3ls4v63ZbS0tbo7iKkBcfrfg-ZnKAeLDl3uVXMu6zEEeijxpk2ON6XU73b-D7Fvea53AIPZkDGiI1hrCCTpvQJFmEwijGqJHJqtUSF2YkAe9qwRMvUUUny-lJTZL:1tJNBz:SK726vNTxEYd2Chj4RNtccZMCIfQgwai4kf9pGizkFc','2024-12-20 01:31:39.305800'),('zmui5sw6mtd0mrdk6m8zg5hnwses9ojy','.eJxVjDsOwjAQBe_iGlnZzfoTSvqcwbLXDg4gW4qTCnF3EikFtG9m3ls4v63ZbS0tbo7iKkBcfrfg-ZnKAeLDl3uVXMu6zEEeijxpk2ON6XU73b-D7Fvea53AIPZkDGiI1hrCCTpvQJFmEwijGqJHJqtUSF2YkAe9qwRMvUUUny-lJTZL:1tSEPW:PHlo5t4-az8Nsj4HlKLZIA282qb5LTtBGFVf9XJy2M4','2025-01-13 11:58:14.283166');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-13  5:00:30
