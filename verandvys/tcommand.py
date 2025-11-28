from dataclasses import dataclass

@dataclass
class TCommand:
    name_command: int = 0
    _MAP = {
        1: "КІРІС ҰЯШЫҚТАН АЛУ",
        2: "ҰЯШЫҚТАН ШЫҒЫС ҰЯШЫҚҚА ЖІБЕРУ",
        4: "РЕЗЕРВТЕУ",
        6: "НӨЛ",
        20: "ПАРМАНДЫ ШЫҒАРУДЫ ТОЛЫҚТАҢЫЗ"
    }

    def get_full_name(self) -> str:
        if self.name_command in self._MAP:
            return self._MAP[self.name_command]
        else:
            return "ҚАТЕ : Пәрмен коды жарамсыз"
