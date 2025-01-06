from dataclasses import dataclass
from enum import Enum


class Specializace(Enum):
    KARDIOLOG = 0
    NEUROLOG= 1
    NEFROLOG = 2

@dataclass
class Pacient:
    rodne_cislo: int
    jmeno: str
    prijmeni: str
    pohlavi: str

@dataclass
class Lekar:
    jmeno: str
    specializace: str


@dataclass
class Ordinace:
    specializace: str
    hlavni_l: Lekar
    pomocny_l:Lekar
    pacienti: list[Pacient]