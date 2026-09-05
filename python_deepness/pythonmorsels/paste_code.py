
def paste_code():
    print("Paste your code block\n")
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    code = "".join(lines)
    exec(code)
    globals().update(locals())



#
# import sys
#
# def paste_code():
#     print("Paste your code block\n")
#     code = "".join(sys.stdin)
#     exec(code, globals(), globals())
