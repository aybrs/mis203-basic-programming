
#student informations
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
githup_username = input("Enter your GitHub username: ")
goal = input("Enter your programming goal: ")

#print the card
print("\n" + "-" * 45)
print("      STUDENT PROFILE CARD      ")
print(F"Name           : {name}")
print(f"Student ID     : {student_id}")
print(f"Department     : {department}")
print(f"GitHub         : @{github_username}")
print(f"Goal           : {goal}")
print("\n" + "-" * 45)
