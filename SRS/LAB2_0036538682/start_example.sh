#!/bin/sh

print_cyan() {
    echo "\033[96m$1\033[0m"
}


print_cyan "Dodavanje Korisnika"
(
set -x
python3 Autentikacija.py usermgmt add Iva <<< $'SigurnaLozinka~12\nSigurnaLozinka~12'
python3 Autentikacija.py usermgmt add Marko <<< $'Marko.bond007\nMarko.bond007'
python3 Autentikacija.py usermgmt add Leo <<< $'leoIleo2.\nleoIleo2.'
)
echo " "
print_cyan "Login Korisnika"
(
set -x
python3 Autentikacija.py usermgmt Login <<< $'Leo\nleoIleo2.'
python3 Autentikacija.py usermgmt Login <<< $'Marko\nMarko.bond007'
)
echo " "
print_cyan "Dodavanje Losa Lozinka"
(
set -x
python3 Autentikacija.py usermgmt add LosaLozinka <<< $'aa\na2bch3456\nA2bcd567\nA.2bcd67\nA.2bcd67'
)
echo " "
print_cyan "Promijena Lozinke"
(
set -x
python3 Autentikacija.py usermgmt passwd Leo <<< $'KeksIKeks2.0\nKeksIKeks2.0'
python3 Autentikacija.py usermgmt Login <<< $'Leo\nKeksIKeks2.0.'
)

echo " "
print_cyan "Forsiranje Nove"
(
set -x
python3 Autentikacija.py usermgmt forcepass Leo
python3 Autentikacija.py usermgmt Login <<< $'Leo\nKeksIKeks2.0.\nNovaLozinka.123\nNovaLozinka.123'
)

echo " "
print_cyan "Forsiranje Nove Zabrana Iste"
(
set -x
python3 Autentikacija.py usermgmt forcepass Marko
python3 Autentikacija.py usermgmt Login <<< $'Marko\nMarko.bond007\nMarko.bond007\nMarko.bond008\nMarko.bond008'
)

echo " "
print_cyan "Brisanje Korisnika"
(
set -x
python3 Autentikacija.py usermgmt del Marko
python3 Autentikacija.py usermgmt Login <<< $'Marko\nMarko.bond008'
)