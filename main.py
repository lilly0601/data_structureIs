from computer import Computer

def print_menu():
    print("\n=== Компьютер таңдаңыз ===")
    print("1. Оқу үшін (school edition)")
    print("2. Офис компьютер")
    print("3. Орташа деңгей (университет студентіне)")
    print("4. Геймер компьютер")
    print("5. Профессиональный (программистке)")


def get_computer(choice):
    configs = {
        1: Computer("Acer", "Intel Pentium", 2.0, 4, 128),
        2: Computer("HP", "Intel i3", 2.4, 8, 256),
        3: Computer("Lenovo", "Intel i5", 3.2, 16, 512),
        4: Computer("MSI", "Intel i7", 4.0, 32, 1024),
        5: Computer("Apple", "M2 Pro", 3.5, 32, 2000),
    }
    return configs.get(choice, None)


if __name__ == "__main__":
    print_menu()

    try:
        choice = int(input("Нөмірді таңдаңыз (1–5): "))
    except ValueError:
        print("Қате таңдау!")
        exit()

    pc = get_computer(choice)

    if pc:
        pc.start()
        pc.show_info()

        # Дайын бағдарламалар
        pc.load_program("Chrome", 1, 1)
        pc.load_program("VS Code", 2, 4)
        pc.show_info()

        pc.close_program("Chrome", 1)
        pc.show_info()
    else:
        print("Мұндай нөмір жоқ!")
