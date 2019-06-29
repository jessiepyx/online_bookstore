-- MySQL dump 10.13  Distrib 5.7.13, for Linux (x86_64)
--
-- Host: localhost    Database: commodity
-- ------------------------------------------------------
-- Server version	5.7.13-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Database structure for DB `bookmarket`
--

drop database if exists bookmarket;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
create database bookmarket;
/*!40101 SET character_set_client = @saved_cs_client */;
use bookmarket;

--
-- Table structure for table user
--

drop table if exists user;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
create table user(
  id varchar(20) not null,
  pwd varchar(20) not null,
  email varchar(20) not null,
  name varchar(20) not null,
  telphone varchar(20) not null,
  primary key(id),
  unique key idname(id),
  unique key emailname(email),
  unique key tel(telphone)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table user
--

insert into user values('sellers','88889999','for@qq.com','陆小朋','18868113423');
/*!40000 ALTER TABLE user ENABLE KEYS */;
insert into user values('administrator','76214573','31@zju.edu.cn','方大同','18868108927');
/*!40000 ALTER TABLE user ENABLE KEYS */;

--
-- Table structure for table book
--

drop table if exists book;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
create table book(
  id varchar(20) not null,
  name varchar(20) not null,
  seil varchar(20) not null,
  beforeprice float,
  nowprice float not null,
  category int not null,
  storm int not null,
  introduction varchar(500),
  primary key(id),
  unique key idname(id),
  unique key bookname(name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table book
--

insert into book values(
  'AKTH2134','论语','陆小朋',24.9,20.9,2,3,
  '《论语》是孔子及其弟子的语录结集，由孔子弟子及再传弟子编写而成，至战国前期成书。全书共20篇492章，以语录体为主，叙事体为辅，主要记录孔子及其弟子的言行，较为集中地体现了孔子的政治主张、伦理思想、道德观念及教育原则等。此书是儒家学派的经典著作之一，与《大学》《中庸》《孟子》并称“四书”，再加上《诗经》《尚书》《礼记》《周易》《春秋》，总称“四书五经”。');
/*!40000 ALTER TABLE book ENABLE KEYS */;
insert into book values(
  'ATMN3672','巴黎圣母院','方大同',25.2,20.9,1,1,
  '《巴黎圣母院》以离奇和对比手法写了一个发生在15世纪法国的故事：巴黎圣母院副主教克罗德道貌岸然、蛇蝎心肠，先爱后恨，迫害吉ト赛女郎埃斯梅拉达。面目丑陋、心地善良的敲钟人卡西莫多为救女郎舍身。小说揭露了宗教的虚伪，宣告禁欲主义的破产，歌颂了下层劳动人民的善良、友爱、舍己为人，反映了雨果的人道主义思想。');
/*!40000 ALTER TABLE book ENABLE KEYS */;

--
-- Table structure for table online_order
--

drop table if exists online_order;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
create table online_order(
  id varchar(20) not null,
  bookname varchar(20) not null,
  seil varchar(20) not null,
  seiltel varchar(20) not null,
  buy varchar(20) not null,
  buytel varchar(20) not null,
  num int not null,
  price float not null,
  destination varchar(100) not null default '',
  state int not null default 0,
  primary key(id),
  unique key idname(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-29  9:21:32



