class Translator:
    def __init__(self, lang_to):
        self.lang_to = lang_to
        self.dictionary = {
            "құс": {"ru": "птица", "en": "bird"},
            "мысық": {"ru": "кошка", "en": "cat"},
            "ит": {"ru": "собака", "en": "dog"},
            "күн": {"ru": "солнце", "en": "sun"},
            "оқу": {"ru": "учить", "en": "study"},
        }

    def __call__(self, word, repeat):
        max_repeat = int(input("Максималды қайталауды енгізіңіз: "))
        if repeat > max_repeat:
            return "Шамадан тыс"
        if word not in self.dictionary:
            return "Сөз табылмады"
        translations = self.dictionary[word]
        if self.lang_to not in translations:
            return "Бұл бағытта аударма жоқ"
        return (translations[self.lang_to] + " ") * repeat


tr_ru = Translator("ru")
print(tr_ru("мысық", 5))
print(tr_ru("ит", 2))

tr_en = Translator("en")
print(tr_en("құс", 2))

print(tr_ru("күн", 3))
