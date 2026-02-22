from model import *

students = load_students()

while True:
    print("\n----- Student Record Management -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        sid = input("Enter ID: ").strip()
        name = input("Enter Name: ").strip()
        branch = input("Enter Branch: ").strip()

        if sid and name and branch:
            students.append(Student(sid, name, branch))
            save_all_students(students)
            print("Student Added Successfully.")
        else:
            print("All fields are required.")

    elif choice == "2":
        if not students:
            print("No records found.")
        else:
            for s in students:
                print(f"ID: {s.student_id}, Name: {s.name}, Branch: {s.branch}")

    elif choice == "3":
        sid = input("Enter ID to update: ").strip()
        found = False
        for s in students:
            if s.student_id == sid:
                s.name = input("Enter New Name: ").strip()
                s.branch = input("Enter New Branch: ").strip()
                found = True
                break
        if found:
            save_all_students(students)
            print("Updated Successfully.")
        else:
            print("Student Not Found.")

    elif choice == "4":
        sid = input("Enter ID to delete: ").strip()
        new_students = [s for s in students if s.student_id != sid]

        if len(new_students) != len(students):
            students = new_students
            save_all_students(students)
            print("Deleted Successfully.")
        else:
            print("Student Not Found.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")