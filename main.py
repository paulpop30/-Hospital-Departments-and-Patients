from Hospital import Hospital
from Departments import Department
from Patients import Patient
def print_departments(hospital):   #this function print on the screen the informations about the each department
    departments = hospital.get_all_departments()
    for department in departments:
        print(f"Department {department.get_id()}: {department.get_name()}, Beds: {department.get_num_beds()}")
        for patient in department.get_patients():
            print(f"  - Patient: {patient.get_first_name()} {patient.get_last_name()}, Code: {patient.get_personal_code()}, Disease: {patient.get_disease()}, Age: {patient.get_age()}")
#those three functions are the assertions functions for each functions from each class
def test_hospital_functions():
    hospital = Hospital()

    # Test add_department function
    department1 = hospital.add_department(1, "Cardiology", 20)
    assert len(hospital.get_departments()) == 1
    assert department1.get_name() == "Cardiology"
    assert department1.get_num_beds() == 20

    # Test get_department_by_id function
    retrieved_department = hospital.get_department_by_id(1)
    assert retrieved_department.get_id() == 1
    assert retrieved_department.get_name() == "Cardiology"

    # Test add_patient_to_department function
    hospital.add_patient_to_department(1, "John", "Doe", "123456789", "Heart Disease", 45)
    department1 = hospital.get_department_by_id(1)
    assert department1.get_num_patients() == 1

    # Test sort_departments_by_num_patients function
    department2 = hospital.add_department(2, "Orthopedics", 15)
    department3 = hospital.add_department(3, "Pediatrics", 10)

    hospital.add_patient_to_department(2, "Bob", "Johnson", "345678912", "Fracture", 30)
    hospital.add_patient_to_department(2, "Alice", "Williams", "789123456", "Sprain", 25)
    hospital.add_patient_to_department(3, "Charlie", "Brown", "567891234", "Common Cold", 40)

    sorted_departments = hospital.sort_departments_by_num_patients()
    assert len(sorted_departments) == 3
    assert sorted_departments[0].get_id() == 1
    assert sorted_departments[2].get_id() == 2

    # Test get_departments_with_patients_with_first_name function
    departments_with_name = hospital.get_departments_with_patients_with_first_name("John")
    assert len(departments_with_name) == 1
    assert departments_with_name[0].get_name() == "Cardiology"

    # Test sort_departments_by_num_patients_above_age function
    sorted_departments_above_age = hospital.sort_departments_by_num_patients_above_age(35)
    assert len(sorted_departments_above_age) == 3
    assert sorted_departments_above_age[0].get_id() == 2
    assert sorted_departments_above_age[2].get_id() == 3

    # Test sort_departments_and_patients_alphabetically function
    sorted_departments_alphabetically = hospital.sort_departments_and_patients_alphabetically()
    assert len(sorted_departments_alphabetically) == 3
    assert sorted_departments_alphabetically[0].get_id() == 1
    assert sorted_departments_alphabetically[2].get_id() == 2  # Cardiology has the most number of patients

    # Test get_patients_with_name_string_in_department function
    matching_patients = hospital.get_patients_with_name_string_in_department(2, "Wi")
    assert len(matching_patients) == 1
    assert matching_patients[0].get_first_name() == "Alice"

    # Test get_departments_with_patients_with_first_name function
    departments_with_name = hospital.get_departments_with_patients_with_first_name("John")
    assert len(departments_with_name) == 1
    assert departments_with_name[0].get_name() == "Cardiology"

    # Test sort_departments_by_num_patients_above_age function
    sorted_departments_above_age = hospital.sort_departments_by_num_patients_above_age(35)
    assert len(sorted_departments_above_age) == 3
    assert sorted_departments_above_age[0].get_id() == 2
    assert sorted_departments_above_age[2].get_id() == 3

    # Test sort_departments_and_patients_alphabetically function
    sorted_departments_alphabetically = hospital.sort_departments_and_patients_alphabetically()
    assert len(sorted_departments_alphabetically) == 3
    assert sorted_departments_alphabetically[0].get_id() == 1
    assert sorted_departments_alphabetically[2].get_id() == 2  # Cardiology has the most number of patients
    # Test form_patient_groups_in_department function
    patient_groups = hospital.form_patient_groups_in_department(1, "Heart Disease", 2)
    assert len(patient_groups) == 0

    # Test form_department_groups_with_max_patients function
    department_groups = hospital.form_department_groups_with_max_patients(2, 1)
    assert len(department_groups) == 3
    assert len(department_groups[0]) == 2
    assert department_groups[0][0].get_name() == "Cardiology"
    assert department_groups[0][1].get_name() == "Orthopedics"
    department = hospital.add_department(1, "Cardiology", 2)
    patients = [
        Patient("John", "Doe", "123456789", "Heart Disease", 45),
        Patient("Jane", "Smith", "987654321", "Heart Disease", 55),
    ]
    groups = []
    hospital._backtrack_patient_groups_in_department(patients, 2, [], groups)
    assert len(groups) == 2
    assert len(groups[0]) == 2
    assert groups[0][0].get_first_name() == "John"
    assert groups[0][1].get_first_name() == "Jane"

    # Test _validate_department_group_with_max_patients function
    department1 = hospital.add_department(1, "Cardiology", 2)
    department2 = hospital.add_department(2, "Orthopedics", 2)
    department3 = hospital.add_department(3, "Pediatrics", 2)

    patients1 = [
        Patient("John", "Doe", "123456789", "Heart Disease", 45),
        Patient("Jane", "Smith", "987654321", "Heart Disease", 55),
    ]

    patients2 = [
        Patient("Bob", "Johnson", "345678912", "Fracture", 30),
        Patient("Alice", "Williams", "789123456", "Sprain", 25),
    ]

    patients3 = [
        Patient("Charlie", "Brown", "567891234", "Common Cold", 40),
        Patient("David", "Clark", "876543210", "Fever", 35),
    ]

    department1.set_patients(patients1)
    department2.set_patients(patients2)
    department3.set_patients(patients3)

    department_combination = [department1, department2, department3]
    valid_group, message = hospital._validate_department_group_with_max_patients(department_combination, 2)
    assert valid_group is not None
    assert message is None
    assert len(valid_group) == 3
    assert valid_group[0].get_name() == "Cardiology"
    assert valid_group[1].get_name() == "Orthopedics"
    assert valid_group[2].get_name() == "Pediatrics"

def test_department_functions():
    department = Department(1, "Cardiology", 20)

    # Test add_patient function
    patient_added = department.add_patient("John", "Doe", "123456789", "Heart Disease", 45)
    assert patient_added is True
    assert len(department.get_patients()) == 1

    # Test update_free_beds function
    department.update_free_beds()
    assert department.get_num_beds() == 19

    # Test sort_patients_by_personal_code function
    department.add_patient("Jane", "Smith", "987654321", "High Blood Pressure", 55)
    department.add_patient("Bob", "Johnson", "345678912", "Fracture", 30)
    sorted_patients = department.sort_patients_by_personal_code()
    assert len(sorted_patients) == 3
    assert sorted_patients[0].get_personal_code() == "123456789"
    assert sorted_patients[2].get_personal_code() == "987654321"

    # Test sort_by_patients_above_age function
    sorted_patients_above_age = department.sort_by_patients_above_age(35)
    assert len(sorted_patients_above_age) == 3
    assert sorted_patients_above_age[0].get_age() == 30
    assert sorted_patients_above_age[1].get_age() == 45

    # Test sort_by_num_patients_alphabetically function
    sorted_patients_alphabetically = department.sort_by_num_patients_alphabetically()
    assert len(sorted_patients_alphabetically) == 3
    assert sorted_patients_alphabetically[0].get_first_name() == "John"
    assert sorted_patients_alphabetically[2].get_first_name() == "Bob"

def test_patient_functions():
    patient = Patient("John", "Doe", "123456789", "Heart Disease", 45)

    # Test set_age function
    patient.set_age(50)
    assert patient.get_age() == 50

    # Test contains_string function
    assert patient.contains_string("John") is True
    assert patient.contains_string("Smith") is False
    assert patient.contains_string("DOE") is True  # Case-insensitive check

    # Test get_disease function
    assert patient.get_disease() == "Heart Disease"

    # Test get_last_name function
    assert patient.get_last_name() == "Doe"
    patient = Patient("Bob", "Johnson", "345678912", "Fracture", 30)

    # Test set_age function
    patient.set_age(34)
    assert patient.get_age() == 34

    # Test contains_string function
    assert patient.contains_string("Bob") is True
    assert patient.contains_string("Smith") is False
    assert patient.contains_string("Johnson") is True  # Case-insensitive check

    # Test get_disease function
    assert patient.get_disease() == "Fracture"

    # Test get_last_name function
    assert patient.get_last_name() == "Johnson"

def main():
    hospital = Hospital()
    department1 = hospital.add_department(1, "Cardiology", 20)
    department2 = hospital.add_department(2, "Orthopedics", 15)
    department3 = hospital.add_department(3, "Pediatrics", 10)

    # Predefined patients
    hospital.add_patient_to_department(1, "John", "Doe", "123456789", "Heart Disease", 45)
    hospital.add_patient_to_department(1, "Jane", "Smith", "987654321", "High Blood Pressure", 55)
    hospital.add_patient_to_department(2, "Bob", "Johnson", "345678912", "Fracture", 30)
    hospital.add_patient_to_department(2, "Alice", "Williams", "789123456", "Sprain", 25)
    hospital.add_patient_to_department(3, "Charlie", "Brown", "567891234", "Common Cold", 40)


    while True:
        print("\n1. Add Department")
        print("2. Add Patient")
        print("3. View Departments")
        print("4. Sort Patients by Personal Code")
        print("5. Sort Departments by Number of Patients")
        print("6. Sort Departments by Number of Patients Above Age Limit")
        print("7. Sort Departments by Number of Patients and Patients Alphabetically")
        print("8. Identify Departments with Patients Below Age Limit")
        print("9. Identify Departments with Patients with a Given First Name")
        print("10.Identify patients from a given department for which the first name or last name contain a given string")
        print("11. Form groups of 𝒌 patients from the same department and the same disease ")
        print("12.Form groups of 𝒌 departments having at most 𝒑 patients suffering from the same disease")

        choice = input("Enter your choice: ")

        if choice == "1":
            department_name = input("Enter department name: ")
            num_beds = input("Enter number of beds: ")
            try:
                num_beds = int(num_beds)
            except ValueError:
                print("Invalid input for number of beds.... Please enter a valid integer!!!")
                continue

            hospital.add_department(len(hospital.get_departments()) + 1, department_name, num_beds)
            print("Department added successfully!!!")

        elif choice == "2":
            department_id = input("Enter department ID: ")
            try:
                department_id = int(department_id)
            except ValueError:
                print("Invalid input for department ID... Please enter a valid integer!!!")
                continue

            if hospital.get_department_by_id(department_id) is None:
                print("Invalid department ID... Please choose a valid department!!!")
                continue

            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            personal_code = input("Enter patient's personal code: ")
            disease = input("Enter patient's disease: ")
            age = input("Enter patient's age: ")

            try:
                age = int(age)
            except ValueError:
                print("Invalid input for age... Please enter a valid integer!!!")
                continue

            hospital.add_patient_to_department(department_id, first_name, last_name, personal_code, disease, age)

        elif choice == "3":
            print_departments(hospital)

        elif choice == "4":
            department_id = input("Enter department ID: ")
            try:
                department_id = int(department_id)
            except ValueError:
                print("Invalid input for department ID... Please enter a valid integer!!!")
                continue

            department = hospital.get_department_by_id(department_id)
            if department:
                sorted_patients = department.sort_patients_by_personal_code()
                for patient in sorted_patients:
                    print(
                        f"Patient: {patient.get_first_name()} {patient.get_last_name()}, Personal Code: {patient.get_personal_code()}")
            else:
                print("Department not found")

        elif choice == "5":
            sorted_departments = hospital.sort_departments_by_num_patients()
            for department in sorted_departments:
                print(f"Department {department.get_id()}: {department.get_name()}, Number of Patients: {department.get_num_patients()}")

        elif choice == "6":
            try:
                age_limit = int(input("Enter age limit: "))
            except ValueError:
                print("Invalid input for age limit... Please enter a valid integer!!!")
                continue

            sorted_departments = hospital.sort_departments_by_num_patients_above_age(age_limit)
            for department in sorted_departments:
                print(
                    f"Department {department.get_id()}: {department.get_name()}, Number of Patients above {age_limit} Years: {sum(patient.get_age() > age_limit for patient in department.get_patients())}")

        elif choice == "7":
            sorted_departments = hospital.sort_departments_and_patients_alphabetically()
            for department in sorted_departments:
                print(
                    f"Department {department.get_id()}: {department.get_name()}, Number of Patients: {department.get_num_patients()}")
                for patient in department.get_patients():
                    print(
                        f"  - Patient: {patient.get_first_name()} {patient.get_last_name()}, Age: {patient.get_age()}")
        elif choice == "8":
            try:
                age_limit = int(input("Enter age limit: "))
            except ValueError:
                print("Invalid input for age limit... Please enter a valid integer!!!")
                continue

            for department in hospital.get_departments():
                patients_below_age = department.get_patients_below_age(age_limit)
                if patients_below_age:
                    print(
                        f"Department {department.get_id()}: {department.get_name()}, Patients Below {age_limit} Years:")
                    for patient in patients_below_age:
                        print(
                            f"  - Patient: {patient.get_first_name()} {patient.get_last_name()}, Age: {patient.get_age()}")
                else:
                    print(f"No patients below {age_limit} years in {department.get_name()}")


        elif choice == "9":
            search_name = input("Enter first name to search: ")
            departments_with_name = hospital.get_departments_with_patients_with_first_name(search_name)
            if departments_with_name:
                print(f"Departments with patients named {search_name}:")
                for department in departments_with_name:
                    print(f"  - Department {department.get_id()}: {department.get_name()}")
            else:
                print(f"No departments with patients named {search_name}")


        elif choice == "10":
            try:
                department_id = int(input("Enter department ID: "))
            except ValueError:
                print("Invalid input for department ID. Please enter a valid integer.")
                continue  # Continue to the next iteration of the loop

            search_name = input("Enter name string to search: ")

            matching_patients = hospital.get_patients_with_name_string_in_department(department_id, search_name)

            if matching_patients:
                print(f"Patients in Department {department_id} with names containing '{search_name}':")
                for patient in matching_patients:
                    print(
                        f"  - Patient: {patient.get_first_name()} {patient.get_last_name()}, Age: {patient.get_age()}")

            else:
                print(f"No patients in Department {department_id} with names containing '{search_name}'")

        elif choice == "11":
            try:
                k = int(input("Enter the value of k for patient groups: "))
            except ValueError:
                print("Invalid input for k... Please enter a valid integer!!!")
                continue

            department_id = int(input("Enter the department ID for grouping: "))
            disease = input("Enter the disease for grouping: ")

            department = hospital.get_department_by_id(department_id)
            if department is not None:
                matching_patients = [patient for patient in department.get_patients() if
                                     patient.get_disease().lower() == disease.lower()]
                if len(matching_patients) >= k:
                    patient_groups = hospital.form_patient_groups_in_department(department_id, disease, k)
                    for i, group in enumerate(patient_groups):
                        print(f"Group {i + 1} - Patients in Department {department_id} with Disease '{disease}':")
                        for patient in group:
                            print(f"  - {patient.get_first_name()} {patient.get_last_name()}, Age: {patient.get_age()}")
                else:
                    print(
                        f"Not enough patients in Department {department_id} with Disease '{disease}' to form a group of size {k}.")
            else:
                print(f"Department with ID {department_id} not found.")

        elif choice == "12":
            try:
                k = int(input("Enter the value of k for department groups: "))
                p = int(input("Enter the value of p for maximum patients per disease: "))
            except ValueError:
                print("Invalid input for k or p... Please enter valid integers!!!")
                continue

            department_groups = hospital.form_department_groups_with_max_patients(k, p)
            for i, group in enumerate(department_groups):
                print(f"Group {i + 1} - Departments with at most {p} patients suffering from the same disease:")
                for department in group:
                    print(
                        f"  - Department {department.get_id()}: {department.get_name()}, Number of Patients: {department.get_num_patients()}")
        else:
            print("Invalid choice. Please try again.")
test_hospital_functions()
test_department_functions()
test_patient_functions()
if __name__ == "__main__":
    main()


