from ClassSMS import SMS
import csv


class StudentManagementSystem:
    
    def __init__(self):
        self.students = []

    def create(self):
        print("Enter student details > ")

        while True:
            name = input("Enter student's name: ")
            if not name.isalpha():
                print("Invalid input. Name should only contain alphabetic characters.")
                continue
            DEP = input("Enter student's department: ")
            session = input("Enter student's session: ")
            sem = input("Enter student's semester: ")
            DoB = input("Enter student's date of birth (YYYY-MM-DD): ")
            Roll_num = input("Enter student's roll number: ")

            st = SMS(name, DEP, session, sem, DoB, Roll_num)

            self.students.append(st)

            break
        print("Student added successfully!")

        self.save_student(st)

    
    def retreive(self):
        roll_num = input("Enter roll_num: ")
        for student in self.students:
            if student.Roll_num == roll_num:
                print("Student Details:")
                student.display_student_info()
                return
        print("Student not found.")

    def update(self):
        roll_num = (input("Enter roll number to update: "))
        for student in self.students:
            if student.Roll_num == roll_num:
                print("Enter updated student details:")
                student.name = input("Enter updated student's name: ")

                print("Student updated successfully!")
                return

        print("Student not found.")
       # self.save_student(student)

    def delete(self):
        roll_num = (input("enter roll_num:"))
        for student in self.students:
            if student.Roll_num == roll_num:
                self.students.remove(student)
                print("Student Deleted Successfully!")
            else:
                print("Student not found.")
                break
        #self.load_student(st)
    def save_student(self, st):
        f = open(r'/home/sam/Documents/PROJECT/student.csv', 'a')
        ro = csv.DictWriter(f, delimiter=',', fieldnames=["Name", "DEP","Session", "Semester", "DOB", "Roll_num"])
        ro.writerow(st.to_dict())

        f.close()
    def load_students(self):
        students = []
        try:
            f = open(self.filename, mode='r', newline='', encoding='utf-8')
            reader = csv.DictReader(f)
            for row in reader:
                students.append(SMS.from_dict(row))
            f.close()
        except FileNotFoundError:
            pass  # If the file does not exist, start with an empty list of students
        return students
    

    def choose_operation(self):
        """
        Choose operations to perform
        """
        while True:
            print("\nChoose an operation:")
            print("1. Create a new student")
            print("2. Retrieve student details")
            print("3. Update student details")
            print("4. Delete a student")
            print("5. Exit")

            try:
                select = int(input("Enter your Select: "))

            except ValueError:
                print("Invalid input. Please enter a valid number.")

            if select == 1:
                sms.create()
            elif select == 2:
                sms.retreive()
            elif select == 3:
                sms.update()
            elif select == 4:
                sms.delete()
            elif select == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


sms = StudentManagementSystem()
sms.choose_operation()
# sms.Create()
# sms.Retreive()
# sms.Update()
# sms.Delete()
# self, name, DP, session, sem, DOB, Roll_num
