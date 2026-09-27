
# duration = 9907
# hours = duration // (60 * 60)
# minutes = (duration // 60) % 60
# seconds = duration % 60
# print(f"{hours}:{minutes:02d}:{seconds:02d}")


# But we could use divmod twice instead:

duration = 9907
minutes, seconds = divmod(duration, 60)
hours, minutes = divmod(minutes, 60)
print(f"{hours}:{minutes:02d}:{seconds:02d}")
