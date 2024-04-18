-- Set the DateStyle to European, DMY (Day, Month, Year)
SET DateStyle = 'ISO, DMY';

-- Create a temporary staging table
CREATE TEMP TABLE Staging (
    MaritalStatus VARCHAR(10),
    Gender VARCHAR(10),
    Nationality VARCHAR(50),
    AppointmentDate TIMESTAMP,
    AppointmentTime TIME,
    BookingDateTime TIMESTAMP,
    DurationMinutes INT,
    SMS VARCHAR(10),
    DoctorID INT,
    Attend BOOLEAN,
    AgeAtAppointmentDate INT,
    Temperature DECIMAL(5,2),
    Weather VARCHAR(50)
);

-- Load data from CSV file into the staging table
COPY Staging
FROM '/Users/abelshakespeare/Documents/GitHub/medbot-AI/data/cleaned/cleaned_data.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');

-- Insert data into Doctors table, avoiding duplicates
INSERT INTO Doctors (DoctorID)
SELECT DISTINCT DoctorID FROM Staging;

-- Insert data into Patients table, generating unique PatientIDs
INSERT INTO Patients (MaritalStatus, Gender, Nationality, AgeAtAppointmentDate, SMS)
SELECT DISTINCT MaritalStatus, Gender, Nationality, AgeAtAppointmentDate, SMS FROM Staging;

-- Map PatientID from Patients to insert into Appointments
INSERT INTO Appointments (
    PatientID, DoctorID, AppointmentDate, AppointmentTime, BookingDateTime,
    DurationMinutes, Attend, Temperature, Weather
)
SELECT 
    p.PatientID, 
    s.DoctorID, 
    s.AppointmentDate, 
    s.AppointmentTime, 
    s.BookingDateTime, 
    s.DurationMinutes, 
    s.Attend, 
    s.Temperature, 
    s.Weather
FROM 
    Staging s
JOIN 
    Patients p ON p.MaritalStatus = s.MaritalStatus AND p.Gender = s.Gender
                 AND p.Nationality = s.Nationality AND p.AgeAtAppointmentDate = s.AgeAtAppointmentDate
                 AND p.SMS = s.SMS;

-- Drop the staging table
DROP TABLE Staging;

