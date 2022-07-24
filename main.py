import os

import subprocess

passwordsList = open("passwordsList.txt", "a")
cont = 0
wordlistNames = ["wordlistEndLCDP.txt", "wordlistEndPokemon.txt"]

def opensslFunction(f, j):
    global cont
    print("Arquivo cifrado " + str(j))
    for i in f:
        try:
            subprocess.check_output("openssl enc -d -aes-256-cbc -pbkdf2 -in ./cifrados/file" + str(j) + ".enc -out saidaDesc.txt -pass pass:" + i, shell=True, stderr=subprocess.STDOUT)
            
            checkFile = open("saidaDesc.txt", "r")
            valor = checkFile.read()
            if valor == "teste\n":
                print("\nSenha descoberta: " + i)
                print(cont)
                # f.close()
                passwordsList.write(i)
                checkFile.close()
            else:
                print("Nao encontrei")
                raise Exception("error")
        except KeyboardInterrupt:
            f.close()
            passwordsList.close()
            print("parada solicitada")
            exit(0)
        except subprocess.CalledProcessError as err:
            if cont % 10000 == 0:
                print(".")
            cont += 1
        except UnicodeDecodeError as err:
            pass
        except:
            pass
    return 0

try:
    for k in wordlistNames:
        for j in range(0, 3):
            print(k)
            f = open(k, "r")
            if opensslFunction(f, j) == 1:
                continue
            else:
                f = open(k, "r")
                opensslFunction(f, j)
            # f = open("sampleWordlist.txt", "r")
        

except KeyboardInterrupt:
    f.close()
    passwordsList.close()
    print("parada solicitada")
    exit(0)