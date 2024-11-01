class Patient:
    def __init__(self, first_name, last_name, personal_code, disease, age):
        self._first_name = first_name
        self._last_name = last_name
        self._personal_code = personal_code
        self._disease = disease
        self._age = age
#getters
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_personal_code(self):
        return self._personal_code

    def get_disease(self):
        return self._disease

    def get_age(self):
        return self._age
#setters
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_personal_code(self, personal_code):
        self._personal_code = personal_code

    def set_disease(self, disease):
        self._disease = disease

    def set_age(self, age):
        self._age = age

    def contains_string(self, search_string):
        return search_string.lower() in self._first_name.lower() or search_string.lower() in self._last_name.lower()

#search_string.lower(): Converts the search string to lowercase to make the comparison case-insensitive
#self._first_name.lower(): Converts the patient's first name to lowercase
#self._last_name.lower(): Converts the patient's last name to lowercase
#... in ...: Checks if the lowercase search string is present in either the lowercase first name or the lowercase last name
#The function returns True if the search string is found in either the first name or last name , and False otherwise
