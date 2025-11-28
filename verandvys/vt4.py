import os
from tcommand import TCommand

try:
    user_code = int(input("Код команды енгізіңіз (мысалы, 1, 2, 4, 6, 20): "))
except ValueError:
    print("Қате! Тек бүтін сан енгізіңіз.")
    exit()

out = TCommand()
out.name_command = user_code
result = out.get_full_name()

html = f"""<html> ... <td>{user_code}</td><td>{result}</td> ... </html>"""

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = rf"C:\Users\Admin\OneDrive\Рабочий стол\tcommand_single_{user_code}.html"


with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML файл для команды {user_code} создан на рабочем столе:\n{file_path}")
