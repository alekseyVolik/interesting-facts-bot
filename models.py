from dataclasses import dataclass
from typing import List


@dataclass
class WikipediaOnThisDay:
    selected: List['WikipediaSelectedEvents']
    web_link: str = ''

    def __post_init__(self):
        self.selected = sorted(self.selected,
                               key=lambda event: event.year,
                               reverse=True)


@dataclass
class WikipediaSelectedEvents:
    text: str
    year: int
