from dataclasses import dataclass, field


@dataclass
class Navigation:
    label: str
    route: str

    sub_nav: list = field(default_factory=lambda: [])
