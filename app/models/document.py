from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Document:
    filename: str
    filetype: str
    content: str
    metadata: Dict = field(default_factory=dict)