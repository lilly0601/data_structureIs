from vystech import Student, ScholarshipStudent, Group

groups = [
    Group("ИС-23-1"),
    Group("ИС-23-2"),
    Group("ИС-23-3"),
    Group("ИС-23-4"),
    Group("ИС-23-5")
]

groups[0].add_student(Student("Аяжан", 88))
groups[0].add_student(ScholarshipStudent("Лили", 95))

groups[1].add_student(Student("Мөлдір", 85))
groups[1].add_student(Student("Айнура", 45))
groups[1].add_student(ScholarshipStudent("Жаннұр", 95))

groups[2].add_student(Student("Арслан", 73))
groups[2].add_student(Student("Сұлтан", 52))

groups[3].add_student(ScholarshipStudent("Қасым", 97))
groups[3].add_student(Student("Алия", 60))

groups[4].add_student(Student("Томирис", 83))
groups[4].add_student(ScholarshipStudent("Әділет", 92))

print("=== Қол жетімді топтар ===")
for i, g in enumerate(groups, start=1):
    print(f"{i}. {g.group_name}")

choice = int(input("Қай топты таңдаңыз (1–5): "))

if 1 <= choice <= 5:
    print()
    groups[choice - 1].show_all()
else:
    print("Қате таңдау!")
