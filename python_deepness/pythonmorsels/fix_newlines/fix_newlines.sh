echo """This is line 1.
This is line 2.
This is line 3.""" > lines1.txt

echo "Use case 1 (lines1.txt output):"
python fix_newlines.py lines1.txt; cat lines1.txt;

echo
echo
echo "Use case 2 (lines2.txt output):"

echo -n """This is line 1.
This is line 2.
This is line 3.""" > lines2.txt

python fix_newlines.py lines2.txt; cat lines2.txt;


echo
echo
echo "Use case 3 (lines3.txt empty file output):"
echo -n "" > lines3.txt
python fix_newlines.py lines3.txt; cat lines3.txt;


echo
echo
echo 'Use case 4 (lines4.txt - file with "\r\n" endings):'

echo -n '''Hello\r\nMy name is Trey\r\nWelcome to my file\r\nThis file is lovely\r\nGoodbye'''> lines4.txt
python fix_newlines.py lines4.txt; cat lines4.txt;

echo
echo
echo 'Use case 5 (lines5.txt - file with "\r\n" endings):'

echo -n '''Hello\r\nMy name is Trey\r\nWelcome to my file\r\nThis file is lovely\r\nGoodbye\r\n''' > lines5.txt
python fix_newlines.py lines5.txt; cat lines5.txt;

echo
echo
