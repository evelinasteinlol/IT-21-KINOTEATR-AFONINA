CREATE TABLE `Cinema_Halls` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `total_rows` integer,
  `total_seats` integer,
  `category` text,
  `is_active` boolean
);

CREATE TABLE `Movies` (
  `id` integer PRIMARY KEY,
  `title` TEXT,
  `genre` TEXT,
  `duration` INTEGER,
  `age_rating` VARCHAR(5),
  `release_year` INTEGER,
  `description` TEXT
);

CREATE TABLE `Sessions` (
  `id` integer PRIMARY KEY,
  `movie_id` integer,
  `hall_id` integer,
  `start_time` datetime,
  `prive` decimal,
  `format` text
);

CREATE TABLE `Tickets` (
  `id` integer PRIMARY KEY,
  `session_id` integer,
  `row_number` integer,
  `seat_number` integer,
  `sale_time` datetime,
  `status` text
);

ALTER TABLE `Sessions` ADD FOREIGN KEY (`hall_id`) REFERENCES `Cinema_Halls` (`id`);

ALTER TABLE `Tickets` ADD FOREIGN KEY (`session_id`) REFERENCES `Sessions` (`id`);

ALTER TABLE `Sessions` ADD FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`id`);
