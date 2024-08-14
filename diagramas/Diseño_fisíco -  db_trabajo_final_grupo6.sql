-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema biks_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema biks_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biks_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `biks_db` ;

-- -----------------------------------------------------
-- Table `biks_db`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`category` (
  `id_category` INT NOT NULL,
  `category_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_category`),
  UNIQUE INDEX `id_category_UNIQUE` (`id_category` ASC) VISIBLE,
  UNIQUE INDEX `category_name_UNIQUE` (`category_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`brand` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`category` (
  `id_category` INT NOT NULL,
  `category_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_category`),
  UNIQUE INDEX `id_category_UNIQUE` (`id_category` ASC) VISIBLE,
  UNIQUE INDEX `category_name_UNIQUE` (`category_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`accessories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`accessories` (
  `id_product` INT NOT NULL,
  `product_category` VARCHAR(45) NOT NULL,
  `brand_accessories` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_product`),
  UNIQUE INDEX `id_product_UNIQUE` (`id_product` ASC) VISIBLE,
  UNIQUE INDEX `product_category_UNIQUE` (`product_category` ASC) VISIBLE,
  UNIQUE INDEX `brand_accessories_UNIQUE` (`brand_accessories` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`payment` (
  `id_payment` INT NOT NULL,
  `payment_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_payment`),
  UNIQUE INDEX `id_payment_UNIQUE` (`id_payment` ASC) VISIBLE,
  UNIQUE INDEX `payment_name_UNIQUE` (`payment_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`cart_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`cart_item` (
  `id_cart_item` INT NOT NULL,
  `costumer` VARCHAR(45) NOT NULL,
  `date` DATETIME NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `payment_type` VARCHAR(45) NOT NULL,
  `total` VARCHAR(45) NOT NULL,
  `payment_id_payment` INT NOT NULL,
  PRIMARY KEY (`id_cart_item`),
  UNIQUE INDEX `id_shopping_UNIQUE` (`id_cart_item` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`product` (
  `id_product` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `price` VARCHAR(45) NOT NULL,
  `stock` INT NOT NULL,
  `description` VARCHAR(45) NULL,
  `product_picture` VARCHAR(45) NOT NULL,
  `accessories_id_product` INT NOT NULL,
  `cart_item_id_cart_item` INT NOT NULL,
  PRIMARY KEY (`id_product`),
  UNIQUE INDEX `id_product_UNIQUE` (`id_product` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`bikes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`bikes` (
  `id_bike` INT NOT NULL,
  `bikes_stock` INT NOT NULL,
  `product_id_product` INT NOT NULL,
  PRIMARY KEY (`id_bike`),
  UNIQUE INDEX `id_bike_UNIQUE` (`id_bike` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`brand_bikes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`brand_bikes` (
  `id_brand_bike` INT NOT NULL,
  `brand_bike` VARCHAR(45) NOT NULL,
  `bikes_id_bike` INT NOT NULL,
  PRIMARY KEY (`id_brand_bike`),
  UNIQUE INDEX `id_brand_UNIQUE` (`id_brand_bike` ASC) VISIBLE,
  UNIQUE INDEX `brand_name_UNIQUE` (`brand_bike` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`costumer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`costumer` (
  `id_costumer` INT NOT NULL,
  `costumer_name` VARCHAR(45) NOT NULL,
  `costumer_id_card` INT NOT NULL,
  `costumer_phone` INT NOT NULL,
  `costumer_adress` VARCHAR(45) NOT NULL,
  `costumer_genre` VARCHAR(45) NOT NULL,
  `costumer_email` VARCHAR(45) NOT NULL,
  `cart_item_id_cart_item` INT NOT NULL,
  `cart_item_id_cart_item1` INT NOT NULL,
  PRIMARY KEY (`id_costumer`),
  UNIQUE INDEX `id_costumer_UNIQUE` (`id_costumer` ASC) VISIBLE,
  UNIQUE INDEX `costumer_id_card_UNIQUE` (`costumer_id_card` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`brand_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`brand_products` (
  `id_category_products` INT NOT NULL,
  `product_id_product` INT NOT NULL,
  PRIMARY KEY (`id_category_products`),
  UNIQUE INDEX `id_category_products_UNIQUE` (`id_category_products` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`bikes_has_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`bikes_has_category` (
  `bikes_id_bike` INT NOT NULL,
  `category_id_category` INT NOT NULL,
  PRIMARY KEY (`bikes_id_bike`, `category_id_category`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biks_db`.`accessories_has_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biks_db`.`accessories_has_category` (
  `accessories_id_product` INT NOT NULL,
  `category_id_category` INT NOT NULL,
  PRIMARY KEY (`accessories_id_product`, `category_id_category`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
