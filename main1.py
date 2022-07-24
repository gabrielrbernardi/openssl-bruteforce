import itertools
import string

lettersSize = 26
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
              # abcdefghijklmnopqrstuvwxyz
ponctuations = "@310$8"
ponctuationsRepresents = "aeiosb"
# ponctuations = string.punctuation
outputFilename = "saida.txt"

def manipulateFiles(inputFilename="pokemonNames1.txt"):
    inputFile = open(inputFilename, "r")
    outputFile = open(outputFilename, "w")
	
    for name in inputFile:
        #name = f.readline()
        words = []
        name = name.replace("\n", "")
        tempName = ""
        for i in range(lettersSize):
            for j in range(name.count(lowercase[i])):
                tempName = name.replace(lowercase[i], uppercase[i], j)
                if (tempName not in words):
                    outputFile.write(tempName + "\n")
                    words.append(tempName)
            name = name.replace(lowercase[i], uppercase[i])
            #print("\n\n\n" + name)
            for j in range(name.count(uppercase[i])):
                tempName = name.replace(uppercase[i], lowercase[i], j)
                if (tempName not in words):
                    outputFile.write(tempName + "\n")
                    words.append(tempName)
            name = name.replace(uppercase[i], lowercase[i])
        # name = name.lower()
        # for i in range(len(name)):
        #     print(name.count(ponctuationsRepresents[i]))
        #     for j in range(name.count(ponctuationsRepresents[i])):
        #         tempName = name.replace(ponctuationsRepresents[i], ponctuations[i], j)
        #         # if (tempName not in words):
        #         outputFile.write(tempName + "\n")
        #         words.append(tempName)
        #         print(ponctuations[i])
                # else:
				
		#outputFile.write(words)
	
    outputFile.close()
		
def run():
    manipulateFiles()

if __name__ == "__main__":
    run()



