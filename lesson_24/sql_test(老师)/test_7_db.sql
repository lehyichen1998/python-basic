/*
Navicat MySQL Data Transfer

Source Server         : class_7_test
Source Server Version : 50712
Source Host           : localhost:3306
Source Database       : test_7_db

Target Server Type    : MYSQL
Target Server Version : 50712
File Encoding         : 65001

Date: 2021-04-19 21:25:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tb_score`
-- ----------------------------
DROP TABLE IF EXISTS `tb_score`;
CREATE TABLE `tb_score` (
  `s_id` int(10) NOT NULL AUTO_INCREMENT,
  `s_python` int(10) NOT NULL,
  `s_html` int(10) NOT NULL,
  `s_c` int(10) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_score
-- ----------------------------
INSERT INTO `tb_score` VALUES ('1', '30', '30', '30');
INSERT INTO `tb_score` VALUES ('2', '40', '40', '40');
INSERT INTO `tb_score` VALUES ('3', '50', '50', '50');
INSERT INTO `tb_score` VALUES ('4', '60', '60', '60');
INSERT INTO `tb_score` VALUES ('5', '70', '70', '70');
INSERT INTO `tb_score` VALUES ('6', '80', '80', '80');

-- ----------------------------
-- Table structure for `tb_stu`
-- ----------------------------
DROP TABLE IF EXISTS `tb_stu`;
CREATE TABLE `tb_stu` (
  `s_id` int(10) NOT NULL AUTO_INCREMENT,
  `s_name` varchar(20) NOT NULL,
  `s_gender` char(10) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_stu
-- ----------------------------
INSERT INTO `tb_stu` VALUES ('1', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('2', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('3', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('4', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('5', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('6', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('7', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('8', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('9', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('10', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('11', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('12', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('13', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('14', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('15', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('16', '大雄', 'male');
INSERT INTO `tb_stu` VALUES ('17', '金乡', 'female');

-- ----------------------------
-- Table structure for `tb_teacher`
-- ----------------------------
DROP TABLE IF EXISTS `tb_teacher`;
CREATE TABLE `tb_teacher` (
  `t_id` int(10) NOT NULL AUTO_INCREMENT,
  `t_name` varchar(20) NOT NULL,
  `t_subject` varchar(20) NOT NULL,
  `t_gender` char(10) NOT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_teacher
-- ----------------------------
INSERT INTO `tb_teacher` VALUES ('1', 'chugu', 'web_site', 'male');
INSERT INTO `tb_teacher` VALUES ('2', 'xionzi', 'scraper', 'male');
INSERT INTO `tb_teacher` VALUES ('3', 'jiyuan', 'scraper', 'male');
INSERT INTO `tb_teacher` VALUES ('4', 'model', 'Ai', 'male');
INSERT INTO `tb_teacher` VALUES ('5', 'mufen', 'scraper', 'male');
