class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

    # Setter methods
    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def set_marks(self, marks):
        self.__marks = marks
    
    def set_age(self, age):
        self.__age = age

    # Getter methods
    def get_student_id(self):
        return self.__student_id
    
    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self.__age

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

# Example usage:
student = Student()
student.set_student_id("S12345")
student.set_age(22)
student.set_marks(70)

if student.check_qualification():
    print(f"Student {student.get_student_id()} qualifies for admission.")
else:
    print(f"Student {student.get_student_id()} does not qualify for admission.")


