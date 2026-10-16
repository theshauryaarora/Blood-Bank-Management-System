# Blood Bank Management System

A Python and MySQL application designed to help hospitals track blood donor records, manage current inventory levels, and quickly search for matching blood types during emergencies.

This project uses a Python terminal interface connected to a local relational database to handle data storage.

## Features
* **Register New Donors**: Input donor names, blood groups, donated units, and contact details.
* **Location Mapping**: Assign blood donations to specific hospital hubs or a default backup depot.
* **Blood Group Search**: Query the database to instantly display all matching donors and their locations for a requested blood type.

## Requirements
* Python 3.x
* MySQL Server
* `mysql.connector` library

## Database Configuration
The application connects to a MySQL database named `BloodBankDB`. It uses a table called `donor_registry` with the following columns:
* `donor_id`: Unique ID for each donor (Primary Key, Auto-Increment)
* `donor_name`: Full name of the donor
* `blood_group`: Blood type (e.g., A+, O-, AB+)
* `units_available`: Number of blood units donated
* `contact_number`: Phone number of the donor
* `hospital_hub`: The hospital facility where the blood unit is stored

## File Descriptions
* **blood_bank_management_system.py**: The main Python script that runs the application menu and executes database queries.
* **schema.sql**: The SQL script used to create the required database and table structure.

## Setup Instructions
1. Run the commands inside `schema.sql` in your MySQL client to set up the database and tables.
2. Open `blood_bank_router.py` and update the `password` field in the `connect_database()` function with your local MySQL password.
3. Run the Python script to open the application menu in your terminal.
