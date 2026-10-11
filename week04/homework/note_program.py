import hashlib
import json
import os

DOSYA_YOLU = os.path.dirname(os.path.abspath(__file__))

STUDENT_FILE = os.path.join(DOSYA_YOLU, "students.json")
TEACHER_FILE = os.path.join(DOSYA_YOLU, "teachers.json")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_data(file_name, default_data):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(default_data, file, indent=4, ensure_ascii=False)
        return default_data

def save_data(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

default_students = {
    "1000000001": {"full_name": "Ahmet Yilmaz", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000002": {"full_name": "Ayse Kaya", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000003": {"full_name": "Mehmet Demir", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000004": {"full_name": "Fatma Sahin", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000005": {"full_name": "Mustafa Celik", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000006": {"full_name": "Zeynep Yildiz", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000007": {"full_name": "Ali Ozturk", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000008": {"full_name": "Elif Aydin", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000009": {"full_name": "Hasan Ozdemir", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0},
    "1000000010": {"full_name": "Merve Arslan", "midterm": None, "final": None, "unexcused_absence": 0, "excused_absence": 0}
}

class SchoolSystem:
    def __init__(self):
        self.teachers = load_data(TEACHER_FILE, {})
        self.students = load_data(STUDENT_FILE, default_students)
        self.active_teacher = None

    def main_login_screen(self):
        while True:
            clear_screen()
            print("=== TEACHER GRADE & ABSENCE MANAGEMENT SYSTEM ===")
            print("1. Login")
            print("2. Create Account")
            print("3. Exit")
            choice = input("Your choice: ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                print("Exiting the system...")
                break
            else:
                input("Invalid choice! Press Enter to continue...")

    def create_account(self):
        username = input("New Username: ")
        if username in self.teachers:
            input("This username already exists! Press Enter to continue...")
            return
        
        password = input("Password: ")
        self.teachers[username] = hash_password(password)
        save_data(TEACHER_FILE, self.teachers)
        input("Account created successfully! You can now login. Press Enter to continue...")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        
        if username in self.teachers and self.teachers[username] == hash_password(password):
            self.active_teacher = username
            self.teacher_panel()
        else:
            input("Invalid username or password! Press Enter to continue...")

    def teacher_panel(self):
        while True:
            clear_screen()
            print(f"Welcome, Teacher {self.active_teacher}")
            print("-" * 50)
            print("SYSTEM INFO:")
            print("* Passing Grade: 40% of Midterm + 60% of Final > 60.")
            print("* Absence Limit: 4 days (Unexcused). Excused days do not count.")
            print("-" * 50)
            print("1. Enter Absence (Unexcused / Excused)")
            print("2. Enter Midterm Grade")
            print("3. Enter Final Grade")
            print("4. Add New Student")
            print("5. View Student Statuses")
            print("6. Logout")
            
            choice = input("\nSelect an action: ")

            if choice == '1':
                self.enter_absence()
            elif choice == '2':
                self.enter_grade("midterm")
            elif choice == '3':
                self.enter_grade("final")
            elif choice == '4':
                self.add_student()
            elif choice == '5':
                self.show_statuses()
            elif choice == '6':
                self.active_teacher = None
                break
            else:
                input("Invalid action. Press Enter to continue...")

    def show_student_list(self):
        print(f"\n{'ID':<12} | {'Full Name'}")
        print("-" * 35)
        for student_id, data in self.students.items():
            print(f"{student_id:<12} | {data['full_name']}")
        print("-" * 35)

    def enter_absence(self):
        clear_screen()
        print("=== ENTER ABSENCE ===")
        self.show_student_list() 
        
        student_id = input("\nStudent ID (10 digits): ")
        if student_id in self.students:
            print("1. Add Unexcused Absence")
            print("2. Add Excused Absence (Medical Report)")
            choice = input("Choice: ")
            
            try:
                days = int(input("How many days to add: "))
                if choice == '1':
                    self.students[student_id]["unexcused_absence"] += days
                elif choice == '2':
                    self.students[student_id]["excused_absence"] += days
                else:
                    print("Invalid choice!")
                    
                save_data(STUDENT_FILE, self.students)
                input("Absence recorded successfully! Press Enter to continue...")
            except ValueError:
                input("Please enter a valid number! Press Enter to continue...")
        else:
            input("Student not found! Press Enter to continue...")

    def enter_grade(self, exam_type):
        clear_screen()
        print(f"=== ENTER {exam_type.upper()} GRADE ===")
        self.show_student_list() # LİSTE BURADA DA ÇAĞRILIYOR
        
        student_id = input("\nStudent ID (10 digits): ")
        if student_id in self.students:
            try:
                score = float(input(f"Enter {exam_type.capitalize()} Grade (0-100): "))
                if 0 <= score <= 100:
                    self.students[student_id][exam_type] = score
                    save_data(STUDENT_FILE, self.students)
                    input("Grade recorded successfully! Press Enter to continue...")
                else:
                    input("Grade must be between 0 and 100! Press Enter to continue...")
            except ValueError:
                input("Please enter a valid number! Press Enter to continue...")
        else:
            input("Student not found! Press Enter to continue...")

    def add_student(self):
        student_id = input("New Student ID (10 digits): ")
        if len(student_id) != 10 or not student_id.isdigit():
            input("Error: Student ID must consist of exactly 10 digits! Press Enter to continue...")
            return
            
        if student_id in self.students:
            input("Error: A student with this ID already exists! Press Enter to continue...")
            return

        full_name = input("Student's Full Name: ")
        
        self.students[student_id] = {
            "full_name": full_name,
            "midterm": None,
            "final": None,
            "unexcused_absence": 0,
            "excused_absence": 0
        }
        save_data(STUDENT_FILE, self.students)
        input("Student added successfully! Press Enter to continue...")

    def show_statuses(self):
        clear_screen()
        print(f"{'ID':<12} | {'Full Name':<15} | {'Mid.':<5} | {'Fin.':<5} | {'Unexcused':<9} | {'Excused':<7} | {'Avg.':<6} | {'Status'}")
        print("-" * 95)
        
        for student_id, data in self.students.items():
            midterm = data['midterm']
            final = data['final']
            unexcused = data['unexcused_absence']
            excused = data['excused_absence']
            
            midterm_display = midterm if midterm is not None else "-"
            final_display = final if final is not None else "-"
            
            average = "-"
            status = ""

            if unexcused > 4:
                status = "FAILED (Absence)"
                if midterm is not None and final is not None:
                    average = round((midterm * 0.4) + (final * 0.6), 2)
            elif midterm is not None and final is not None:
                average = round((midterm * 0.4) + (final * 0.6), 2)
                if average > 60:
                    status = "PASSED"
                else:
                    status = "FAILED (Low Grade)"
            else:
                status = "Missing Grades"

            print(f"{student_id:<12} | {data['full_name']:<15} | {midterm_display:<5} | {final_display:<5} | {unexcused:<9} | {excused:<7} | {average:<6} | {status}")
            
        print("-" * 95)
        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    system = SchoolSystem()
    system.main_login_screen()