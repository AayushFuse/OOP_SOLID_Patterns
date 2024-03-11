"""
Create a Python class to represent a University.
The university should have attributes like name, location, and a list of departments.
Implement encapsulation to protect the internal data of the University class. 
Create a Department class that inherits from the University class. 
The Department class should have attributes like department name, head of the department, and a list of courses offered. 
Implement polymorphism by defining a common method for both the University and Department classes to display their details. 
"""

class University:
    def __init__(self,uname,location):
        self.__uname = uname
        self.__location = location
        self.__departments = []

    

    @property
    def display_details(self):
        print("="*10)
        print(f"University Name: {self.__uname}\nLocation: {self.__location}\n")
        for department in self.__departments:
            department.display_details
        print("="*10)

    def add_department(self,department):
        self.__departments.append(department)
    
class Department(University):
    def __init__(self, dname, hod) -> None:
        self._dname = dname
        self._hod = hod
        self._courses = []
    
    
    def add_courses(self,course):
        self._courses.append(course)
    
    @property
    def display_details(self):
        print("="*10)
        print(f"Department Name: {self._dname}\nHOD: {self._hod}")
        for course in self._courses:
            print(course)
        print("="*10)




def main():
    pokharaUniversity = University("Pokhara University","Pokhara")
    pokharaUniversity.display_details
    comDep = Department("Computer Department","Madan Kadariya")
    comDep.add_courses(["Math","Physics","C"])
    comDep.display_details
    pokharaUniversity.add_department(comDep)
    pokharaUniversity.display_details
    



if __name__=="__main__":
    main()