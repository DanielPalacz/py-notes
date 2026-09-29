
from typing import Optional

def len_or_none(obj) -> Optional[int]:
    try:
        return len(obj)
    except TypeError:
        return None
