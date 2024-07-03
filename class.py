class SMS:
    def __init__(self, name, dep, session, sem, dob, roll_num):
        self.name = name
        self.dep = dep
        self.session = session
        self.sem = sem
        self.dob = dob
        self.roll_num = roll_num

    def display_student_info(self):
        print("Student Name:", self.name)
        print("department:", self.dep)
        print("Session:", self.session)
        print("Semester:", self.sem)
        print("Date of Birth:", self.dob)
        print("Roll Number:", self.roll_num)
        print()

    