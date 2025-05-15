-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 13, 2024 at 01:02 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `1_social_media`
--
CREATE DATABASE IF NOT EXISTS `1_social_media` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `1_social_media`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add comment', 8, 'add_comment'),
(30, 'Can change comment', 8, 'change_comment'),
(31, 'Can delete comment', 8, 'delete_comment'),
(32, 'Can view comment', 8, 'view_comment'),
(33, 'Can add post', 9, 'add_post'),
(34, 'Can change post', 9, 'change_post'),
(35, 'Can delete post', 9, 'delete_post'),
(36, 'Can view post', 9, 'view_post'),
(37, 'Can add interest', 10, 'add_interest'),
(38, 'Can change interest', 10, 'change_interest'),
(39, 'Can delete interest', 10, 'delete_interest'),
(40, 'Can view interest', 10, 'view_interest'),
(41, 'Can add friend request', 11, 'add_friendrequest'),
(42, 'Can change friend request', 11, 'change_friendrequest'),
(43, 'Can delete friend request', 11, 'delete_friendrequest'),
(44, 'Can view friend request', 11, 'view_friendrequest'),
(45, 'Can add message', 12, 'add_message'),
(46, 'Can change message', 12, 'change_message'),
(47, 'Can delete message', 12, 'delete_message'),
(48, 'Can view message', 12, 'view_message'),
(49, 'Can add unposted content', 13, 'add_unpostedcontent'),
(50, 'Can change unposted content', 13, 'change_unpostedcontent'),
(51, 'Can delete unposted content', 13, 'delete_unpostedcontent'),
(52, 'Can view unposted content', 13, 'view_unpostedcontent'),
(53, 'Can add dataset', 14, 'add_dataset'),
(54, 'Can change dataset', 14, 'change_dataset'),
(55, 'Can delete dataset', 14, 'delete_dataset'),
(56, 'Can view dataset', 14, 'view_dataset');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dataset_table`
--

DROP TABLE IF EXISTS `dataset_table`;
CREATE TABLE IF NOT EXISTS `dataset_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dataset_table`
--

INSERT INTO `dataset_table` (`id`, `title`, `file`, `uploaded_at`) VALUES
(3, 'test_clean1.csv', 'datasets/test_clean1_5i9utGD.csv', '2024-07-13 10:53:40.660497');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mainapp', 'user'),
(8, 'userapp', 'comment'),
(9, 'userapp', 'post'),
(10, 'mainapp', 'interest'),
(11, 'mainapp', 'friendrequest'),
(12, 'userapp', 'message'),
(13, 'userapp', 'unpostedcontent'),
(14, 'adminapp', 'dataset');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-07-08 06:42:57.498628'),
(2, 'auth', '0001_initial', '2024-07-08 06:42:58.120000'),
(3, 'admin', '0001_initial', '2024-07-08 06:42:58.337573'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-07-08 06:42:58.345410'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-07-08 06:42:58.351762'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-07-08 06:42:58.424024'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-07-08 06:42:58.465361'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-07-08 06:42:58.517782'),
(9, 'auth', '0004_alter_user_username_opts', '2024-07-08 06:42:58.524336'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-07-08 06:42:58.561733'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-07-08 06:42:58.562740'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-07-08 06:42:58.569803'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-07-08 06:42:58.605781'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-07-08 06:42:58.639287'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-07-08 06:42:58.676108'),
(16, 'auth', '0011_update_proxy_permissions', '2024-07-08 06:42:58.681975'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-07-08 06:42:58.722636'),
(18, 'sessions', '0001_initial', '2024-07-08 06:42:58.764373'),
(19, 'mainapp', '0001_initial', '2024-07-08 10:04:27.746681'),
(20, 'userapp', '0001_initial', '2024-07-10 07:38:30.594863'),
(21, 'mainapp', '0002_interest_alter_user_age_user_interests', '2024-07-10 10:08:29.715057'),
(22, 'mainapp', '0003_friendrequest', '2024-07-10 10:41:59.012347'),
(23, 'userapp', '0002_message', '2024-07-11 09:56:45.950240'),
(24, 'userapp', '0003_message_read', '2024-07-11 11:25:07.973092'),
(25, 'userapp', '0004_unpostedcontent', '2024-07-13 06:35:53.872144'),
(26, 'adminapp', '0001_initial', '2024-07-13 10:36:16.744149');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('677th9ud8co0ja0005iqp6ayi07cu84k', 'eyJpZF9mb3Jfb3RwX3ZlcmlmaWNhdGlvbl91c2VyIjo2LCJ1c2VyX2lkX2FmdGVyX2xvZ2luIjo1fQ:1sRXH5:nT07yrFsnP7S41FtDF-awHULPvaatJkhvYVzsw0hMNg', '2024-07-24 13:22:23.262471'),
('mqbf55c2aauymmg3yh8ceruc81gfum2y', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjoxfQ:1sRpYD:TNJClN5Gid5gtLZCiE2QCN3KrwM4LZlo40cyokLn95E', '2024-07-25 08:53:17.941527'),
('jistcl1j2k35io0g7ob4ezfg86ckgmqu', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjoxfQ:1sRPwn:7SUtzPFkwSozGAnnoo4Rh1uYbpir5BEOvzu_ie20u-U', '2024-07-24 05:32:57.303737'),
('ntln09o238o728zzk3vpnmzcqd9wfb9d', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjoxfQ:1sRarm:aWP58WwiLVoj49_9Hvy3wRCyr3LfxArk1hs0ycT39wg', '2024-07-24 17:12:30.836665'),
('rnviwwbk9q238t2a5cgvp3h6cn87td1h', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjo2fQ:1sRtgx:Ftfzjey6iSGtVqk3iPnH84J93kq0FHlSKCZVY291-3w', '2024-07-25 13:18:35.439508'),
('ax0efznjvlo0m2b08buavthoif357ld7', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjoxfQ:1sSBm1:0XybKW_791UtQ6QXKmWVlHrL3GV-fSWMBBazio09GxQ', '2024-07-26 08:37:01.681432'),
('q20dt863ogum3hpzlm43n96ctx3kua77', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjoxLCJpZF9mb3Jfb3RwX3ZlcmlmaWNhdGlvbl91c2VyIjo3fQ:1sSKkR:gES3IlK2CjlJL0KiP8U3IdPOXURH5ms1ataACppvDfo', '2024-07-26 18:11:59.049083'),
('489g0fi5wprcione47caswazox32m35j', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjo1fQ:1sSW48:KbyptzsGhrtGwFIfGgFgpRDHNDEqsqp4yC8Q6XnMj44', '2024-07-27 06:17:04.366947'),
('uvesyiqaeuqe756260ec3ayy0snm20cg', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjo1fQ:1sSVv9:Qk2eL5yDBfT4CAS83_NhxLqToMo-o-7TROoOMO0ylNQ', '2024-07-27 06:07:47.302979'),
('lz024hq3pv7ecceoehngbcotku8yzhe1', 'eyJ1c2VyX2lkX2FmdGVyX2xvZ2luIjoxfQ:1sScNC:83Bb06Vyykyj9n6qMN63GUws9WVAlNDkG15BCXrPT7c', '2024-07-27 13:01:10.597910');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_friendrequest`
--

DROP TABLE IF EXISTS `mainapp_friendrequest`;
CREATE TABLE IF NOT EXISTS `mainapp_friendrequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `is_accepted` tinyint(1) NOT NULL,
  `from_user_id` bigint NOT NULL,
  `to_user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mainapp_friendrequest_from_user_id_e34bdcf1` (`from_user_id`),
  KEY `mainapp_friendrequest_to_user_id_33fefd47` (`to_user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainapp_friendrequest`
--

INSERT INTO `mainapp_friendrequest` (`id`, `timestamp`, `is_accepted`, `from_user_id`, `to_user_id`) VALUES
(2, '2024-07-10 11:50:24.298634', 1, 1, 5),
(6, '2024-07-11 11:43:16.968585', 1, 1, 6),
(5, '2024-07-10 13:20:09.143187', 1, 5, 6),
(8, '2024-07-12 17:44:06.071100', 1, 7, 5),
(9, '2024-07-12 18:11:45.675445', 1, 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_interest`
--

DROP TABLE IF EXISTS `mainapp_interest`;
CREATE TABLE IF NOT EXISTS `mainapp_interest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainapp_interest`
--

INSERT INTO `mainapp_interest` (`id`, `name`) VALUES
(6, 'Drawing'),
(5, 'Writing'),
(4, 'Reading'),
(7, 'Singing');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_user`
--

DROP TABLE IF EXISTS `mainapp_user`;
CREATE TABLE IF NOT EXISTS `mainapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `age` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `otp` varchar(6) NOT NULL,
  `otp_status` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainapp_user`
--

INSERT INTO `mainapp_user` (`id`, `full_name`, `email`, `password`, `phone_number`, `age`, `address`, `photo`, `otp`, `otp_status`, `status`) VALUES
(1, 'upender', 'upenderimp25@gmail.com', '1', '12345678', '22', 'lb nagar ', 'profiles/Y3.jpg', '2967', 'Verified', 'Accepted'),
(5, 'codeleaf', 'codeleaf@gmail.com', '1', '1234567890', '22', 'lb nagar', 'profiles/cb_UfvCKMu.jpeg', '4611', 'Verified', 'Hold'),
(6, 'deep', 'deep@gmail.com', '1', '12345678987', '99', 'lb nagar', 'profiles/sad.png', '7456', 'Verified', 'Accepted'),
(7, 'user10', 'user10@gmail.com', '1', '1234567809', '22', 'information colony, hayathnagar', 'profiles/contact_Image.avif', '1417', 'Verified', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_user_interests`
--

DROP TABLE IF EXISTS `mainapp_user_interests`;
CREATE TABLE IF NOT EXISTS `mainapp_user_interests` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `interest_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mainapp_user_interests_user_id_interest_id_221e6c40_uniq` (`user_id`,`interest_id`),
  KEY `mainapp_user_interests_user_id_c3e1c04c` (`user_id`),
  KEY `mainapp_user_interests_interest_id_c273abdc` (`interest_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainapp_user_interests`
--

INSERT INTO `mainapp_user_interests` (`id`, `user_id`, `interest_id`) VALUES
(1, 4, 1),
(2, 4, 2),
(3, 4, 3),
(4, 5, 4),
(5, 5, 5),
(6, 5, 6),
(7, 5, 7),
(8, 6, 4),
(9, 6, 5),
(10, 6, 6),
(11, 6, 7),
(19, 1, 5),
(16, 7, 4),
(17, 7, 5),
(18, 7, 6);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_comment`
--

DROP TABLE IF EXISTS `userapp_comment`;
CREATE TABLE IF NOT EXISTS `userapp_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `post_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_comment_user_id_c6a6df84` (`user_id`),
  KEY `userapp_comment_post_id_a21f0527` (`post_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_comment`
--

INSERT INTO `userapp_comment` (`id`, `text`, `timestamp`, `user_id`, `post_id`) VALUES
(1, 'what is this bro ?', '2024-07-10 08:51:00.008002', 1, 2),
(2, 'what is this are drunk', '2024-07-10 09:27:20.557765', 1, 4),
(3, 'hey me again fool \r\n', '2024-07-10 09:34:29.085231', 1, 4),
(4, 'hey iam codeleaf ????', '2024-07-10 10:22:34.031298', 5, 4),
(5, 'what are you doing deep ! what is that img ???', '2024-07-10 10:24:21.236955', 5, 2),
(6, 'hey hello how are you ', '2024-07-10 11:31:15.572193', 1, 5),
(7, 'nice image deep bro ???????????????????', '2024-07-11 12:56:58.203496', 1, 7),
(8, 'nice image deep bro ???????????????????', '2024-07-11 12:57:38.015671', 1, 7),
(9, 'hey ????', '2024-07-11 12:59:43.285079', 1, 6),
(10, 'hello\r\n', '2024-07-13 12:58:57.645493', 1, 11);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_message`
--

DROP TABLE IF EXISTS `userapp_message`;
CREATE TABLE IF NOT EXISTS `userapp_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `from_user_id` bigint NOT NULL,
  `to_user_id` bigint NOT NULL,
  `read` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_message_from_user_id_a6ae52f3` (`from_user_id`),
  KEY `userapp_message_to_user_id_5b8be759` (`to_user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_message`
--

INSERT INTO `userapp_message` (`id`, `message`, `timestamp`, `from_user_id`, `to_user_id`, `read`) VALUES
(3, 'hello codeleaf team we want a project ! ', '2024-07-11 10:34:08.235583', 1, 5, 'read'),
(4, 'hi upender how are you ', '2024-07-11 12:47:49.046999', 6, 1, 'read'),
(5, 'nhyyj', '2024-07-11 13:14:27.008419', 1, 5, 'read'),
(6, 'iam good bro how are you ?', '2024-07-12 08:35:56.876143', 1, 6, 'read'),
(7, 'where are you ? upender', '2024-07-12 08:36:46.099150', 6, 1, 'read'),
(8, 'hey codeleaf !!', '2024-07-13 13:00:09.236407', 1, 5, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_post`
--

DROP TABLE IF EXISTS `userapp_post`;
CREATE TABLE IF NOT EXISTS `userapp_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext,
  `image` varchar(100) DEFAULT NULL,
  `video` varchar(100) DEFAULT NULL,
  `audio` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_post_user_id_f7394edb` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_post`
--

INSERT INTO `userapp_post` (`id`, `text`, `image`, `video`, `audio`, `timestamp`, `user_id`) VALUES
(1, 'hi iam upender posting my first text in blog', '', '', '', '2024-07-10 07:41:13.500486', 1),
(2, 'this is my first img ????????????', 'posts/images/WhatsApp_Image_2024-07-08_at_6.00.32_PM.jpeg', '', '', '2024-07-10 07:41:58.174392', 1),
(3, 'long video ????????????', '', 'posts/videos/Screen_Recording_2024-07-02_182436.mp4', '', '2024-07-10 07:42:38.533538', 1),
(4, 'In the provided code snippet, the elements for images, videos, and audios are indeed placed towards the end of the card-body section, while the text content is not. This is likely due to how the conditional blocks ({% if post.text %}) are structured in relation to the other content.\r\n\r\nTo ensure consistency in layout, you can adjust the structure so that all content types are handled similarly. Here\'s how you can structure it:', '', '', '', '2024-07-10 09:26:47.849715', 1),
(5, 'hello all we are from code book . hope you like our logo ????', 'posts/images/cb.jpeg', '', '', '2024-07-10 10:23:35.420612', 5),
(6, 'iam deep pratap', 'posts/images/sad.png', '', '', '2024-07-10 12:57:12.607151', 6),
(7, NULL, 'posts/images/brain.jpg', '', '', '2024-07-10 13:21:52.331727', 6),
(8, 'police\r\n', 'posts/images/pol15.jpg', '', '', '2024-07-11 13:15:40.875829', 5),
(9, 'How to Overlay\nText on an Image\nin HTML and CSS\n\nJosephine Loo', 'posts/images/image.jpg', '', '', '2024-07-13 06:17:54.450027', 5),
(10, 'follow up from the gentlemen who were kicked off of  user airlines for simply speaking arabic', '', '', '', '2024-07-13 06:30:23.775414', 5),
(11, 'how many pols passed by how many times and said nothing bluelivesmatter draintheswamp ferguson', '', '', '', '2024-07-13 06:39:35.031638', 5);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_post_likes`
--

DROP TABLE IF EXISTS `userapp_post_likes`;
CREATE TABLE IF NOT EXISTS `userapp_post_likes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `post_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userapp_post_likes_post_id_user_id_5d8c7adb_uniq` (`post_id`,`user_id`),
  KEY `userapp_post_likes_post_id_8e62672c` (`post_id`),
  KEY `userapp_post_likes_user_id_8a029c53` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_post_likes`
--

INSERT INTO `userapp_post_likes` (`id`, `post_id`, `user_id`) VALUES
(2, 3, 1),
(3, 2, 1),
(4, 1, 1),
(5, 4, 1),
(6, 4, 5),
(7, 5, 1),
(8, 3, 5),
(9, 7, 1),
(10, 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_unpostedcontent`
--

DROP TABLE IF EXISTS `userapp_unpostedcontent`;
CREATE TABLE IF NOT EXISTS `userapp_unpostedcontent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext,
  `image` varchar(100) DEFAULT NULL,
  `video` varchar(100) DEFAULT NULL,
  `audio` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_unpostedcontent_user_id_f9fc9667` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userapp_unpostedcontent`
--

INSERT INTO `userapp_unpostedcontent` (`id`, `text`, `image`, `video`, `audio`, `timestamp`, `user_id`) VALUES
(1, 'if you hold open a door for a woman because she s a woman and not because it s a nice thing to do that s don t even try to deny it', '', '', '', '2024-07-13 06:40:05.892784', 5),
(2, 'user and you keep telling that only aryans are allowed to rape women you re just a troll eod user user', '', '', '', '2024-07-13 07:17:53.623403', 1),
(4, 'user and you keep telling that only aryans are allowed to rape women you re just a troll eod user user', 'unposted/images/Screenshot_2024-07-13_124917_nt2XR3Y.png', '', '', '2024-07-13 12:53:38.816040', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
