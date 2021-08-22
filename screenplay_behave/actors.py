from typing import Dict
from screenplay.actor import Actor


class Actors:
    def __init__(self):
        self._actors: Dict[str, Actor] = {}
        self._active: Actor = None

    def __getitem__(self, key: str) -> Actor:
        return self._actors[key]

    def add_person_called(self, name: str):
        a = Actor.named(name)
        self._actors[name] = a
        return a

    @property
    def active(self) -> Actor:
        return self._active

    def switch_active(self, name: str):
        self._active = self._actors[name]

    def clean_up(self):
        for name in self._actors:
            self._actors[name].clean_up()
