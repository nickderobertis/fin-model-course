from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class CaseConfig:
    input_dict: Dict[str, Any]
    case_name: str
