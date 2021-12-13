-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recipes_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema recipes_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipes_schema` ;
USE `recipes_schema` ;

-- -----------------------------------------------------
-- Table `recipes_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` CHAR(60) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes_schema`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_schema`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `name` VARCHAR(100) NULL,
  `description` VARCHAR(255) NULL,
  `instructions` TEXT NULL,
  `under_30` TINYINT(1) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipes_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes_schema`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_schema`.`likes` (
  `user_id` INT NOT NULL,
  `recipe_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `recipe_id`),
  INDEX `fk_users_has_recipes_recipes1_idx` (`recipe_id` ASC) VISIBLE,
  INDEX `fk_users_has_recipes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipes_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_recipes_recipes1`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipes_schema`.`recipes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
