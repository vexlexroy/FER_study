#!/bin/sh

print_cyan() {
    echo "\033[96m$1\033[0m"
}

print_cyan "Upisi glavnu lozinku"
read glavna
(
set -x
python3 PassManage.py init $glavna
python3 PassManage.py addnew $glavna www.google.com sigurnalozinka1
python3 PassManage.py addnew $glavna www.yahoo.com sigurnalozinka2
python3 PassManage.py addnew $glavna www.bok.com www.bok.com
python3 PassManage.py addnew $glavna istaduzina duzinaista
)
echo
print_cyan "Upisani podatci"
(
set -x
python3 PassManage.py get $glavna www.google.com
python3 PassManage.py get $glavna www.yahoo.com
python3 PassManage.py get $glavna www.bok.com
python3 PassManage.py get $glavna istaduzina
)
echo
print_cyan "Zahtjev ne upisanog podatka"
(
set -x
python3 PassManage.py get $glavna www.nepostoji.com
)
echo
print_cyan "Primjer dodavanje postojece adrese"
(
set -x
python3 PassManage.py addnew $glavna www.google.com nesigurnaLozinka1
python3 PassManage.py get $glavna www.google.com
)
echo
print_cyan "Primjer krivog master password-a"
(
set -x
python3 PassManage.py get nije$glavna www.google.com
python3 PassManage.py addnew nije$glavna www.google.com ne
)
echo
print_cyan "Testiranje napada na datoteku, zamjena."
(
set -x
python3 PassManage.py testSwitchTwo
python3 PassManage.py get $glavna www.google.com
python3 PassManage.py addnew $glavna www.google.com ne
python3 PassManage.py testSwitchTwo
python3 PassManage.py get $glavna www.google.com
)
echo
print_cyan "Manualno testiranje..."
(
set -x
python3 PassManage.py main
)