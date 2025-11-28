class Adam:
    def __init__(self, at, jasy):
        self.at = at
        self.jasy = jasy

    def tanystyru(self):
        return f"Менің атым {self.at}, мен {self.jasy} жастамын."

class Mugalim(Adam):
    def __init__(self, at, jasy, peni):
        super().__init__(at, jasy)
        self.peni = peni

    def sabak_beru(self):
        return f"{self.peni} пәнінен сабақ өтіп жатырмын."

    def uiru(self, student, tema):
        return f"{student.at} студентіне {tema} тақырыбын түсіндіріп жатыр."

class Student(Adam):
    def __init__(self, at, jasy, kurs):
        super().__init__(at, jasy)
        self.kurs = kurs
        self.bilim = []

    def uiru(self, tema):
        self.bilim.append(tema)
        return f"{self.at} студенті '{tema}' тақырыбын өздігінен меңгерді."

    def koru(self):
        return f"{self.at} меңгерген тақырыптар: {', '.join(self.bilim) if self.bilim else 'әзірге ештеңе'}"

class Synyp:
    def __init__(self, at):
        self.at = at
        self.mugalim = None
        self.studentter = []

    def mugalim_qosu(self, mugalim):
        self.mugalim = mugalim

    def student_qosu(self, student):
        self.studentter.append(student)

    def akparat(self):
        akp = f"\nСынып атауы: {self.at}\n"
        akp += f"Мұғалім: {self.mugalim.at} ({self.mugalim.peni})\n"
        akp += "Студенттер:\n"
        for s in self.studentter:
            akp += f" - {s.at}, {s.kurs}-курс\n"
        return akp

print("=== ОББ бойынша сабақ ===")

synyp_atauy = input("Сынып атауын енгізіңіз: ")
synyp = Synyp(synyp_atauy)

print("\n--- Мұғалім туралы мәлімет ---")
m_at = input("Мұғалімнің аты-жөні: ")
m_jas = int(input("Мұғалімнің жасы: "))
m_peni = input("Пән атауы: ")
mugalim = Mugalim(m_at, m_jas, m_peni)
synyp.mugalim_qosu(mugalim)

print("\n--- Студенттер туралы мәлімет ---")
n = int(input("Студенттер санын енгізіңіз: "))
for i in range(n):
    print(f"\n{i+1}-студент:")
    s_at = input("Аты-жөні: ")
    s_jas = int(input("Жасы: "))
    s_kurs = int(input("Курсы: "))
    student = Student(s_at, s_jas, s_kurs)
    synyp.student_qosu(student)

print(synyp.akparat())
print(mugalim.sabak_beru())

student_tandau = input("\nМұғалім қай студентке тақырып түсіндіреді? (аты): ")
tema = input("Тақырып атауы: ")

target = None
for s in synyp.studentter:
    if s.at.lower() == student_tandau.lower():
        target = s
        break

if target:
    print(mugalim.uiru(target, tema))
else:
    print("Мұндай студент табылмады!")

print("\n--- Өздік жұмыс ---")
student_tandau2 = input("Қай студент өздігінен оқиды? (аты): ")
tema2 = input("Қандай тақырыпты меңгереді?: ")

for s in synyp.studentter:
    if s.at.lower() == student_tandau2.lower():
        print(s.uiru(tema2))
        print(s.koru())
        break
else:
    print("Мұндай студент табылмады!")
