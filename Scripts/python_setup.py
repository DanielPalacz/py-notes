# python3 -m sysconfig

import sysconfig
import pprint

# wszystkie dostępne ustawienia builda
pprint.pprint(sysconfig.get_config_vars())

# lokalizacja instalacji standardowej biblioteki
print("Prefix:", sysconfig.get_config_var("prefix"))
print("Exec-prefix:", sysconfig.get_config_var("exec_prefix"))
print("Purelib (Python .py files):", sysconfig.get_path("purelib"))
print("Plib/dynload (C extensions):", sysconfig.get_path("platlib"))

import sys
print("sys.prefix:", sys.prefix)
print("sys.executable:", sys.executable)
print("sys.path:", sys.path)

# sys.prefix → katalog główny instalacji Pythona
# sys.executable → pełna ścieżka do binarki
# sys.path → ścieżki, gdzie Python szuka modułów (.py, .so, site-packages`)
