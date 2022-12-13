from dataclasses import dataclass
from typing import List


@dataclass
class WikipediaOnThisDay:
    events: List['WikipediaEvents']
    web_link: str = ''

    def __post_init__(self):
        self.events = sorted(self.events,
                             key=lambda event: event.year,
                             reverse=True)


@dataclass
class WikipediaEvents:
    text: str
    year: int
