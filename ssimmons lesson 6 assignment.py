
def main():
    student_info = {}
    student_info['Sam'] = {
        'ID': 'S001',
        'GPA': 3.5,
        'Credits Completed': 30,
        'Grades': ['A', 'B', 'A-', 'B+']
    }
    student_info['John'] = {
        'ID': 'S002',
        'GPA': 3.8,
        'Credits Completed': 45,
        'Grades': ['A', 'A', 'B+', 'A-']
    }
    student_info['Larry'] = {
        'ID': 'S003',
        'GPA': 3.2,
        'Credits Completed': 20,
        'Grades': ['B', 'C', 'B-', 'B']
    }
    print("Student Information Dictionary:")
    print(student_info)
    print("\n Student Names")
    for student in student_info.keys():
        print(student)
    print("\n Student Information")
    print(f"{'Name':<10}\t{'ID':<10}\t{'GPA':<10}\t{'Credits Completed':<20}\t{'Grades'}")
    for name, details in student_info.items():
        print(f"{name:<10}\t{details['ID']:<10}\t{details['GPA']:<10}\t{details['Credits Completed']:<20}\t{', '.join(details['Grades'])}")
    print("\nRemoving a Student:")
    removed_student = student_info.pop('Larry', None)
    print(f"Removed Student: {removed_student}")
    print("Updated Student Information Dictionary:")
    print(student_info)
    print("\nAccessing GPA Information:")
    for name in student_info.keys():
        gpa = student_info[name].get('GPA')
        print(f"{name}: GPA = {gpa}")
    print("\nClearing the Student Registry:")
    student_info.clear()
    print("Student Information Dictionary after clearing:")
    print(student_info)

    print("\n" + "-"*15)
    print("Coded by samuel Simmons")

if __name__ == "__main__":
    main()

