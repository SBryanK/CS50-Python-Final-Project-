-- Represent the details of participants
CREATE TABLE "profiles" (
    "id" INTEGER,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL,
    "mobile_number" VARCHAR(15) UNIQUE,
    "email" VARCHAR NOT NULL UNIQUE,
    "company_name" VARCHAR NOT NULL,
    "ROLE" VARCHAR NOT NULL,
    PRIMARY KEY("id")
);

-- Represent the details of food and beverages type
CREATE TABLE "f&b_selection" (
    "id" INTEGER AUTO_INCREMENT,
    "meal_region" VARCHAR(15) NOT NULL CHECK ("meal_region" IN ('ASIAN', 'WESTERN', 'MEDITERANIAN', 'INDIAN', 'VEGETARIAN')) NOT NULL,
    "time_access" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "breakfast_sel" NUMERIC NOT NULL CHECK("breakfast_sel" IN('0', '1', '2', '3')) ,
    "lunch_sel" NUMERIC NOT NULL CHECK("breakfast_sel" IN('0', '1', '2', '3')),
    "dinner_sel" NUMERIC NOT NULL CHECK("breakfast_sel" IN('0', '1', '2', '3')),
    PRIMARY KEY("id")
);

-- Represent the details of stage choice
CREATE TABLE "stage" (
    "id" INT AUTO_INCREMENT,
    "stage_type" VARCHAR(15) NOT NULL CHECK ("type" IN ('ESG', 'TECHNOLOGY', 'REGULATION', 'INNOVATION')) NOT NULL,
    "entry_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "exit_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id","stage")
);

-- Represent the details of lounge area inside stage
CREATE TABLE "lounge_area" (
    "id" INTEGER AUTO_INCREMENT,
    "type" VARCHAR(15) NOT NULL CHECK ("type" IN ('ESG', 'TECHNOLOGY', 'REGULATION', 'INNOVATION')) NOT NULL,
    "lounge_number" INTEGER NOT NULL CHECK ("type" BETWEEN 1 AND 10) NOT NULL,
    "entry_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "exit_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id"),
    FOREIGN KEY("type") REFERENCES "stage"("stage_type")
);

-- Create indexes to speed common searches
CREATE INDEX "participant_name_search" ON "participant" ("first_name", "last_name");
CREATE INDEX "stage_search" ON "stage" ("id", "stage_type");
CREATE INDEX "lounge_search" ON "lounge_area" ("id", "type");
