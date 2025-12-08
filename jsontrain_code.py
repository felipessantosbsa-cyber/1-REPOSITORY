import json

student_notes = 'student_system.json'

print("   <--- STUDENTS NOTES --->\n" + '¨¨' * 15)

def student_menu():
    print("> [1] add student\n" + '---' * 10)
    print("> [2] search desapproveds\n" + '---' * 10)
    print("> [3] search approveds\n" + '---' * 10)
    print("> [4] view students\n" + '---' * 10)
    print("> [5] search student name\n" + '---' * 10)
    print("> [6] delete something student\n" + '---' * 10)
    print("> [7] uptade something student\n" + '---' * 10)
    print("> [8] leave this program\n" + '---' * 10)
    

def add_student():
    try:
        name_student = input("student name: ") 
        print(f"you add {name_student} student\n")
        note1 = float(input("inserch first note: "))
        print(f"you add note {note1}\n")
        note2 = float(input("inserch second note: "))
        print(f"you add note {note2}\n") 
        note3 = float(input("inserch third note: "))
        print(f"you add note {note3}\n")
        print(f"\n student {name_student} notes {note1}, {note2}, {note3}")
        media_result = (note1 + note2 + note3) / 3

        student_name_notes = {
            'name': name_student,
            'note1': note1,
            'note2': note2,
            'note3': note3,
            'result': media_result
        }
        return student_name_notes
    except ValueError:
        print("ERROR: write something numbers for notes please")
        return None

def delete_student():
    name_delete = input("student name from delete: ")
    delete_found = False
    for student in students_list:
        if student['name'] == name_delete:
            students_list.remove(student)
            print(f"SUCCESS removed student {name_delete} delete from the system")
            delete_found = True
            return
    if not delete_found:
        print("no have this student from the system")

def uptade_student():
    name_uptade = input("student name to uptade: ")
    for student in students_list:
        if student['name'] == name_uptade:

            while True:
                note_choice = input("which note do you want to change? (1,2,3 or exit): ")
                if note_choice == '1' or '2' or '3':
                    try:
                        new_note = float(input("what is a new note?: "))
                        student[f'note{note_choice}'] = new_note
                        n1 = student['note1']
                        n2 = student['note2']
                        n3 = student['note3']
                        student['result'] = (n1 + n2 + n3) / 3
                        print(f"SUCESS, to change a notes of {name_uptade} student")
                        return
                    except ValueError:
                        print("ERROR: write something numbers please")
                elif note_choice == exit:
                    return
                else:
                    print("ERROR: write between (1) (2) (3) or (exit)")
    print(f"\n{name_uptade} not found in system")

power = True
students_list = []

try:
    with open(student_notes, 'r') as program_file:
        students_list = json.load(program_file)
    print(f"[load] {len(students_list)} students loaded from file.")
except FileNotFoundError:
    students_list = []
    print("[load] no existing file. starting new file")




while power:
    student_menu()
    try:
        choose_menu = int(input("choose your opition: "))
    except ValueError:
        print("something numbers please")

    if choose_menu == 1:
        student_name_notes = add_student()
        students_list.append(student_name_notes)
        print("your add a student")

    elif choose_menu == 2:
        print("--- DESAPPROVED LIST ---\n")
        found = False
        for students in students_list:
            if students['result'] < 5:
                print(f"Name: {students['name']} | Media: {students['result']}")
                found = True
        
        if not found:
            print("no have desapproved students")

    elif choose_menu == 3:
        print("--- APPROVED LIST ---\n")
        found = False
        for students in students_list:
            if students['result'] >= 5:
                print(f"Name: {students['name']} | Media: {students['result']}")
                found = True
        
        if not found:
            print("no have approved students")

    elif choose_menu == 4:
        print("  <---All Students --->\n")
        for students in students_list:
            print(f"name: {students['name']} | media: {students['result']}")

    elif choose_menu == 5:
        search_student = input("write name to search: ")
        found = False
        for students in students_list:
            if students['name'] == search_student:
                print(f"name: {students['name']}\n" + '-' * 30)
                print('-' * 30)
                print(f"name: {students['name']} | media: {students['result']}")
                print('-' * 30)
                found = True
        if not found:
            print("No have this student in system")

    elif choose_menu == 6:
        delete_student()

    elif choose_menu == 7:
        uptade_student()

    elif choose_menu == 8:
        with open(student_notes, 'w') as program_file:
            json.dump(students_list, program_file, indent=4)

        print(f"\n[SAVE] Data saved successfully to '{student_notes}'.")
        power = False

    else:
        print("no have this option")

print("\nthank you for using my program")
            

