from Departments import Department
from Patients import Patient
from itertools import combinations
import itertools
from collections import defaultdict
class Hospital:
    def __init__(self):
        self._departments = []

    def get_departments(self):   #getters
        return self._departments

    def add_department(self, department_id, department_name, num_beds):   # this function add new departments
        department = Department(department_id, department_name, num_beds)   #input: department_id, department_name, num_beds
        self._departments.append(department)                                #output: the department added
        return department

    def get_department_by_id(self, department_id):                               #this function get the department by id
        return next((dept for dept in self._departments if dept.get_id() == department_id), None)    #input: department_id the id given
                                                                                                    #output:  either the department object with the specified id or None if no department with that id is found
    def add_patient_to_department(self, department_id, first_name, last_name, personal_code, disease, age):    #this function add a patient in a department if there's a free place
        department = self.get_department_by_id(department_id)                                                  #input:department_id, first_name, last_name, personal_code, disease, age
        if department is None:                                                                                 #output: a suggestive message wjich say if he patient was added or not depending on the number of free beds in each department
            department = self.add_department(department_id, f"Department {department_id}", 0)

        patient_added = department.add_patient(first_name, last_name, personal_code, disease, age)

        if patient_added:
            print(f"Patient {first_name} {last_name} added to Department {department_id} successfully.")
            department.update_free_beds()
        else:
            print(f"Unable to add patient {first_name} {last_name} to Department {department_id}. No available beds.")

    def get_all_departments(self):  #getters
        return self._departments

    def sort_departments_by_num_patients(self):                                           #this function sort departments by the number of patients
        return sorted(self._departments, key=lambda x: x.get_num_patients())              #input:none, output: a list with departments sorted

    def get_departments_with_patients_with_first_name(self, first_name):                                                                                                #this function get departments which contains persons with the first name equal to a given name
        return [department for department in self._departments if any(patient.get_first_name().lower() == first_name.lower() for patient in department.get_patients())]  #first_name- the given name
                                                                                                                                                                            #output: a list with departments which hold the condition above
    def sort_departments_by_num_patients_above_age(self, age_limit):                               #this function sort departments by the number of patients with age above a given limit
        sorted_departments = sorted(self._departments, key=lambda x: (                              #input: age_limit the limit given
        sum(patient.get_age() > age_limit for patient in x.get_patients()), x.get_name()))           #output: a list with sorted departments
        return sorted_departments

    def sort_departments_and_patients_alphabetically(self):                                                              #this function sort departments by the number of patients and the patients in each department alph
        sorted_departments = sorted(self._departments, key=lambda x: (x.get_num_patients(), x.get_name()))              #input:none
                                                                                                                        #output: a list with the sorted departments

        for department in sorted_departments:
            department.set_patients(
                sorted(department.get_patients(),
                       key=lambda patient: (patient.get_first_name(), patient.get_last_name()))
            )

        return sorted_departments

    def get_patients_with_name_string_in_department(self, department_id, search_string):              #this function get the patients with the name equal to a string from a department with id given
        department = self.get_department_by_id(department_id)                                         #input: department_id the id of the department, search_string the name which is searched in the departments
                                                                                                      #output: a alist with the patients which name holds the condition if there's some in the department selected(found) or a a suggestive message instead
        if department:
            matching_patients = [patient for patient in department.get_patients() if
                                 patient.contains_string(search_string)]
            return matching_patients
        else:
            print("Department not found.")
            return []

    def form_patient_groups_in_department(self, department_id, disease, k):                     #this function form  groups with a number of(given)  patients with  the same disease(given) in a selected department
        department = self.get_department_by_id(department_id)                                   #input: department_id the id of the department, disease the disease given, k is the number of patients from a group
        if department is not None:                                                               #output: the groups constructed or a sugestive message otherwise(error or something)
            matching_patients = [patient for patient in department.get_patients() if patient.get_disease().lower() == disease.lower()]
            if len(matching_patients) >= k:
                groups = []
                self._backtrack_patient_groups_in_department(matching_patients, k, [], groups)
                return groups
            else:
                print(f"Not enough patients in Department {department_id} with Disease '{disease}' to form a group of size {k}.")
                return []
        else:
            print(f"Department with ID {department_id} not found.")
            return []



    def _backtrack_patient_groups_in_department(self, patients, k, current_group, groups):                  #this function backtrack patient groups in department
        if len(current_group) == k:                                                                         #input:patients, k, current_group, groups
            groups.append(current_group.copy())                                                             #output: the groups of departments formed
            return

        for i, patient in enumerate(patients):
            current_group.append(patient)
            remaining_patients = patients[:i] + patients[i + 1:]
            self._backtrack_patient_groups_in_department(remaining_patients, k, current_group, groups)
            current_group.pop()

    def form_department_groups_with_max_patients(self, k, p):                                                      #this function form groups of departments with max numb of patients with the same disease given
        department_combinations = combinations(self._departments, k)                                               #input: k is the number of departments in a group and p is the max number of patients with same disease
        valid_groups = []                                                                                          #output: the valid groups formed or a suggestive message otherwise

        for department_combination in department_combinations:
            valid_group, message = self._validate_department_group_with_max_patients(department_combination, p)
            if valid_group:
                valid_groups.append(valid_group)
            else:
                print(f"Cannot form a group with {k} departments and at most {p} patients per disease. {message}")

        return valid_groups

    def _validate_department_group_with_max_patients(self, department_combination, p):                     #this function verify if the number of patients from each department from a group goes over the limit or not and validate the formed groups
        patients_count_per_disease = defaultdict(int)                                                      #input:department_combination the groups of  departments formed  and p is the max numb of patients with the same disease2
                                                                                                        #output: the groups of departments which are valid or a suggestive message otherwise
        for department in department_combination:
            for patient in department.get_patients():
                patients_count_per_disease[patient.get_disease()] += 1

        for count in patients_count_per_disease.values():
            if count > p:
                return None, f"Exceeded the maximum patients per disease limit ({p})"

        return department_combination, None


