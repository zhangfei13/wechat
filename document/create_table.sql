-- 用户信息表
CREATE TABLE IF NOT EXISTS `v_user`(
    `user_id` BIGINT(120) AUTO_INCREMENT,
    `wechat_no` VARCHAR(60),
    `id_type` INT(10),
    `id_no` VARCHAR(30),
    `name` VARCHAR(60),
    `phone` VARCHAR(20),
    `user_level` INT(10),
    `status` VARCHAR(10),
    `self_proc_illegal` VARCHAR(10),
    `desc` VARCHAR(120),
    PRIMARY KEY ( `user_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
DROP INDEX wechat_no_index ON v_user;
ALTER TABLE v_user ADD INDEX wechat_no_index (wechat_no);

-- 车辆违法信息表
CREATE TABLE IF NOT EXISTS `vehicle_illegal_info`(
    `vehicle_id` BIGINT,
    `illegal_type` VARCHAR(60),
    `desc` VARCHAR(1024)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 枚举信息表
CREATE TABLE IF NOT EXISTS `enum_info`(
    `id` INT(30) AUTO_INCREMENT,
    `enum_no` INT(20),
    `enum_type` VARCHAR(50),
    `enum_subtype` VARCHAR(50),
    `enum_value` VARCHAR(120),
    `desc` INT(120),
    PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;