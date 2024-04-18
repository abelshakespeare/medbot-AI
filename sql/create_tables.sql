-- Create a table for storing patient information
CREATE TABLE Patients (
    PatientID SERIAL PRIMARY KEY,
    MaritalStatus VARCHAR(10),
    Gender VARCHAR(10),
    Nationality VARCHAR(50),
    AgeAtAppointmentDate INT,
    SMS VARCHAR(10)
);

-- Create a table for storing doctor information
CREATE TABLE Doctors (
    DoctorID SERIAL PRIMARY KEY
);

-- Create a table for storing appointment details
CREATE TABLE Appointments (
    AppointmentID SERIAL PRIMARY KEY,
    PatientID INT,
    DoctorID INT,
    AppointmentDate TIMESTAMP,
    AppointmentTime TIME,
    BookingDateTime TIMESTAMP,
    DurationMinutes INT,
    Attend BOOLEAN,
    Temperature DECIMAL(5,2),
    Weather VARCHAR(50),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);