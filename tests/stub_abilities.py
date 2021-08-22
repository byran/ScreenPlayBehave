from screenplay import Ability


class StubAbility(Ability):
    def __init__(self):
        self.clean_up_run = False

    def clean_up(self):
        self.clean_up_run = True


class SecondStubAbility(Ability):
    def __init__(self):
        self.clean_up_run = False

    def clean_up(self):
        self.clean_up_run = True
