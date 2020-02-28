from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class CaseConfig:
    input_dict: Dict[str, Any]
    case_name: str
    tolerances: Optional[Dict[str, float]] = None
    default_tolerance: float = 0.01

    def __post_init__(self):
        if self.tolerances is None:
            self.tolerances = defaultdict(lambda: self.default_tolerance)
