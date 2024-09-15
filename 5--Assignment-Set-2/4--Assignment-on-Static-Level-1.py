# Assignment 2
# Assignment on Static - Level 1

class Classroom:
    classroom_list=[]
    
    @staticmethod
    def search_classroom(class_room):
        if class_room.lower() in [i.lower() for i in Classroom.classroom_list]:
            return "Found"
        else:
            return -1

