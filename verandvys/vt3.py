from tcommand import TCommand

def test_tcommand():
    t = TCommand()

    assert t._MAP[1] == "КІРІС ҰЯШЫҚТАН АЛУ"
    assert t._MAP[2] == "ҰЯШЫҚТАН ШЫҒЫС ҰЯШЫҚҚА ЖІБЕРУ"
    assert t._MAP[4] == "РЕЗЕРВТЕУ"
    assert t._MAP[6] == "НӨЛ"
    assert t._MAP[20] == "ПАРМАНДЫ ШЫҒАРУДЫ ТОЛЫҚТАҢЫЗ"

    t.name_command = 4
    assert t.get_full_name() == "РЕЗЕРВТЕУ"

    t.name_command = -1
    assert t.get_full_name() == "ҚАТЕ : Пәрмен коды жарамсыз"

    print("Барлық формальды тексерулер сәтті өтті ✅")

if __name__ == "__main__":
    test_tcommand()
