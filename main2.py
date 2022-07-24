# sudo mount -t tmpfs -o size=4G myramdisk /tmp/ramdisk
# openssl enc -aes-256-cbc -pbkdf2 -in teste.txt -out teste.enc -pass pass:senha.txt
# openssl enc -d -aes-256-cbc -pbkdf2 -in teste.enc -out saida.txt -pass pass:senha.txt

import itertools
import string
import time

lettersSize = 26
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
              # abcdefghijklmnopqrstuvwxyz
# ponctuations = "@8__3___1_____0___$_______"
ponctuations = "@310$8"
ponctuationsRepresents = "aeiosb"
# ponctuations = string.punctuation
outputFilename = "saida.txt"

def manipulateFiles(inputFilename="pokemonNames.txt"):
    inputFile = open(inputFilename, "r")
    # outputFile = open(outputFilename, "w")
    
    words = []

    print("ola")

    for x in inputFile:
        
        string = map(''.join, itertools.product(*zip(x.upper(), x.lower())))

        
        for y in string:
            # string1 = map(y.join, itertools.product(*zip(y, ponctuations)))
            if y not in words:
                # outputFile.write(y)
                words.append(y)
        
        # generateWords()

    inputFile.close()
    # outputFile.close()

    return words

def writeFile(words):
    outputFile = open(outputFilename, "w")
    for y in words:
        outputFile.write(y)
    
    outputFile.close()

    
def generateWords(word, uppercase = False):
    if uppercase == False:
        for j in range(word.count("a")):
            tempWord = word.replace("a", "$", j+1)
            print(tempWord)
        word = word[::-1]
        for j in range(word.count("a") - 1):
            tempWord = word.replace("a", "$", j+1)
            print(tempWord[::-1])
    else:
        for i in range(len(ponctuationsRepresents)):
            # print("representa: " + ponctuationsRepresents[i].upper())
            # print("certo: " + ponctuations[i].upper())
            # print("quantidade: " + str(word.count(ponctuationsRepresents[i].upper())))
            if word.count(ponctuationsRepresents[i].upper()) == 0:
                continue
            else:
                # print("ahsjhdgashdgsajhgdhjasgdhjasgdhjasgdhjagshjdgashjdgjhas")
                for j in range(word.count(ponctuationsRepresents[i].upper())):
                    tempWord = word.replace(ponctuationsRepresents[i].upper(), ponctuations[i], j+1)
                    print( tempWord)
                tempWord1 = word[::-1]
                for j in range(tempWord1.count(ponctuationsRepresents[i].upper())-1):
                    tempWord = tempWord1.replace(ponctuationsRepresents[i].upper(), ponctuations[i], j+1)
                    print(tempWord[::-1])
        

def run():
    t0 = time.time()
    words = manipulateFiles()
    t1 = time.time()
    print("Tempo de duracao: " + str(t1-t0))
        
    t0 = time.time()
    writeFile(words)
    t1 = time.time()

    print("Tempo de duracao: " + str(t1-t0))

    # generateWords(word="gabriela", uppercase=False)
    # generateWords(word="GABRIELA", uppercase=True)

if __name__ == "__main__":
    run()
