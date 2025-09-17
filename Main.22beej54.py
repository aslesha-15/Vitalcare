from typing import List, Dict, Optional
from datetime import datetime

def readPatientsFromFile(fileName):
    patients = {}
    try:
        with open(fileName, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split(',')
                if len(parts) != 8:
                    print(f"Invalid number of fields ({len(parts)}) in line: {line_number}")
                    continue
                try:
                    patient_id = int(parts[0])
                    visit_date = parts[1]
                    temperature = float(parts[2])
                    heart_rate = int(parts[3])
                    respiratory_rate = int(parts[4])
                    systolic_bp = int(parts[5])
                    diastolic_bp = int(parts[6])
                    oxygen_saturation = int(parts[7])

                    if not (35 <= temperature <= 42):
                        print(f"Invalid temperature value ({temperature}) in line: {line_number}")
                        continue
                    if not (30 <= heart_rate <= 180):
                        print(f"Invalid heart rate value ({heart_rate}) in line: {line_number}")
                        continue
                    if not (5 <= respiratory_rate <= 40):
                        print(f"Invalid respiratory rate value ({respiratory_rate}) in line: {line_number}")
                        continue
                    if not (70 <= systolic_bp <= 200):
                        print(f"Invalid systolic blood pressure value ({systolic_bp}) in line: {line_number}")
                        continue
                    if not (40 <= diastolic_bp <= 120):
                        print(f"Invalid diastolic blood pressure value ({diastolic_bp}) in line: {line_number}")
                        continue
                    if not (70 <= oxygen_saturation <= 100):
                        print(f"Invalid oxygen saturation value ({oxygen_saturation}) in line: {line_number}")
                        continue

                    if patient_id in patients:
                        patients[patient_id].append([visit_date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation])
                    else:
                        patients[patient_id] = [[visit_date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation]]
                except ValueError:
                    print(f"Invalid data type in line: {line_number}")
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    return patients

def displayPatientsAsDictionary(patients):
    patients_dict = {}
    for patient_id, visits in patients.items():
        visits_list = []
        for visit in visits:
            visit_date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation = visit
            visit_data = [visit_date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation]
            visits_list.append(visit_data)
        patients_dict[patient_id] = visits_list
    print(patients_dict)

def displayPatientData(patients, patientId=0):
    if patientId == 0:
        for patient_id, visits in patients.items():
            print(f"Patient ID: {patient_id}")
            for visit in visits:
                print(f"Date: {visit[0]}")
                print(f"Temperature: {visit[1]}")
                print(f"Heart Rate: {visit[2]}")
                print(f"Respiratory Rate: {visit[3]}")
                print(f"Systolic Blood Pressure: {visit[4]}")
                print(f"Diastolic Blood Pressure: {visit[5]}")
                print(f"Oxygen Saturation: {visit[6]}")
                print("-" * 30)
    elif patientId in patients:
        visits = patients[patientId]
        print(f"Patient ID: {patientId}")
        for visit in visits:
            print(f"Date: {visit[0]}")
            print(f"Temperature: {visit[1]}")
            print(f"Heart Rate: {visit[2]}")
            print(f"Respiratory Rate: {visit[3]}")
            print(f"Systolic Blood Pressure: {visit[4]}")
            print(f"Diastolic Blood Pressure: {visit[5]}")
            print(f"Oxygen Saturation: {visit[6]}")
            print("-" * 30)
    else:
        print(f"Patient ID {patientId} not found.")

def displayStats(patients, patientId=0):
    try:
        patientId = int(patientId)
    except ValueError:
        print("Invalid patient ID. Please enter a valid integer.")
        return
    if not isinstance(patientId, int):
        print("Error: 'patientId' should be an integer.")
        return
    if not isinstance(patients, dict):
        print("Error: 'patients' should be a dictionary.")
        return
    if patientId == 0:
        if not patients:
            print("No data found for any patients.")
            return
        num_patients = len(patients)
        temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = 0
        num_visits = 0
        for patient_visits in patients.values():
            num_visits += len(patient_visits)
            for visit in patient_visits:
                temp_sum += visit[1]
                hr_sum += visit[2]
                rr_sum += visit[3]
                sbp_sum += visit[4]
                dbp_sum += visit[5]
                spo2_sum += visit[6]
        avg_temp = temp_sum / num_visits
        avg_hr = hr_sum / num_visits
        avg_rr = rr_sum / num_visits
        avg_sbp = sbp_sum / num_visits
        avg_dbp = dbp_sum / num_visits
        avg_spo2 = spo2_sum / num_visits
        print("Vital Signs for All Patients:")
        print("  Average temperature:", "%.2f" % avg_temp, "C")
        print("  Average heart rate:", "%.2f" % avg_hr, "bpm")
        print("  Average respiratory rate:", "%.2f" % avg_rr, "bpm")
        print("  Average systolic blood pressure:", "%.2f" % avg_sbp, "mmHg")
        print("  Average diastolic blood pressure:", "%.2f" % avg_dbp, "mmHg")
        print("  Average oxygen saturation:", "%.2f" % avg_spo2, "%")
    elif patientId > 0:
        if patientId not in patients:
            print(f"No data found for patient with ID {patientId}.")
            return
        patient_visits = patients[patientId]
        num_visits = len(patient_visits)
        temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = 0
        for visit in patient_visits:
            temp_sum += visit[1]
            hr_sum += visit[2]
            rr_sum += visit[3]
            sbp_sum += visit[4]
            dbp_sum += visit[5]
            spo2_sum += visit[6]
        avg_temp = temp_sum / num_visits
        avg_hr = hr_sum / num_visits
        avg_rr = rr_sum / num_visits
        avg_sbp = sbp_sum / num_visits
        avg_dbp = dbp_sum / num_visits
        avg_spo2 = spo2_sum / num_visits
        print(f"Vital Signs for Patient {patientId}:")
        print("  Average temperature:", "%.2f" % avg_temp, "C")
        print("  Average heart rate:", "%.2f" % avg_hr, "bpm")
        print("  Average respiratory rate:", "%.2f" % avg_rr, "bpm")
        print("  Average systolic blood pressure:", "%.2f" % avg_sbp, "mmHg")
        print("  Average diastolic blood pressure:", "%.2f" % avg_dbp, "mmHg")
        print("  Average oxygen saturation:", "%.2f" % avg_spo2, "%")
    else:
        print("Error: 'patientId' should be a positive integer.")

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    try:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
            return
        year, month, day = map(int, date.split('-'))
        if month < 1 or month > 12 or day < 1 or day > 31:
            print("Invalid date. Please enter a valid date.")
            return
        if not (35.0 <= temp <= 42.0):
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return
        if not (30 <= hr <= 180):
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
            return
        if not (5 <= rr <= 40):
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return
        if not (70 <= sbp <= 200):
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return
        if not (40 <= dbp <= 120):
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
            return
        if not (70 <= spo2 <= 100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return
        new_visit = [date, temp, hr, rr, sbp, dbp, spo2]
        if patientId in patients:
            patients[patientId].append(new_visit)
        else:
            patients[patientId] = [new_visit]
        with open(fileName, 'a') as file:
            file.write(f"\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}")
        print(f"Visit is saved successfully for Patient #{patientId}")
    except Exception:
        print("An unexpected error occurred while adding new data.")

def findVisitsByDate(patients, year=None, month=None):
    visits = []
    for patient_id, patient_visits in patients.items():
        for visit in patient_visits:
            visit_date = visit[0]
            visit_year, visit_month, _ = visit_date.split('-')
            if (year is None or year == int(visit_year)) and (month is None or month == int(visit_month)):
                visits.append((patient_id, visit))
    return visits

def findPatientsWhoNeedFollowUp(patients):
    followup_patients = []
    for patient_id, visits in patients.items():
        followup_needed = False
        for visit in visits:
            try:
                _, _, hr, _, sbp, _, spo2 = visit
                if (
                    int(hr) > 100 or int(hr) < 60 or
                    int(sbp) > 140 or int(spo2) < 90
                ):
                    followup_needed = True
                    break
            except ValueError:
                print(f"Error converting vital sign values for patient {patient_id}")
                continue
        if followup_needed:
            followup_patients.append(patient_id)
    return followup_patients

def deleteAllVisitsOfPatient(patients, patientId, filename):
    if patientId in patients:
        patients[patientId] = []
        with open(filename, 'w') as file:
            for patient, visits in patients.items():
                file.write(f"{patient} : {visits}\n")
        print(f"All visits of patient {patientId} deleted and data saved to {filename}")
    else:
        print(f"Patient {patientId} not found in the data.")

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()