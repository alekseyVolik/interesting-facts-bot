from dataclasses import dataclass
from typing import List
from random import choice


@dataclass
class WikipediaOnThisDay:
    date: str
    wikipedia: str
    events: List['WikipediaEvent']

    def get_random_event(self) -> 'WikipediaEvent':
        return choice(self.events)


@dataclass
class WikipediaEvent:
    year: str
    description: str
    wikipedia: List['WikipediaLink']


@dataclass
class WikipediaLink:
    title: str
    wikipedia: str
