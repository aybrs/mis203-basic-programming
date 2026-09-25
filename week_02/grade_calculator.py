courses = {
    "Basic Programming": [],
    "Research Methods": [],
    "Management and Organization": [],
}
#this part maden to define the courses and how many student have a note in each course, and to find a avarage of the notes in each course.
course_keys = {
    "1": "Basic Programming",
    "2": "Research Methods",
    "3": "Management and Organization"
}

def print_course_summary():
    #prints the current status of each course after every entry and at program end.
    print("\n" + "=" * 50)
    print("             CURRENT COURSE SUMMARY")
    print("=" * 50)
    for c_name, scores in courses.items():
        count = len(scores)
        if count > 0:
             #this line is necessary because of the ZeroDivisionError, if there is no student in the course, it will not try to calculate the average.
             avg = sum(scores) / count
             print(f"-{c_name:28}: {count} student(s) | Average: {avg:.2f}")
        else :
            print(f"- {c_name:28}: 0 Students   | Average: No grades")
    print("=" * 50 + "\n")

print("=== Student Grade Registration System ===")
print("Hint: 'q' or 'Q' -> Quit | 'x' or 'X' ->Go back one step\n") 

current_step = 0
#current step maden to allow for a return trip.
name = ""
student_id = ""
selected_course = ""

while True:
     #-- Step 1: Get student name and surname --
     if current_step == 0:
        val = input("Enter student name and surname: ").strip()
        if val in ["q", "Q"]:
            break
        if val in ["x", "X"]:
            print("You are already at the first step. ")
            continue  
        if not val:
            print("Name and surname cannot be empty.")
            continue
        name = val
        current_step = 1

     #-- Step 2: Get student ID --
     elif current_step == 1:
        val = input(f"Enter student ID for [{name}]: ").strip()
        if val in ["q", "Q"]:
            break
        if val in ["x", "X"]:
            print("going back to Name step...\n")
            current_step = 0
            continue
        if not val:
            print("Student ID cannot be empty.")
            continue
        student_id = val
        current_step = 2

        #-- Step 3: Select course --

     elif current_step == 2:
            print(f"\nSelect a course for [{name} - {student_id}]:")
            print("1-) Basic Programming")
            print("2-) Research Methods")
            print("3-) Management and Organization")

            val = input("Enter your choice (1-3): ").strip()
            if val in ["q", "Q"]:
                break
            if val in ["x", "X"]:
                print("going back to Student ID step...\n")
                current_step = 1
                continue
            if val in course_keys:
                selected_course = course_keys[val]
                current_step = 3
            else:
                print("Invalide choice!!! Please select 1,2 or 3.")

        #-- Step 4: Get student grade --
     elif current_step == 3:
          val = input(f"\nEnter score for [{name}] - {selected_course}: ").strip()
          if val in ["q", "Q"]:
              break
          if val in ["x", "X"]:
              print("going back to Course selection step...\n")               
              current_step = 2
              continue
          try:
              score = float(val)
              if 0 <= score <= 100:
                  #Detemine Letter Grade
                  if score >= 90:
                      letter = 'A'
                  elif score >= 80:
                      letter = 'B'
                  elif score >= 70:
                      letter = 'C'
                  elif score >= 60:
                      letter = 'D'
                  else:
                      letter = 'F'

                  courses[selected_course].append(score)
                  print(f"\n✔ [RECORDED] {name} ({student_id}) - {selected_course}: {score} -> {letter}")
                
                # Show updated statistics after each valid entry
                  print_course_summary()
                
                # Reset step to enter the next student
                  current_step = 0
              else:
                print("Error: Score must be between 0 and 100.")
          except ValueError:
            print("Error: Please enter a valid numerical score.")

# Final summary displayed when exiting with 'q'
print("\nProgram terminated. Final results:")
print_course_summary()            
