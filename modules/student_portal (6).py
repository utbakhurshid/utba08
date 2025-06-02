def run_student_portal():
    from datetime import datetime

    # data store
    students = [
        {
            "Batch": "2023", "Degree": "ICS", "RollNo": "ICS-101", "Name": "Ali Khan", "Password": "ali123",
            "FatherName": "Ahmed Khan", "Contact": "03001234567", "Address": "Lahore", "CNIC": "35201-1234567-1",
            "Email": "ali.khan@example.com"
        },
        {
            "Batch": "2023", "Degree": "FSC", "RollNo": "FSc-102", "Name": "Sara Ahmed", "Password": "sara456",
            "FatherName": "Imran Ahmed", "Contact": "03011234567", "Address": "Karachi", "CNIC": "42101-2345678-2",
            "Email": "sara.ahmed@example.com"
        },
        {
            "Batch": "2024", "Degree": "ICOM", "RollNo": "Icom-201", "Name": "Usman Malik", "Password": "usman789",
            "FatherName": "Naveed Malik", "Contact": "03021234567", "Address": "Islamabad", "CNIC": "61101-3456789-3",
            "Email": "usman.malik@example.com"
        }
    ]

    attendance = [
        {"RollNo": "ICS-101", "Date": "2023-10-01", "Status": "Present", "Course": "ICS101"},
        {"RollNo": "ICS-101", "Date": "2023-10-02", "Status": "Present", "Course": "ICS101"},
        {"RollNo": "ICS-101", "Date": "2023-10-03", "Status": "Absent", "Course": "ICS101"},
        {"RollNo": "ICS-101", "Date": "2023-10-04", "Status": "Present", "Course": "FSc102"},
        {"RollNo": "ICS-101", "Date": "2023-11-15", "Status": "Present", "Course": "ICS101"},
        {"RollNo": "FSc-102", "Date": "2023-10-01", "Status": "Present", "Course": "FSc101"},
        {"RollNo": "Icom-201", "Date": "2023-10-01", "Status": "Present", "Course": "MGT201"}
    ]

    courses = [
        {"RollNo": "ICS-101", "CourseCode": "ICS101", "CourseName": "Intro to Programming"},
        {"RollNo": "ICS-101", "CourseCode": "FSc102", "CourseName": "Discrete Math"},
        {"RollNo": "FSc-102", "CourseCode": "FSc101", "CourseName": "Intro to Programming"},
        {"RollNo": "Icom-201", "CourseCode": "MGT201", "CourseName": "Principles of Management"}
    ]

    grades = [
        {"RollNo": "ICS-101", "CourseCode": "ICS101", "Grade": "A"},
        {"RollNo": "ICS-101", "CourseCode": "FSc102", "Grade": "B+"},
        {"RollNo": "FSc-102", "CourseCode": "FSc101", "Grade": "A-"},
        {"RollNo": "Icom-201", "CourseCode": "MGT201", "Grade": "B"}
    ]

    fees = [
        {"RollNo": "ICS-101", "TotalFees": "50000", "Paid": "40000", "Due": "10000"},
        {"RollNo": "FSc-102", "TotalFees": "50000", "Paid": "45000", "Due": "5000"},
        {"RollNo": "Icom-201", "TotalFees": "45000", "Paid": "45000", "Due": "0"}
    ]

    def student_login():
        print("\n==== STUDENT PORTAL ====")
        batch = input("Batch: ").strip()
        degree = input("Degree: ").strip().upper()
        roll_no = input("Roll Number: ").strip().upper()

        for student in students:
            if student["Batch"] == batch and student["Degree"] == degree and student["RollNo"] == roll_no:
                password = input("Password: ").strip()
                if password == student["Password"]:
                    print(f"\nWelcome, {student['Name']}!")
                    return roll_no
                else:
                    print("Incorrect Password!")
                    return None
        print("Student not found!")
        return None

    def student_menu(roll_no):
        while True:
            print("\n==== STUDENT DASHBOARD ====")
            print("1. View Attendance")
            print("2. View Fees")
            print("3. View Grades")
            print("4. Courses Enrolled")
            print("5. Attendance Percentage (by Year)")
            print("6. View Profile")
            print("7. View Result Card")
            print("8. Logout")
            choice = input("Choose (1-8): ")
            if choice == '1':
                view_attendance(roll_no)
            elif choice == '2':
                view_fees(roll_no)
            elif choice == '3':
                view_grades(roll_no)
            elif choice == '4':
                view_courses(roll_no)
            elif choice == '5':
                yearly_attendance(roll_no)
            elif choice == '6':
                view_profile(roll_no)
            elif choice == '7':
                view_result_card(roll_no)
            elif choice == '8':
                print("Logging out...")
                break
            else:
                print("Invalid choice!")

    def view_attendance(roll_no):
        course = input("Course code (optional): ").strip().upper()
        date = input("Date YYYY-MM-DD (optional): ").strip()
        print("\n==== ATTENDANCE RECORDS ====")
        found = False
        for record in attendance:
            if record["RollNo"] == roll_no:
                if (not course or record["Course"] == course) and (not date or record["Date"] == date):
                    print(f"{record['Date']} | {record['Course']} | {record['Status']}")
                    found = True
        if not found:
            print("No records found!")

    def view_fees(roll_no):
        print("\n==== FEE DETAILS ====")
        for f in fees:
            if f["RollNo"] == roll_no:
                print(f"Total: {f['TotalFees']}, Paid: {f['Paid']}, Due: {f['Due']}")
                return
        print("No fee record found.")

    def view_grades(roll_no):
        print("\n==== GRADES ====")
        found = False
        for g in grades:
            if g["RollNo"] == roll_no:
                print(f"{g['CourseCode']} | Grade: {g['Grade']}")
                found = True
        if not found:
            print("No grades found.")

    def view_courses(roll_no):
        print("\n==== ENROLLED COURSES ====")
        found = False
        for c in courses:
            if c["RollNo"] == roll_no:
                print(f"{c['CourseCode']} | {c['CourseName']}")
                found = True
        if not found:
            print("No course records.")

    def yearly_attendance(roll_no):
        year = input("Enter year (YYYY): ").strip()
        print(f"\n==== ATTENDANCE DETAILS FOR {year} ====")
        present, total = 0, 0
        for record in attendance:
            if record["RollNo"] == roll_no and record["Date"].startswith(year):
                print(f"{record['Date']} | {record['Course']} | {record['Status']}")
                total += 1
                if record["Status"].lower() == "present":
                    present += 1
        if total:
            print(f"\nTotal Classes: {total}, Present: {present}, Attendance: {present / total * 100:.2f}%")
        else:
            print("No attendance records found for this year.")

    def view_profile(roll_no):
        print("\n==== STUDENT PROFILE ====")
        for student in students:
            if student["RollNo"] == roll_no:
                print(f"Name       : {student['Name']}")
                print(f"Father Name: {student['FatherName']}")
                print(f"Contact No : {student['Contact']}")
                print(f"Email      : {student['Email']}")
                print(f"Roll No    : {student['RollNo']}")
                print(f"Address    : {student['Address']}")
                print(f"CNIC       : {student['CNIC']}")
                return
        print("Profile not found.")

    def view_result_card(roll_no):
        print("\n==== RESULT CARD ====")
        student_courses = [c for c in courses if c["RollNo"] == roll_no]
        found = False
        for c in student_courses:
            for g in grades:
                if g["RollNo"] == roll_no and g["CourseCode"] == c["CourseCode"]:
                    print(f"{c['CourseCode']} - {c['CourseName']} | Grade: {g['Grade']}")
                    found = True
        if not found:
            print("No result records available.")

    # Main loop
    while True:
        roll = student_login()
        if roll:
            student_menu(roll)
        else:
            if input("Try again? (y/n): ").lower() != 'y':
                print("Exiting Student Portal...")
                break

if __name__ == "__main__":
    run_student_portal()
