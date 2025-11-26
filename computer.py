class Processor:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def info(self):
        return f"Процессор: {self.model}, {self.speed} ГГц"


class Memory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used = 0

    def load(self, amount):
        if self.used + amount <= self.capacity:
            self.used += amount
        else:
            self.used = self.capacity

    def free(self, amount):
        self.used = max(0, self.used - amount)

    def info(self):
        return f"ОЗУ: {self.used}/{self.capacity} ГБ"


class HardDrive:
    def __init__(self, size):
        self.size = size
        self.files = {}

    def save_file(self, name, size):
        if self.get_free_space() >= size:
            self.files[name] = size
        else:
            print("Орын жеткіліксіз!")

    def delete_file(self, name):
        if name in self.files:
            del self.files[name]

    def get_free_space(self):
        return self.size - sum(self.files.values())

    def info(self):
        return f"Диск: {self.size} ГБ (бос: {self.get_free_space()} ГБ)"


class Computer:
    def __init__(self, brand, cpu_model, cpu_speed, ram_capacity, disk_size):
        self.brand = brand
        self.cpu = Processor(cpu_model, cpu_speed)
        self.ram = Memory(ram_capacity)
        self.hdd = HardDrive(disk_size)

    def start(self):
        print(f"{self.brand} компьютер іске қосылды.")

    def load_program(self, program_name, ram_usage, disk_usage):
        print(f"'{program_name}' жүктелуде...")
        self.ram.load(ram_usage)
        self.hdd.save_file(program_name, disk_usage)

    def close_program(self, program_name, ram_usage):
        print(f"'{program_name}' жабылды.")
        self.ram.free(ram_usage)
        self.hdd.delete_file(program_name)

    def show_info(self):
        print(f"\nКомпьютер: {self.brand}")
        print(self.cpu.info())
        print(self.ram.info())
        print(self.hdd.info())
