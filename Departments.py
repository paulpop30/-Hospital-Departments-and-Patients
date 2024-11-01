from Patients import Patient
class Department:
    def __init__(self, id, name, num_beds, patients=[]):
        self._id = id
        self._name = name
        self._num_beds = num_beds
        self._patients = patients or []
#getters
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_num_beds(self):
        return self._num_beds

    def get_patients(self):
        return self._patients
#setters
    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_num_beds(self, num_beds):
        self._num_beds = num_beds

    def set_patients(self, patients):
        self._patients = patients

    def add_patient(self, first_name, last_name, personal_code, disease, age):   #this function add a patient in a department if there's a free place
        patient = Patient(first_name, last_name, personal_code, disease, age)     #input: first_name,last_name, personal_code, disease, age of the patient
                                                                                    #output: True if the patient was added to the department and False otherwise
        if len(self._patients) < self._num_beds:
            self._patients.append(patient)
            return True  # Patient added successfully
        else:
            print("No available beds in the department.")
            return False  # Patient not added due to no available beds

    def update_free_beds(self):                          #this function update the number of free beds of a department at each patient added in that department
        self._num_beds -= len(self._patients)            #input:none, output:none

    def sort_patients_by_personal_code(self):                                   # this function sort patients in a department by their personal numeric code
        return sorted(self._patients, key=lambda x: int(x.get_personal_code()))  #input:none
                                                                                 #output:returns a sorted list of patients from a department
    def get_num_patients(self):           #this function give the number of patients from a department
        return len(self._patients)        #input:none , output: the number of patients from a department

    def sort_by_patients_above_age(self, age_limit):                           # this function sort departments by the number of their patients having age above a given limit
        return sorted(self._patients, key=lambda x: x.get_age() > age_limit)   #input:age_limit which is the given limit
                                                                                #output: a list of the departments sorted as it was said before
    def sort_by_num_patients_alphabetically(self):                                                                                         #this funcion sort the departments by the number of patients and the patients alph in each department
        return sorted(self._patients, key=lambda x: (len(x.get_first_name() + x.get_last_name()), x.get_first_name(), x.get_last_name()))  #input:none , output: a list of the departments sorted as it was said above

    def get_patients_below_age(self, age_limit):                  #this function get the patients which have the age below a age limit
        return [patient for patient in self._patients if patient.get_age() < age_limit]    #input:none
                                                                                        #output:a list with the patients whicj respect the condition above

    def get_patients_with_first_name(self, first_name):                    # this function get the patients with the first name equal to a given string
        return [patient for patient in self._patients if patient.get_first_name().lower() == first_name.lower()]  #input: first_name which is the string given
                                                                                                                    #output: alist with the patients which respect the condition above


