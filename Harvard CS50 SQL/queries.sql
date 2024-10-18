-- Add a new participant
INSERT INTO "profile" ("id", "first_name", "last_name", "mobile_number", "email", "company_name", "role")
VALUES ('1', 'John', 'Doe', '+6599911111', 'john1doe@gmail.com', 'Google', 'CEO');

-- Add a new f&b selection for breakfast
INSERT INTO "f&b_selection" ("id", "meal_region", "time_access", "breakfast_sel", "lunch_sel", "dinner_sel")
VALUES (1, 'ASIAN', 'Data Analyst', '12/2/2026 09:00', '3', '0', '0');

-- Add a new stage data
INSERT INTO "stage" ("id", "stage_type", "entry_time", "exit_time")
VALUES (1, 1, 'TECHNOLOGY', '12/2/2026 09:10', '12/2/2026 09:50');

-- Add a new job requirement
INSERT INTO "lounge_area" ("id", "type", "lounge_number", "entry_time", "exit_time")
VALUES (1, 1, 'TECHNOLOGY', '3', '12/2/2026 10:10', '12/2/2026 13.00');


-- Find details of people from Google
SELECT *
FROM "profile"
WHERE "id" = (
    SELECT "id"
    FROM "profile"
    WHERE "comapny_name" = 'Google'
);

-- Find the people who choose ASIAN meal
SELECT *
FROM "f&b_selection"
WHERE "id" = (
    SELECT "id"
    FROM "f&b_selection"
    WHERE "meal_region" = 'ASIAN'
);

-- Update the status of the role of employee number 1 to Owner
UPDATE `profile`
SET `role` = 'Owner'
WHERE `id` = 1;


-- Database to manage attandee in a conference when they want to enter and exit venue, as well as visit every stgaes and booths,
-- most importantly when they will enter food and beverage area and also lounge and stage area. 

