# compile() w Pythonie
#
# Funkcja compile() kompiluje kod źródłowy do obiektu kodu (code object), czyli do bytecode’u CPythona, ale:
#
# ✔ tworzy bytecode (wewnętrznie)
# ❌ nie zapisuje pliku .pyc
# ❌ nie integruje się z systemem cache importu

_bytecode = compile(
    "x = 2 + 2;"
    "print('[1] -', x);"

    "x += 2;"
    "print('[2] -', x);",

    "<string>",
    "exec"
)

exec(_bytecode)
