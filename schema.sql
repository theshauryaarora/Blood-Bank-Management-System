CREATE DATABASE BloodBankDB;
USE BloodBankDB;

CREATE TABLE donor_registry (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(50) NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    units_available INT NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    hospital_hub VARCHAR(50) NOT NULL
);