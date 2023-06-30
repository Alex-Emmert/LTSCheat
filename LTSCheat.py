#Alex Emmert
#June 29, 2023
#Cheat at the game "License To Spell" by SeattlePhysicsTeacher (https://www.seattlephysicstutor.com/plates.html)

with open("CSW21.txt", "r") as file:
    wordList = file.read().splitlines()

while True:
    plate = [*input("ENTER PLATE (Letters Only): ").upper()] #Takes input and casts into an array of chars
    validWords = []
    for word in wordList: #Inefficient
        if plate[0] in word and plate[1] in word[word.index(plate[0])+1:] and plate[2] in word[word.index(plate[0])+1:][word[word.index(plate[0])+1:].index(plate[1])+1:]:
            validWords.append(word)
    minLen = min(len(word) for word in validWords)
    if minLen < 4:
        minLen = 4
    for word in validWords: #Almost certainly a more efficient way of doing this; this is good enough for now
        if len(word) == minLen:
            print(word)
            break