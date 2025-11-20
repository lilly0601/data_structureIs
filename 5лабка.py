import os
from tcommand import TCommand

# Список кодов команд для тестирования
codes = [-1, 1, 2, 4, 6, 20]
out = TCommand()

# Начало HTML-документа
html = """
<html>
<head>
<meta charset="UTF-8">
<title>Результаты теста TCommand</title>
<style>
table {border-collapse: collapse; width: 60%;}
td, th {border: 1px solid black; padding: 6px; text-align: center;}
th {background-color: #f2f2f2;}
body {font-family: Arial, sans-serif;}
</style>
</head>
<body>
<h2>Тестирование класса TCommand</h2>
<table>
<tr><th>Код команды</th><th>Результат</th></tr>
"""

# Цикл для автоматического добавления данных в таблицу
for code in codes:
    out.name_command = code
    result = out.get_full_name()
    html += f"<tr><td>{code}</td><td>{result}</td></tr>\n"

# Завершение HTML-документа
html += "</table>\n</body>\n</html>"

# Определяем путь к рабочему столу
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop, "tcommand_test.html")

# Сохраняем HTML-файл
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML файл создан на рабочем столе:")
print(file_path)


