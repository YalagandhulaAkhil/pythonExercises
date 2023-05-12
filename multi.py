class teacher:
    def  teachers_action(self):
        print("i can teach")

class student:
    def students_action(self):
        print("i study")

class youtuber:
    def youtubers_action(self):
        print("i study and teach")

class person(teacher, student, youtuber):
    pass

coder = person()
coder.teachers_action()
coder.students_action()
coder.youtubers_action()


        
