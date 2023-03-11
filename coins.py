class USD:
    def get_value(self):
        return 3.52

    def calculate(self, user_input):
        return user_input * self.get_value()


class ILS:
    def get_value(self):
        return 0.28

    def calculate(self, user_input):
        return user_input * self.get_value()


class EUR:
    def get_value(self):
        return 4.23

    def calculate(self, user_input):
        return user_input * self.get_value()
