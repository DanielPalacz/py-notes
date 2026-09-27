
def format_time(seconds) -> str:
    minutes = seconds // 60
    secs = seconds % 60

    if secs < 10:
        return f"{minutes}:0{secs}"

    return f"{minutes}:{secs}"
