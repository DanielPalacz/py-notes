
# # Base:
#
# def paragraphs(lines: list[str]) -> list[str]:
#     paragraphs_out = []
#     paragraphs_tmp = []
#
#     for line in lines:
#         paragraphs_tmp.append(line)
#
#         if line == "\n":
#             paragraphs_out.append("".join(paragraphs_tmp))
#             paragraphs_tmp = []
#
#     if paragraphs_tmp:
#         paragraphs_out.append("".join(paragraphs_tmp))
#
#     return paragraphs_out
#
#
# L = ["line 1\n", "line 2\n", "\n", "line 3\n", "line 4\n"]

#

# # Bonus 1 - lazy:
#
# def paragraphs(lines):
#     paragraph = []
#
#     for line in lines:
#         paragraph.append(line)
#
#         if line == "\n":
#             yield "".join(paragraph)
#             paragraph = []
#
#     if paragraph:
#         yield "".join(paragraph)


# Bonus 2 - lazy (multiple consecutive blank lines):


def paragraphs(lines):
    paragraph = []
    blank = False

    for line in lines:
        if line == "\n":
            paragraph.append(line)
            blank = True
            continue

        if blank:
            yield "".join(paragraph)
            paragraph = []
            blank = False

        paragraph.append(line)

    if paragraph:
        yield "".join(paragraph)
