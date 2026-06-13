
from string.templatelib import Interpolation

def lower_upper(template):
    """Render static parts lowercase and interpolations uppercase."""
    parts = []
    for part in template:
        print(part)
        if isinstance(part, Interpolation):
            parts.append(str(part.value).upper())
        else:
            parts.append(part.lower())
    return ''.join(parts)

name = 'Wenslydale'
template = t'Mister {name}'
assert lower_upper(template) == 'mister WENSLYDALE'
