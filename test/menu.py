class Menu_choice:

    def __init__(self):
        self._default = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "점심":
            return "한식"
        else:
            return "알 수 없는 명령어입니다."
