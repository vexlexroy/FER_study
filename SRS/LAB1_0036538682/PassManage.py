from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes as salt_gen
import time
import json
import random
import sys


class PassManager:

    glavna_lozinka=None
    cipher=None
    hasher=SHA256.new()
    file_path = "manager.json" #format checkdata = encripted message, field[(addres, pass, hash)]

    def __init__(self):
        pass

    def shift(self,shift, byte_array):
        shift=shift*8
        shift %= len(byte_array)
        return byte_array[shift:] + byte_array[:shift]

    def init_cipher(self,salt):
        derive= PBKDF2(self.glavna_lozinka, b'', dkLen=32)
        self.cipher=AES.new(derive, AES.MODE_GCM, nonce=salt)

    def hash_message(self, msg):
        hashed=""
        self.hasher.update(msg.encode())
        hash_value_bytes = self.hasher.digest()
        hashed=hash_value_bytes.hex()
        self.hasher=SHA256.new()
        return hashed
    
    def hash_file_write(self,json_data):
        json_data["hash"]=""
        json_data["salt0"]=""
        #print(json_data)
        js_str=json.dumps(json_data)
        f_hash=self.hash_message(js_str)
        salt0=salt_gen(12)
        f_hash_encoded=self.message_encriptor(f_hash,salt0)
        json_data["hash"]=f_hash_encoded
        json_data["salt0"]=salt0.hex()
        js_str=json.dumps(json_data)
        with open(self.file_path, "w") as w:
            w.write(js_str)
        return
        
    def check_file_hash(self):
        json_data=""
        try: 
            with open(self.file_path, "r") as r:
                json_data=json.load(r)
            cripthash=bytes.fromhex(json_data["hash"])
            salt0=bytes.fromhex(json_data["salt0"])
            oldhash=self.message_decriptor(cripthash,salt0)
        except:
            return False
        json_data["hash"]=""
        json_data["salt0"]=""
        str_json=json.dumps(json_data)
        newhash=self.hash_message(str_json)
        # print(oldhash, newhash)
        if(oldhash==newhash):
            return True
        else:
            return False


    def message_encriptor(self, msg, salt):
        if(self.glavna_lozinka!=None):
            self.init_cipher(salt)
            encripted=self.cipher.encrypt(msg.encode()).hex()
            return encripted
        else:
            return False



    def message_decriptor(self, msg, salt):
        if(self.glavna_lozinka!=None):
            self.init_cipher(salt)
            try:
                decripted=self.cipher.decrypt(msg)
                decripted=decripted.decode("utf-8")
            except:
                return False
            return decripted
        else:
            return False


    def check_master(self, lozinka): # check if master pass hash correct
        self.glavna_lozinka=lozinka
        if(not self.check_file_hash()):
                    print(colors.RED + "Kriva Lozinka, ili Ne Autorizirana promijena podataka" + colors.RESET)
                    sys.exit()
        fraza="ISPRAVNOdefiniranaLozinkaSlobodanUlaz"
        with open(self.file_path, "r") as r:
            j_data=json.load(r)
        check=bytes.fromhex(j_data["check"])
        salt1=bytes.fromhex(j_data["salt1"])
        # print(check,"  ",salt1)
        saved_fraza=self.message_decriptor(check, salt1)
        if(fraza==saved_fraza):
            return True
        else:
            self.glavna_lozinka=None
            return False
        
        
    def create_manager(self): #add master password
        self.new_salt0=salt_gen(16).hex()
        fraza="ISPRAVNOdefiniranaLozinkaSlobodanUlaz"
        lozinka=input("Upisite glavnu lozinku: ")
        self.glavna_lozinka=lozinka
        salt1=salt_gen(12)
        encripted_checker=self.message_encriptor(fraza, salt1)
        data={
            "hash" : "",
            "salt0" : "",
            "salt1" : salt1.hex(),
            "check" : encripted_checker,
            "data" : {} #dict (addresa: (pass, salt))
        }
        self.hash_file_write(data)
        return
    
    def create_manager_pass(self, Mpass): #add master password
        self.new_salt0=salt_gen(16).hex()
        fraza="ISPRAVNOdefiniranaLozinkaSlobodanUlaz"
        lozinka=Mpass
        self.glavna_lozinka=lozinka
        salt1=salt_gen(12)
        encripted_checker=self.message_encriptor(fraza, salt1)
        data={
            "hash" : "",
            "salt0" : "",
            "salt1" : salt1.hex(),
            "check" : encripted_checker,
            "data" : {} #dict (addresa: (pass, salt))
        }
        self.hash_file_write(data)
        return

    def add_new_pass(self): # adds new entry into db
        fraza="ISPRAVNOdefiniranaLozinkaSlobodanUlaz"
        new_addres=input("Upisite Addresu: ")
        new_lozinka=input("Upisite Lozinku: ")
        new_salt=salt_gen(12)
        new_entry={
            self.message_encriptor(new_addres,self.shift(1,new_salt)):(self.message_encriptor(new_lozinka,new_salt),new_salt.hex())
            }
        j_loaded=""
        j_new={}
        with open ( self.file_path, "r") as r:
            j_loaded=json.load(r)
        data=j_loaded["data"]
        if(self.get_with_addres(new_addres)):
            _,_,hashadd=self.get_with_addres(new_addres)
            del data[hashadd]
        data.update(new_entry)
        # print(data)
        salt1=salt_gen(12)
        encripted_checker=self.message_encriptor(fraza, salt1)
        j_new=j_loaded
        j_new["data"]=data
        j_new["check"]=encripted_checker
        j_new["salt1"]=salt1.hex()
        # print(j_new)
        self.hash_file_write(j_new)
        return

    def add_new_pass2(self, new_addres, new_lozinka): # adds new entry into db
        fraza="ISPRAVNOdefiniranaLozinkaSlobodanUlaz"
        new_salt=salt_gen(12)
        new_entry={
            self.message_encriptor(new_addres,self.shift(1,new_salt)):(self.message_encriptor(new_lozinka,new_salt),new_salt.hex())
            }
        j_loaded=""
        j_new={}
        with open ( self.file_path, "r") as r:
            j_loaded=json.load(r)
        data=j_loaded["data"]
        if(self.get_with_addres(new_addres)):
            _,_,hashadd=self.get_with_addres(new_addres)
            del data[hashadd]
        data.update(new_entry)
        # print(data)
        salt1=salt_gen(12)
        encripted_checker=self.message_encriptor(fraza, salt1)
        j_new=j_loaded
        j_new["data"]=data
        j_new["check"]=encripted_checker
        j_new["salt1"]=salt1.hex()
        # print(j_new)
        self.hash_file_write(j_new)
        return


    def decript_data_entry(self, key, entry):
        # print(entry)
        salt=entry[1]
        adresa=self.message_decriptor(bytes.fromhex(key),self.shift(1,bytes.fromhex(salt)))
        lozinka=self.message_decriptor(bytes.fromhex(entry[0]),bytes.fromhex(salt))
        # print(adresa, lozinka)
        return adresa, lozinka, key


    def get_with_addres(self, addres):
        j_data=""
        with open(self.file_path, "r") as r:
            j_data=json.load(r)
            # print(j_data["data"])
        for i,x in enumerate(j_data["data"]):
            add,loz, hashadd=self.decript_data_entry(x,j_data["data"][x])
            if(add==addres):
                return loz, add, hashadd
        return False


    def manager_menue(self): # enter master pass
        while(True):
            lozinka = input("Upisite Lozinku:")
            if(self.check_master(lozinka)):
                self.glavna_lozinka=lozinka
                print("Izaberite uslugu.")
                print(colors.GREEN + "Dodavanje Lozinke: D" + colors.RESET)
                print( colors.GREEN+ "Dohvati Lozinku: A" + colors.RESET)
                print(colors.YELLOW + "Izlaz iz Managera: X" +colors.RESET)
                while(True):
                    selector=input(":").upper()
                    if(selector=="D"):
                        self.add_new_pass()
                    if(selector=="A"):
                        add=input("Addresa: ")
                        if(self.get_with_addres(add)):
                            loz,add,_= self.get_with_addres(add)
                            print(colors.YELLOW + add +" "+ colors.GREEN+ loz + colors.RESET)
                        else:
                            print(colors.BLUE + "Nema zadane adrese" + colors.RESET)
                        # print(loz,"  ", adresa)
                    elif(selector=="X"):
                        self.glavna_lozinka=None
                        self.main_menue()
            else:
                print(colors.RED + "kriva lozinka" + colors.RESET)
                print("Pricekajte random sekundi")
                time.sleep(random.randint(1, 15))


    def main_menue(self):
        exists=False
        u_colour=colors.GREEN
        try:
            with open(self.file_path, "r") as r:
                exists=True
        except:
            exists=False
            u_colour=colors.RED
        print("Izaberite uslugu.")
        print(colors.GREEN + "Kreiranje Managera: K" + colors.RESET)
        print(u_colour +"Ulazak u Managera: U" + colors.RESET)
        while(True):
            selector=input(": ").upper()
            if(selector=="K"):
                self.create_manager()
            elif(selector=="U" and exists):
                self.manager_menue()
        return


class colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'



def main():
    print("menue")
    manager.main_menue()
    return

def init(master_pass):
    manager.create_manager_pass(master_pass)
    print(colors.GREEN+"Kreiro managera"+colors.RESET)
    return

def addnew(masterpass, addres, newpass):
    if manager.check_master(masterpass):
        manager.add_new_pass2(addres, newpass)
        print(colors.GREEN+"Nova lozinka dodana"+colors.RESET)
    else:
        print(colors.RED+"Krivi master password"+colors.RESET)
    return

def get(masterpass, addres):
    if manager.check_master(masterpass):
        if(manager.get_with_addres(addres)):
            loz,add,_= manager.get_with_addres(addres)
            print(colors.YELLOW + add +" "+ colors.GREEN+ loz + colors.RESET)
        else:
            print(colors.BLUE + "Nema zadane adrese" + colors.RESET)
    else:
        print(colors.RED+"Krivi master password"+colors.RESET)

def testSwitchTwo():
    with open(manager.file_path, "r") as r:
        j_data=json.load(r)
    j_new=j_data
    list_d=list(j_new["data"])
    d1=j_new["data"][list_d[1]]
    d2=j_new["data"][list_d[0]]
    j_new["data"][list_d[0]]=d1
    j_new["data"][list_d[1]]=d2
    j_str=json.dumps(j_new)
    with open(manager.file_path, "w") as w:
        w.write(j_str)

if __name__ == "__main__":
    manager = PassManager()
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:]
        try:
            getattr(sys.modules[__name__], command)(*args)
        
        except SystemExit:
            sys.exit()
        except (AttributeError, TypeError):
            print("Ne postoji naredba, naredbe koje postoje:")
            print(colors.YELLOW +"main" + colors.RESET)
            print(colors.YELLOW +"init" + colors.RESET, "masterPassword")
            print(colors.YELLOW +"addnew" + colors.RESET, "masterPassword newAddres newPassword")
            print(colors.YELLOW +"get" + colors.RESET, "masterPassword getAddres")





