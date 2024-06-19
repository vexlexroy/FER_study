#! /bin/sh
#
# Dodajte ili modificirajte pravila na oznacenim mjestima ili po potrebi (i želji) na 
# nekom drugom odgovarajucem mjestu (pazite: pravila se obrađuju slijedno!)
#
IPT=/sbin/iptables
$IPT -P INPUT DROP
$IPT -P OUTPUT DROP
$IPT -P FORWARD DROP

$IPT -F INPUT
$IPT -F OUTPUT
$IPT -F FORWARD

$IPT -A INPUT   -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPT -A OUTPUT  -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPT -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

#
# za potrebe testiranja dozvoljen je ICMP (ping i sve ostalo)
#
$IPT -A INPUT   -p icmp -j ACCEPT
$IPT -A FORWARD -p icmp -j ACCEPT
$IPT -A OUTPUT  -p icmp -j ACCEPT
#
# Primjer "anti spoofing" pravila na sucelju eth0
#
#$IPT -A INPUT   -i eth0 -s 127.0.0.0/8  -j DROP
#$IPT -A FORWARD -i eth0 -s 127.0.0.0/8  -j DROP
#$IPT -A INPUT   -i eth0 -s 203.0.113.0/24  -j DROP
#$IPT -A FORWARD -i eth0 -s 203.0.113.0/24  -j DROP
#$IPT -A INPUT   -i eth0 -s 10.0.0.0/24  -j DROP
#$IPT -A FORWARD -i eth0 -s 10.0.0.0/24  -j DROP
#$IPT -A INPUT   -i eth0 -s 192.168.1.2  -j DROP
#$IPT -A FORWARD -i eth0 -s 192.168.1.2  -j DROP
# -o, -i (port)| -p (protocol)| -s, -d (Ip adresa)| --dport port
#
# Web poslužitelju (tcp/80 i tcp/443) pokrenutom na www se može 
# pristupiti s bilo koje adrese (iz Interneta i iz lokalne mreže), ...
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth0 -d 203.0.113.100 -p tcp --dport 80 -j ACCEPT # za internet
$IPT -A FORWARD -i eth0 -d 203.0.113.100 -p tcp --dport 443 -j ACCEPT
$IPT -A FORWARD -i eth1 -d 203.0.113.100 -p tcp --dport 80 -j ACCEPT # za lokalne
$IPT -A FORWARD -i eth1 -d 203.0.113.100 -p tcp --dport 443 -j ACCEPT
#
# DNS poslužitelju (udp/53 i tcp/53) pokrenutom na www se može 
# pristupiti s bilo koje adrese (iz Interneta i iz lokalne mreže), ...
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth0 -d 203.0.113.100 -p udp --dport 53 -j ACCEPT # za internet
$IPT -A FORWARD -i eth0 -d 203.0.113.100 -p tcp --dport 53 -j ACCEPT
$IPT -A FORWARD -i eth1 -d 203.0.113.100 -p udp --dport 53 -j ACCEPT # za lokalne
$IPT -A FORWARD -i eth1 -d 203.0.113.100 -p tcp --dport 53 -j ACCEPT
#
# ... a SSH poslužitelju na www samo s racunala admin iz lokalne mreže "Private"
# 
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -p tcp -s 10.0.0.20 -i eth1 -d 203.0.113.100 --dport 22 -j ACCEPT
#
# ... kao i SSH poslužitelju na dns (samo s racunala admin iz lokalne mreže "Private")
# 
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -p tcp -s 10.0.0.20 -i eth1 -d 203.0.113.200 --dport 22 -j ACCEPT
# 
# S www je dozvoljen pristup poslužitelju database (Private) na TCP portu 10000 te pristup 
# DNS poslužiteljima u Internetu (UDP i TCP port 53).
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -p tcp -s 203.0.113.100 -i eth2 -d 10.0.0.100  --dport 1000 -j ACCEPT
$IPT -A FORWARD -p tcp -s 203.0.113.100 -o eth0  --dport 53 -j ACCEPT
#
# ... S www je zabranjen pristup svim ostalim adresama i poslužiteljima.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth1 -s 203.0.113.100 -j DROP
#
#
# Pristup svim ostalim adresama i poslužiteljima u DMZ je zabranjen.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A OUTPUT -o eth1 -j DROP
#
# Pristup SSH poslužitelju na cvoru database, koji se nalazi u lokalnoj mreži "Private", 
# dozvoljen je samo racunalima iz mreže "Private".
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A OUTPUT -o eth1 -p tcp --dport 22 -j DROP
#
# Web poslužitelju na cvoru database, koji sluša na TCP portu 10000, može se pristupiti
# iskljucivo s racunala www koje se nalazi u DMZ (i s racunala iz mreže "Private").
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -o eth1 -p tcp --dport 1000 -s 203.0.113.100 -d 10.0.0.100 -j ACCEPT
#
# S racunala database je zabranjen pristup svim uslugama u Internetu i u DMZ.
#
# <--- Na odgovarajuce mjesto dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth1 -s 10.0.0.100 -j DROP
# Zabranjen je pristup svim ostalim uslugama na poslužitelju database (iz Interneta i iz DMZ)
#
# <--- Na odgovarajuce mjesto dodajte pravila (ako je potrebno)
$IPT -A FORWARD -o eth1 -j DROP
#
# S racunala iz lokalne mreže "Private" (osim s database) se može pristupati svim racunalima 
# u Internetu ali samo korištenjem protokola HTTP (tcp/80 i tcp/443) i DNS (udp/53 i tcp/53).
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD  -o eth0 -s 10.0.0.20 -p tcp --dport 80 -j ACCEPT # admin
$IPT -A FORWARD  -o eth0 -s 10.0.0.20 -p tcp --dport 443 -j ACCEPT
$IPT -A FORWARD  -o eth0 -s 10.0.0.21 -p tcp --dport 80 -j ACCEPT # pc
$IPT -A FORWARD  -o eth0 -s 10.0.0.21 -p tcp --dport 443 -j ACCEPT
$IPT -A FORWARD  -o eth0 -s 10.0.0.21 -p tcp --dport 53 -j ACCEPT # DNS
$IPT -A FORWARD  -o eth0 -s 10.0.0.21 -p udp --dport 53 -j ACCEPT
#
# Pristup iz vanjske mreže u lokalnu LAN mrežu je zabranjen.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth0 -o eth1 -j DROP 
#
# Na FW je pokrenut SSH poslužitelj kojem se može pristupiti samo iz lokalne mreže "Private"
# i to samo sa cvora admin.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A INPUT -i eth1 -p tcp --dport 22 -s 10.0.0.20 -d 10.0.0.1 -j ACCEPT

#
# Pristup svim ostalim uslugama (portovima) na cvoru FW je zabranjen.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A INPUT -i eth1 -d 10.0.0.1 -j DROP
$IPT -A INPUT -i eth0 -d 192.168.1.2 -j DROP
$IPT -A INPUT -i eth2 -d 203.0.113.1 -j DROP
