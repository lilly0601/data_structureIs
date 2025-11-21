# Исходный список слов
words = ["apple", "banana", "apricot", "cherry", "blueberry", "avocado", "carrot"]

# Создаём пустой хэш-словарь
grouped = {}

# Проходим по каждому слову
for word in words:
    first_letter = word[0].lower()  # первая буква (в нижнем регистре)
    
    # Если этой буквы ещё нет в словаре — создаём список
    if first_letter not in grouped:
        grouped[first_letter] = []
    
    # Добавляем слово в список по этой букве
    grouped[first_letter].append(word)

# Вывод результата
for letter, group in grouped.items():
    print(f"{letter}: {group}")
