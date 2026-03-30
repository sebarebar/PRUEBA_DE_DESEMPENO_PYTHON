from functions import *
from functions_csv import * 

db =[] 
running = True

while running:

        print("\n╔══════════════════════════════════════╗")
        print("║           MAIN MENU                  ║")
        print("╚══════════════════════════════════════╝")
        print("1. register student")
        print("2. consult list of students")
        print("3. search student")
        print("4. update student")
        print("5. remove student")
        print("7. save students")
        print("8. upload student list")
        print("9. Exit")
        print("────────────────────────────────────────")
        try:
            choice = int(input("choose the option you want to make.: "))
        except ValueError:
            print("Error: enter a number between 1 and 8")
            continue

        if choice < 1 or choice > 9:
            print("Error: enter a number between 1 and 8")
            continue
        print("────────────────────────────────────────")

        if choice == 1:
            try:
                id  = int(input("Student ID: "))
            except ValueError:
                print("Error: Please enter only numbers.")
                continue

            name = input("Enter student name: ").strip()
            if not name.replace(" ", "").isalpha():
                print("Error: name must contain only letters")
                continue
            
            try:
                ege = int(input("Entered students age: "))
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue
    
            course = input("Enter the students course: ")
            if not course.replace(" ", "").isalpha():
                print("Error: name must contain only letters")
                continue

            status = input("Enter the student status(Active/Inactive): ")
            if not status.replace(" ", "").isalpha():
                print("Error: name must contain only letters")
            
                continue   
            db=register_student(db, id, name, ege, course, status)

        elif choice == 2:
            consult_list(db)

        elif choice == 3:
            try:
                id = int(input("Enter the student ID you want to search for: "))

            except ValueError:
                print("Error: IDs only contain numbers. please enter only numbers")
                continue

            student = search_student(db,id)

            if student:
                print("\nStudent found:")
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"ege: {student['age']}")
                print(f"course: {student['course']}")
                print(f"status: {student['status']}")
            else:
                print("Student not found.")

        elif choice == 4:
            print
            try:
                id = int(input("Enter the student ID you want to update: "))

            except ValueError:
                print("Error: IDs only contain numbers. please enter only numbers")
                continue
                
            new_name = input(
                "Enter new name (leave blank to keep): ").strip()
            new_age = int(input(
                "Enter new age (leave blank to keep): "))
            new_course = input(
                "Enter new course (leave blank to keep): ").strip()
            new_status = input(
                "Enter new status(leave blank to keep): ").strip()
            
            try:
                new_name = str(new_name) if new_name else None
            except ValueError:
                print("Error: please enter only letters.")
                continue

            try:
                new_age = int(new_age) if new_age else None
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            try:
                new_course = str(new_course) if new_course else None
            except ValueError:
                print("Error: please enter only letters.")
                continue

            try:
                new_status = str(new_status) if new_status else None
            except ValueError:
                print("Error: please enter only letters.")
                continue
            
            if update_student(db, id, new_name, new_age, new_course, new_status,):
                print("Student updated successfully.")

            else : 
                print("Student no found")

        elif choice == 5:
            id = int(input("Enter the student ID of the student you want to delete: "))
            if delete_product(db, id):
                print("Product deleted successfully.")
            else:
                print("Product not found.")

        elif choice == 6:
            filename = input(
                "Enter filename to save (e.g., df.csv or student_list.csv): ").strip()
            save_student_list(db, filename)


        elif choice == 7:
            filename = input(
                "Enter filename to upload (e.g., df.csv or student_list.csv): ").strip()
            loaded = upload_list(filename)
            csv_choice = input(
                "Overwrite current list? (yes/no): ").strip().lower()

            if csv_choice == 'yes':
                db.clear()
                db.extend(loaded)
            elif csv_choice == 'no':
                for product in loaded:
                    existing = search_student(db, id['id'])
                    if existing:
                        existing['name'] += student['name']
                        existing['age'] = student['age']
                        existing['course'] = student['course']
                        existing['status'] = student['status']
                    else:
                        db.append(product)

            print(f"product loaded: {len(loaded)}")
            if csv_choice == 'yes':
                print("list overwritten with loaded data.")
            elif csv_choice == 'no':
                print("Loaded products merged with existing inventory.")


        elif choice == 8:
            print("closet the program. good bye!")
            running = False


