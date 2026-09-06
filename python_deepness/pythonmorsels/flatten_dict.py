from typing import Optional


D1 = {'a': {1: True, 2: False}, 'b': {3: True, 4: False}}
D2 = {'a': {1: True, 2: False}}
D3 = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}


def flatten_dict(dod: dict, *, sep: str = "_") -> dict:
    def flatten(current: dict, prefix: str = "") -> dict:
        result = {}

        for key, val in current.items():
            new_key = f"{prefix}{sep}{key}" if prefix else str(key)

            if isinstance(val, dict):
                result.update(flatten(val, new_key))
            else:
                result[new_key] = val

        return result

    return flatten(dod)


# out_d1 = flatten_dict(D1)
out_d2 = flatten_dict(D2)
