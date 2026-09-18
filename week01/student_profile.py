import os

def clear_screen():
    # For Windows 'cls',For Mac/Linux  'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # 1. Step: Name
    clear_screen()
    name = input("Name: ").strip()

    # 2. Step: Department
    clear_screen()
    department = input("Department: ").strip()

    # 3. Step: Age
    clear_screen()
    age = input("Age: ").strip()

    # 4. Step: Career Goal
    clear_screen()
    career_goal = input("Career Goal: ").strip()

    # 5. Step: Clear screen and display output
    clear_screen()
    print("--- Student Profile ---")
    print(f"Name: {name}")
    print(f"Department: {department}")
    print(f"Age: {age}")
    print(f"Career Goal: {career_goal}")

if __name__ == "__main__":
    main()
