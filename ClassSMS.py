class SMS:
    def __init__(self, name, DEP, session, sem, DoB, Roll_num):
        self.name = name
        self.DEP = DEP
        self.session = session
        self.sem = sem
        self.DoB = DoB
        self.Roll_num = Roll_num

    def display_student_info(self):
        print("Student Name:", self.name)
        print("Department:", self.DEP)
        print("Session:", self.session)
        print("Semester:", self.sem)
        print("Date of Birth:", self.DoB)
        print("Roll Number:", self.Roll_num)
        print()

    def to_dict(self):
        return {
            'Name': self.name,
            'DEP': self.DEP,
            'Session': self.session,
            'Semester': self.sem,
            'DOB': self.DoB,
            'Roll_num': self.Roll_num
        }

    @staticmethod
    def from_dict(data):
        return SMS(
            data['Name'],
            data['DEP'],
            data['Session'],
            data['Semester'],
            data['DOB'],
            data['Roll_num']
        )
        