from dataclasses import dataclass
from typing import List


@dataclass
class WikipediaOnThisDay:
    date: str
    wikipedia: str
    events: List['WikipediaEvent']


@dataclass
class WikipediaEvent:
    year: str
    description: str
    wikipedia: List['WikipediaLink']


@dataclass
class WikipediaLink:
    title: str
    wikipedia: str
