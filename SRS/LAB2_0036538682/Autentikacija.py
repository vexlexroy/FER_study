import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes as salt_gen
import time
import json
import os
import re
import argparse
import getpass


class colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'


# json = {userHash : (passHash, salt1, salt2, flag),} salt1 for nonce, salt2 for PBKD2

class Enkripcija:
    file_name=None
    cipher=None
    hasher=SHA256.new()

    def __init__(self, file):
        self.file_name=file
        return
    def init_cipher(self, isalt1, isalt2, lozinka):
        salt1 = bytes.fromhex(isalt1)
        salt2 = bytes.fromhex(isalt2)
        derive = PBKDF2(lozinka, salt2, dkLen=32)
        self.cipher=AES.new(derive, AES.MODE_GCM, nonce=salt1)
        
    def message_encriptor(self, msg:str, salt1, salt2, lozinka):
            self.init_cipher(salt1, salt2, lozinka)
            encripted=self.cipher.encrypt(bytes.fromhex(msg)).hex()
            return encripted

    def message_decriptor(self, msg:str, salt1, salt2, lozinka):
            self.init_cipher(salt1, salt2, lozinka)
            try:
                decripted=self.cipher.decrypt(bytes.fromhex(msg)).hex()
            except:
                return False
            return decripted
    
    def hash_message(self, msg:str):
        hashed=""
        self.hasher.update(msg.encode())
        hash_value_bytes = self.hasher.digest()
        hashed=hash_value_bytes.hex()
        self.hasher=SHA256.new()
        return hashed

    def file_writer(self, json_data:dict):
        try:
            with open(self.file_name, "r") as r:
                old_data:dict = json.load(r)["data"] 
            old_data.update(json_data)
            with open(self.file_name, "w") as w:
                json.dump({"data":old_data}, w)
            return True
        except Exception as e:
            print(e)
            return False
        
    def file_reader(self):
        try:
            with open(self.file_name, "r") as r:
                data:dict = json.load(r)["data"]
            return data
        except Exception as e:
            print(e)
            return False

    def save_user(self, user, password):
        curr_data:dict=self.file_reader()
        user_hash=self.hash_message(user)
        if(user_hash not in set(curr_data.keys())):
            salt1=salt_gen(12).hex()
            salt2=salt_gen(12).hex()
            hashPass=self.hash_message(password)
            encryptedHashPass=self.message_encriptor(hashPass, salt1, salt2, password)
            new_data={user_hash : (encryptedHashPass, salt1, salt2, False)}
        else:
            return False
        if(self.file_writer(new_data)):
            return True
        else:
            return False

    def update_user(self, user, newpassword):
        user_hash=self.hash_message(user)
        data:dict=self.file_reader()
        # print(data)
        if(data):
            if(user_hash in set(data.keys())):
                pas_hash=self.hash_message(newpassword)
                pkd_salt=salt_gen(12).hex()
                enc_salt=salt_gen(12).hex()
                pas_hash_enc = self.message_encriptor(pas_hash,enc_salt,pkd_salt,newpassword)
                edited_data={user_hash:(pas_hash_enc, enc_salt, pkd_salt, False)}
                if(self.file_writer(edited_data)):
                    return True
                else:
                    raise False
            else:
                return False
            
    def remove_user(self, user:str):
        hash_user=self.hash_message(user)
        current_data=self.file_reader()
        if(hash_user in set(current_data.keys())):
            del current_data[hash_user]
            with open(self.file_name, "w") as w:
                json.dump({"data":current_data}, w)
            return True
        else:
            return False


    def autenticate_password(self, user, password):
        current_data=self.file_reader()
        user_hash=self.hash_message(user)
        if(user_hash in set(current_data.keys())):
            user_data=current_data[user_hash]
            pass_hash=self.hash_message(password)
            decripted_hash=self.message_decriptor(user_data[0],user_data[1],user_data[2],password)
            if(pass_hash==decripted_hash):
                return True
            else:
                return False
        else:
            return False
        
    def set_flag(self, user:str, val:bool):
        current_data=self.file_reader()
        user_hash=self.hash_message(user)
        if(user_hash in set(current_data.keys())):
            update_data=list(current_data[user_hash])
            update_data[-1]=val
            if(self.file_writer({user_hash: tuple(update_data)})):
                return True
            else:
                return False
        else:
            return False
        
    def get_flag(self, user:str):
        current_data=self.file_reader()
        user_hash=self.hash_message(user)
        if(user_hash in set(current_data.keys())):
            return {"value":current_data[user_hash][-1]}
        else:
            return False
        
    
class Autentikator:
    enkriptor=None
    patern=re.compile("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!-/:-@[-`{-~]).{8,256}$")
    
    def __init__(self, file):
        if not os.path.exists(file):
            data={"data":{}}
            with open(file, "w") as w:
                json.dump(data, w)
        self.enkriptor=Enkripcija(file)
        return

    def add_user(self, uname):
        while(True):
            password=input(colors.CYAN + "Password: "+colors.RESET)
            while(not self.check_password_strenght(password)):
                print(colors.YELLOW + "Pre slaba lozinka bar:\njedno (malo,velio slovo)\njedan broj\njedan znak\ndljina 8 do 256"+ colors.RESET)
                password=getpass.getpass(colors.CYAN + "Password: "+colors.RESET)
            repitpassword=getpass.getpass(colors.CYAN + "Confirm Password: "+colors.RESET)
            if(repitpassword==password):
                break
        if(self.enkriptor.save_user(uname, password)):
            print(colors.GREEN + f"Uspjesna Registracija korisnika: {uname}" + colors.RESET)
        else:
            print(colors.RED + "Korisnicko ime vec postoji ili problem pri registraciji" + colors.RESET)
        return
    
    def update_user(self, uname, old_password=None):
        while(True):
            password=getpass.getpass(colors.CYAN + "Password: "+colors.RESET)
            while(not self.check_password_strenght(password) or password==old_password):
                print(colors.YELLOW + "Pre slaba lozinka bar:\njedno (malo,velio slovo)\njedan broj\njedan posebni znak\nduljina 8 do 256 znakova"+ colors.RESET)
                if(password==old_password):
                    print(colors.RED + "Nemozete koristiti istu lozinku" + colors.RESET)
                password=getpass.getpass(colors.CYAN + "Password: "+colors.RESET)
            repitpassword=getpass.getpass(colors.CYAN + "Confirm Password: "+colors.RESET)
            if(repitpassword==password):
                break
        if(self.enkriptor.update_user(uname, password)):
            print(colors.GREEN + "Uspjesna promjena lozinke" + colors.RESET)
        else:
            print(colors.RED + "Korisnik ne postoji ili je doslo do problema pri promijeni" + colors.RESET)
        return
        
    def force_user(self, uname):
        if (self.enkriptor.set_flag(uname, True)):
            print(colors.GREEN + "Zastavica Postavljena" + colors.RESET)
        else:
            print(colors.RED + "Korisnicko ime ne postoji ili problem pri postavljanju zastavice" + colors.RESET)
        return

    def autenticate_user(self, uname, password):
        if(x:=self.enkriptor.get_flag(uname)):
            if(self.enkriptor.autenticate_password(uname, password)):
                print(colors.GREEN + f"Uspjesna Prijava korisnika: {uname}" + colors.RESET)
                if(x["value"]):
                    print(colors.YELLOW + "Molim promijenite password" + colors.RESET)
                    self.update_user(uname, password)
            else:
                print(colors.RED + "Korisnicko ime ili lozinka neispravni" + colors.RESET)
        else:
            print(colors.RED + "Korisnicko ime ili lozinka neispravni" + colors.RESET)
        return

    def delete_user(self, uname):
        if(self.enkriptor.remove_user(uname)):
            print(colors.GREEN +"Korisnik Obrisan"+ colors.RESET)
        else:
            print(colors.RED +"Korisnik ne postoji"+ colors.RESET)

    def check_password_strenght(self, password):
        if(self.patern.search(password)):
            return True
        else:
            return False




if __name__ == "__main__":
    aut=Autentikator("data.json")
    pars=argparse.ArgumentParser()
    # parsing--------------------------------------------------------------
    user = pars.add_subparsers(dest="command", title="commands") # user sub parser
    usermgmt = user.add_parser('usermgmt', help='Execute usermgmt comand') #sub parser for usermgmt
    login = user.add_parser('login', help='Execute user login comand') #sub parser for login
    mgmt_comands=usermgmt.add_subparsers(dest="task", title="task")# comands sub parser for usermgmt

    c_add=mgmt_comands.add_parser('add')
    c_add.add_argument("uname", help="Username")

    c_del=mgmt_comands.add_parser('del')
    c_del.add_argument("uname", help="Username")

    c_force=mgmt_comands.add_parser('forcepass')
    c_force.add_argument("uname", help="Username")

    c_passwd=mgmt_comands.add_parser('passwd')
    c_passwd.add_argument("uname", help="Username")

    sys_args=sys.argv[1:]
    args=pars.parse_args(sys_args)
    if args.command=="usermgmt":
        if(args.task=="add"):
            aut.add_user(args.uname)
        if(args.task=="del"):
            aut.delete_user(args.uname)
        if(args.task=="forcepass"):
            aut.force_user(args.uname)
        if(args.task=="passwd"):
            aut.update_user(args.uname)
    elif args.command=="login":
        uname=input("Upisite ime: "+ colors.CYAN)
        password=getpass.getpass(colors.RESET+"Upisite Lozinku: ")
        aut.autenticate_user(uname, password)


