from dataclasses import dataclass
from typing import List


@dataclass
class Navigation:
    label: str
    route: str

    sub_nav: List = list
