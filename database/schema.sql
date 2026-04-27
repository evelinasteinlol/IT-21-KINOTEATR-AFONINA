-- Создание таблиц
CREATE TABLE `Cinema_Halls` (
  `id` INT PRIMARY KEY,
  `name` VARCHAR(255),
  `total_rows` INT,
  `total_seats` INT,
  `category` TEXT,
  `is_active` BOOLEAN
);

CREATE TABLE `Movies` (
  `id` INT PRIMARY KEY,
  `title` TEXT,
  `genre` TEXT,
  `duration` INT,
  `age_rating` VARCHAR(5),
  `release_year` INT,
  `description` TEXT
);

CREATE TABLE `Sessions` (
  `id` INT PRIMARY KEY,
  `movie_id` INT,
  `hall_id` INT,
  `start_time` DATETIME,
  `price` DECIMAL(10,2),
  `format` TEXT,
  FOREIGN KEY (`hall_id`) REFERENCES `Cinema_Halls`(`id`),
  FOREIGN KEY (`movie_id`) REFERENCES `Movies`(`id`)
);

CREATE TABLE `Tickets` (
  `id` INT PRIMARY KEY,
  `session_id` INT,
  `row_number` INT,
  `seat_number` INT,
  `sale_time` DATETIME,
  `status` TEXT,
  FOREIGN KEY (`session_id`) REFERENCES `Sessions`(`id`)
);
