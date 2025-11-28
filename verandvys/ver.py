import os
from tcommand import TCommand

codes = [-1, 1, 2, 4, 6, 20]
out = TCommand()

html = """
<html> ... <table> ...
"""

for code in codes:
    out.name_command = code
    result = out.get_full_name()
    html += f"<tr><td>{code}</td><td>{result}</td></tr>\n"

html += "</table></body></html>"

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = r"C:\Users\Admin\OneDrive\Рабочий стол\tcommand_test.html"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML файл создан на рабочем столе:", file_path)
