class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None

    # Setter methods
    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def set_marks(self, marks):
        self.__marks = marks
    
    def set_age(self, age):
        self.__age = age

    def set_course_id(self, course_id):
        self.__course_id = course_id
    
    def set_fees(self, fees):
        self.__fees = fees

    # Getter methods
    def get_student_id(self):
        return self.__student_id
    
    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self.__age
    
    def get_course_id(self):
        return self.__course_id
    
    def get_fees(self):
        return self.__fees

    # Method to validate marks
    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        else:
            return False
    
    # Method to validate age
    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False
    
    # Method to check qualification
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False

    # Method to choose a course and apply discount based on marks
    def choose_course(self, course_id):
        courses = {
            1001: 25575.0,
            1002: 15500.0
        }

        if course_id in courses:
            self.set_course_id(course_id)
            self.set_fees(courses[course_id])

            if self.get_marks() > 85:
                discounted_fees = self.get_fees() * 0.75
                self.set_fees(discounted_fees)
            
            return True
        else:
            return False

# Example usage:
student = Student()
student.set_student_id("S12345")
student.set_age(22)
student.set_marks(90)

if student.check_qualification():
    student.choose_course(1001)
    print(f"Student {student.get_student_id()} qualifies for admission.")
    print(f"Course ID: {student.get_course_id()}")
    print(f"Fees after discount (if any): {student.get_fees()}")
else:
    print(f"Student {student.get_student_id()} does not qualify for admission.")


