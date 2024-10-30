# Design Document
By Santasila Bryan

GitHub Username: SBryanK

Video overview:https://youtu.be/mxMgaRxEoXM

## Scope
The database is designed to manage participant information and their interactions within an event or conference. It includes all entities necessary to:

* Store participant profiles with detailed contact information.
* Record food and beverage selections for each participant.
* Track participant attendance at various stages of the event.
* Monitor lounge area usage within stages.
* Excluded from the scope are payment processing, scheduling details, and other non-essential features.

## Functional Requirements
This database will support:

* CRUD (Create, Read, Update, Delete) operations for participant profiles.
* Recording and retrieving food and beverage selections for participants.
* Logging participant entry and exit times for different stages.
* Monitoring lounge area usage, including entry and exit times.

Note that group registrations and financial transactions are not supported in this version.

## Representation
Entities are represented in SQL tables with carefully designed schemas to ensure data integrity and efficient access.

## Entities
The database includes the following entities:

### Profiles
The profiles table stores participant information and includes:

* id: An INTEGER serving as the unique identifier for each participant. It is the PRIMARY KEY of the table.
* first_name: A VARCHAR(30) representing the participant's first name. It is NOT NULL.
* last_name: A VARCHAR(30) representing the participant's last name. It is NOT NULL.
* mobile_number: A VARCHAR(12) for the participant's mobile number. It has a UNIQUE constraint to prevent duplicates.
* email: A VARCHAR storing the participant's email address. It is both NOT NULL and UNIQUE.
* linkedin: A VARCHAR containing the participant's LinkedIn profile URL. It is NOT NULL and UNIQUE.
* company_name: A VARCHAR indicating the participant's company. It is NOT NULL.
* company_id: A VARCHAR representing the company's identifier. It is NOT NULL.
* ROLE: A VARCHAR specifying the participant's role within the event. It is NOT NULL.

All columns are required, ensuring that each participant's profile is complete and unique where necessary.

### Food and Beverage Selection
The f&b_selection table captures participants' meal preferences:

* id: An INTEGER that auto-increments to uniquely identify each selection. It is the PRIMARY KEY.
* meal_region: A VARCHAR(15) indicating the preferred cuisine type. It is NOT NULL and restricted by a CHECK constraint to the values 'ASIAN', 'WESTERN', 'MEDITERRANEAN', 'INDIAN', or 'VEGETARIAN'.
* time_access: A NUMERIC timestamp recording when the selection was made. It defaults to the current timestamp via DEFAULT CURRENT_TIMESTAMP.
* breakfast_sel: An INTEGER indicating breakfast selection. It is NOT NULL and constrained to values between 0 and 3 inclusive.
* lunch_sel: An INTEGER indicating lunch selection. It follows the same constraints as breakfast_sel.
* dinner_sel: An INTEGER indicating dinner selection. It follows the same constraints as breakfast_sel.
All meal selection columns are required and validated to ensure participants select from predefined options.

### Stage
The stage table records participant attendance at different event stages:

* id: An INTEGER that auto-increments, serving as part of the composite PRIMARY KEY.
* stage_type: A VARCHAR(15) indicating the type of stage. It is NOT NULL and restricted by a CHECK constraint to the values 'ESG', 'TECHNOLOGY', 'REGULATION', or 'INNOVATION'.
* entry_time: A NUMERIC timestamp marking when the participant entered the stage. It defaults to CURRENT_TIMESTAMP.
* exit_time: A NUMERIC timestamp marking when the participant exited the stage. It also defaults to CURRENT_TIMESTAMP.
* The PRIMARY KEY is a composite of id and stage_type, ensuring each record uniquely identifies a participant's attendance at a specific stage.

### Lounge Area
The lounge_area table monitors usage of lounges within stages:

* id: An INTEGER that auto-increments as the PRIMARY KEY.
* type: A VARCHAR(15) representing the lounge's stage type. It is NOT NULL and constrained to match the stage_type in the stage table via a FOREIGN KEY.
* lounge_number: An INTEGER indicating the specific lounge number. It is NOT NULL and must be between 1 and 10 inclusive, enforced by a CHECK constraint.
* entry_time: A NUMERIC timestamp for when the participant entered the lounge. It defaults to CURRENT_TIMESTAMP.
* exit_time: A NUMERIC timestamp for when the participant exited the lounge. It also defaults to CURRENT_TIMESTAMP.
* The type column's FOREIGN KEY constraint ensures referential integrity with the stage table.

### Relationships
The entity-relationship structure of the database is as follows:

Profiles to Food and Beverage Selection: Each participant in profiles may have one or more entries in f&b_selection, capturing their meal preferences.
Stage and Lounge Area: The lounge_area is associated with a stage via the type and stage_type relationship, enforcing consistency in stage types.
Participants and Event Activities: While not explicitly linked in the current schema, participants are intended to be associated with their stage attendance and lounge usage.
Constraints and Checks
Unique Constraints: Ensure no duplication of critical contact information like email, mobile_number, and linkedin.
Not Null Constraints: Mandate essential information is provided for each participant and selection.
Check Constraints: Validate that entries for meal_region, stage_type, and type are within the specified acceptable values.
Foreign Keys: Maintain referential integrity between lounge_area and stage tables.

## Optimizations
To enhance query performance, especially for commonly accessed data, the following indexes are implemented:

Participant Name Search: An index on the profiles table covering first_name and last_name to speed up searches by participant names.
Stage Search: An index on the stage table covering id and stage_type to optimize queries filtering by stage identifiers and types.
Lounge Search: An index on the lounge_area table covering id and type to expedite searches for lounge area usage records.
These indexes are designed to improve the efficiency of read operations without significantly impacting write performance.

## Limitations
The current schema has several limitations:

Lack of Participant Activity Linkage: There are no participant_id foreign keys in the stage and lounge_area tables. This omission means participant activities in stages and lounges cannot be directly associated with their profiles.
Food and Beverage Association: The f&b_selection table lacks a foreign key linking selections to specific participants, preventing direct correlation of meal preferences with individual profiles.
Constraint Errors: There are inconsistencies in the CHECK constraints, such as referencing incorrect column names (e.g., using "type" instead of "stage_type") and comparing numeric fields to string literals.
Data Type Issues: Using NUMERIC for timestamps may not be appropriate. A dedicated TIMESTAMP or DATETIME data type would provide better functionality and accuracy.
Composite Primary Keys: The stage table's primary key references a non-existent "stage" column. It should be corrected to "stage_type" or adjusted to a single-column primary key if appropriate.

To address these limitations, the schema should be revised to:

Add participant_id foreign keys to the f&b_selection, stage, and lounge_area tables.
Correct CHECK constraints to reference the appropriate columns and compare compatible data types.
Use appropriate data types for timestamp fields.
Ensure all primary keys reference existing columns.
By making these adjustments, the database will better support the intended functionalities and maintain data integrity.
