class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def get_info(self):
        return f"Студент: {self.name}, орташа балл: {self.grade}"
    def performance(self):
        if self.grade >= 90:
            return "Өте жақсы оқиды"
        elif self.grade >= 70:
            return "Жақсы оқиды"
        elif self.grade >= 50:
            return "Қанағаттанарлық"
        else:
            return "Оқу үлгерімі төмен"
    def __call__(self, bonus):
        old_grade = self.grade
        self.grade += bonus
        if self.grade > 100:
            self.grade = 100
        if self.grade >= 90 and not isinstance(self, ScholarshipStudent):
            print(f"{self.name} енді үздік студент атанды және стипендия алады! 🎓")
            self.__class__ = ScholarshipStudent
        return f"{self.name} жаңа баллы: {old_grade} → {self.grade}"

class ScholarshipStudent(Student):
    def performance(self):
        return f"{self.name} — үздік студент, стипендия алады!"
    def __call__(self, bonus):
        old_grade = self.grade
        self.grade += bonus
        if self.grade > 100:
            self.grade = 100
        return f"{self.name} стипендия арқасында баллын көтерді: {old_grade} → {self.grade}"

class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def show_all(self):
        print(f"\n=== {self.group_name} тобының студенттері ===")
        for s in self.students:
            print(s.get_info())
            print(s.performance())
            print("-" * 40)

if __name__ == "__main__":
    st1 = Student("Мөлдір", 85)
    st2 = Student("Айнура", 45)
    st3 = ScholarshipStudent("Жаннұр", 95)
    group = Group("ИС-23-2")
    group.add_student(st1)
    group.add_student(st2)
    group.add_student(st3)
    group.show_all()
    print("\n=== __call__ әдісін қолдану ===")
    print(st1(10))
    print(st2(15))  
    print(st3(3))    
    print("\n=== Өзгерістерден кейін ===")
    group.show_all()
