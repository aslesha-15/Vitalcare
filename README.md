# Health Information System

A comprehensive Python-based health information management system for tracking and managing patient vital signs data. This system allows healthcare professionals to store, retrieve, analyze, and manage patient visit records efficiently.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Data Format](#data-format)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Data Validation](#data-validation)
- [File Structure](#file-structure)
- [Functions Documentation](#functions-documentation)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Health Information System is designed to help healthcare facilities manage patient vital signs data effectively. It provides a command-line interface for healthcare workers to input, view, and analyze patient data while ensuring data integrity through comprehensive validation.

## Features

### Core Functionality
- **Patient Data Management**: Add, view, and delete patient visit records
- **Data Import**: Read patient data from CSV files
- **Statistical Analysis**: Calculate average vital signs for individual patients or all patients
- **Search Capabilities**: Find visits by specific dates, months, or years
- **Follow-up Identification**: Automatically identify patients requiring follow-up care
- **Data Persistence**: Save all changes back to the data file

### Data Tracking
The system tracks the following vital signs for each patient visit:
- Patient ID
- Visit Date
- Body Temperature (°C)
- Heart Rate (bpm)
- Respiratory Rate (bpm)
- Systolic Blood Pressure (mmHg)
- Diastolic Blood Pressure (mmHg)
- Oxygen Saturation (%)

## Data Format

### Input File Format
Patient data should be stored in a CSV file (`patients.txt`) with the following format:
```
patient_id,visit_date,temperature,heart_rate,respiratory_rate,systolic_bp,diastolic_bp,oxygen_saturation
```

### Example Data
```
101,2023-01-15,36.5,72,18,120,80,98
102,2023-01-16,37.2,85,20,130,85,96
101,2023-01-20,36.8,68,16,115,75,99
```

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/health-information-system.git
cd health-information-system
```

2. Ensure you have a `patients.txt` file in the same directory, or the system will create one when you add data.

3. Run the program:
```bash
python Main.22beej54.py
```

## Usage

Launch the application by running the main Python file. The system presents an interactive menu with 8 options:

```
Welcome to the Health Information System

1. Display all patient data
2. Display patient data by ID
3. Add patient data
4. Display patient statistics
5. Find visits by year, month, or both
6. Find patients who need follow-up
7. Delete all visits of a particular patient
8. Quit
```

## Menu Options

### 1. Display All Patient Data
Shows complete visit history for all patients in the system, including all vital signs for each visit.

### 2. Display Patient Data by ID
Displays all visit records for a specific patient when provided with their ID.

### 3. Add Patient Data
Allows input of new patient visit data with real-time validation:
- Patient ID (integer)
- Visit date (YYYY-MM-DD format)
- Temperature, heart rate, respiratory rate, blood pressures, and oxygen saturation

### 4. Display Patient Statistics
Calculates and displays average vital signs:
- For a specific patient (when ID is provided)
- For all patients (when ID is 0)

### 5. Find Visits by Date
Search functionality to find visits by:
- Specific year
- Specific month
- Specific year and month combination
- All visits (when both year and month are 0)

### 6. Find Patients Who Need Follow-up
Automatically identifies patients requiring follow-up based on these criteria:
- Heart rate < 60 or > 100 bpm
- Systolic blood pressure > 140 mmHg
- Oxygen saturation < 90%

### 7. Delete All Visits
Removes all visit records for a specified patient ID.

### 8. Quit
Exits the application.

## Data Validation

The system implements comprehensive data validation to ensure data integrity:

### Vital Signs Ranges
- **Temperature**: 35.0 - 42.0°C
- **Heart Rate**: 30 - 180 bpm
- **Respiratory Rate**: 5 - 40 bpm
- **Systolic Blood Pressure**: 70 - 200 mmHg
- **Diastolic Blood Pressure**: 40 - 120 mmHg
- **Oxygen Saturation**: 70 - 100%

### Date Validation
- Must be in YYYY-MM-DD format
- Month must be 1-12
- Day must be 1-31
- Uses Python's datetime module for format validation

### Input Validation
- Patient IDs must be positive integers
- All vital signs must be within acceptable medical ranges
- Handles invalid data types gracefully with error messages

## File Structure

```
health-information-system/
├── Main.22beej54.py          # Main application file
├── patients.txt              # Patient data file (CSV format)
└── README.md                 # This documentation
```

## Functions Documentation

### Core Functions

#### `readPatientsFromFile(fileName)`
- Reads patient data from CSV file
- Validates each record during import
- Returns dictionary with patient ID as key and visit list as value

#### `displayPatientData(patients, patientId=0)`
- Displays patient visit data
- Shows all patients when patientId=0
- Shows specific patient when patientId is provided

#### `displayStats(patients, patientId=0)`
- Calculates and displays average vital signs
- Supports both individual patient and aggregate statistics

#### `addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName)`
- Adds new patient visit record
- Validates all input parameters
- Appends data to file and updates in-memory dictionary

#### `findVisitsByDate(patients, year=None, month=None)`
- Searches for visits by date criteria
- Supports flexible date filtering
- Returns list of matching visits

#### `findPatientsWhoNeedFollowUp(patients)`
- Identifies patients requiring follow-up care
- Based on predefined medical criteria
- Returns list of patient IDs

#### `deleteAllVisitsOfPatient(patients, patientId, filename)`
- Removes all visits for specified patient
- Updates both memory and file storage

## Error Handling

The system includes robust error handling for:

### File Operations
- Missing data files
- File read/write permissions
- Corrupted data format

### Data Validation
- Invalid data types
- Out-of-range vital signs
- Malformed dates
- Missing required fields

### User Input
- Invalid menu selections
- Type conversion errors
- Empty or null inputs

### Runtime Errors
- Memory allocation issues
- Unexpected exceptions during data processing

## Medical Context

### Follow-up Criteria
The system uses medically relevant thresholds to identify patients needing follow-up:
- **Bradycardia/Tachycardia**: Heart rate outside 60-100 bpm range
- **Hypertension**: Systolic blood pressure > 140 mmHg
- **Hypoxemia**: Oxygen saturation < 90%

These criteria are based on standard medical guidelines for identifying potentially concerning vital signs.

## Data Security & Privacy

### Recommendations
- Store patient data files in secure, encrypted directories
- Implement proper access controls for healthcare staff
- Regular backups of patient data
- Compliance with healthcare data protection regulations (HIPAA, GDPR)

## Future Enhancements

### Potential Features
- **Database Integration**: Migrate from file-based to database storage
- **Graphical User Interface**: Develop GUI for easier use
- **Advanced Analytics**: Trend analysis and predictive modeling
- **Export Capabilities**: Generate reports in PDF/Excel formats
- **Multi-user Support**: Role-based access control
- **Data Visualization**: Charts and graphs for vital signs trends

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 Python style guidelines
- Include comprehensive error handling
- Add comments for complex logic
- Maintain existing validation standards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue in the GitHub repository.

---

**Note**: This system is designed for educational and demonstration purposes. For production healthcare environments, additional security measures, compliance features, and professional medical validation would be required.
