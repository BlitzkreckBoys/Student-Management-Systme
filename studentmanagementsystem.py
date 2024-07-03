import sqlite3

from sqlite3 import Error



class StudentManagementSystem:
    """
    Student Management System
    """
    def __init__(self):
        self.conn = self.create_connection('database.db')
        self.create_table()

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite database '{db_file}'")
        except KeyError as e:
            print(e)
        return conn

    def create_table(self):
        """ create students table """
        sql_create_students_table = """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                dep TEXT NOT NULL,
                Session TEXT NOT NULL,
                semester INTEGER NOT NULL,
                dob TEXT NOT NULL,
                roll_num INTEGER NOT NULL
            );
        """
        try:
            c = self.conn.cursor()
            c.execute(sql_create_students_table)
        except Error as e:
            print(e)

    def create(self):
        """Create a new student record"""
        print("Enter student details > ")

        while True:
            name = input("Enter student's name: ")
            if not name.isalpha():
                print("Invalid input. Name should only contain alphabetic characters.")
                continue
            dep = input("Enter student's department: ")
            session = input("Enter student's session: ")
            sem = input("Enter student's semester: ")
            dob = input("Enter student's date of birth (YYYY-MM-DD): ")
            roll_num = input("Enter student's roll number: ")

            student_data = (name, dep, session, sem,dob, roll_num)
            sql = ''' INSERT INTO students(name, dep,session,semester,dob,roll_num)
                    VALUES(?,?,?,?,?,?) '''
            try:
                cur = self.conn.cursor()
                cur.execute(sql, student_data)
                self.conn.commit()
                print('Student added successfully!')
            except Error as e:
                print(e)
            break
    def retrieve(self):
        """Retrieve student details"""
        
        roll_nu = input("Enter roll_num: ")
        
        sql = ''' SELECT * FROM students where roll_num = ?'''
        
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (roll_nu,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(e)    
            
    def update(self):
        """Update student details"""
        
        roll_nu = input("Enter roll_num: ")
        name = input("Enter Updated Name: ")
        sql = ''' UPDATE  students SET name = ? WHERE roll_num = ?'''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (name, roll_nu))
            self.conn.commit()
            print('Student updated successfully!')
        except Error as e:     
            print(e)
    
    def delete(self):
        """Delete students"""
        
        roll_nu = input("Enter roll_num: ")
        sql = ''' DELETE FROM students WHERE roll_num =?'''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (roll_nu,))
            self.conn.commit()
            print('Student deleted successfully!')
        except Error as e:
            print(e)
        
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
                select = int(input("please enter appropriate option: "))

            except ValueError:
                print("Invalid input. Please enter a valid number.")

            if select == 1:
                sms.create()
            elif select == 2:
                sms.retrieve()
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
