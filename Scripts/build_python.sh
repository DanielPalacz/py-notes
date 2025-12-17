echo "Skrypt ma być wykonywany:"
echo " - z ustawionego głównego katalogu CPythona"
echo " - z ustawionego odpowiednio brancha"
echo " - wymagane jest podanie wersji budowanego buildu Pythona (tj. sprawdzane)"
echo " - Python zostanie zbudowany w $HOME/python-debug-VersionID"

echo -n ""
read _void



if [ ! $1 ]; then
  echo "Wymagane jest podanie wersji budowanego buildu Pythona, czego nie podano." 
  exit
else
  echo "Rozpoczynam budowę buildu Pythona dla wersji: $1"
fi



./configure --with-pydebug --prefix=$HOME/python-debug-$1
make -j$(nproc)
make install

echo ""

