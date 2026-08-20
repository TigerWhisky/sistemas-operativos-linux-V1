from dataclasses import dataclass

@dataclass(frozen=True)
class Process:
    name: str
    arrival: int
    burst: int
    priority: int = 0
