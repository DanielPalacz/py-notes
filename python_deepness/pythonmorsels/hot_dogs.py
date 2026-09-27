

def dog_and_bun_packs_needed(guests_nr: int) -> tuple[int, int]:
    if not guests_nr % 8:
        buns_packs = guests_nr // 8
    else:
        buns_packs = guests_nr // 8 + 1

    if not guests_nr % 10:
        hotdogs_packs = guests_nr // 10
    else:
        hotdogs_packs = guests_nr // 10 + 1

    return buns_packs, hotdogs_packs


# def dog_and_bun_packs_needed(guests_nr: int) -> tuple[int, int]:
#     buns_packs = (guests_nr + 7) // 8
#     hotdogs_packs = (guests_nr + 9) // 10
#
#     return buns_packs, hotdogs_packs
