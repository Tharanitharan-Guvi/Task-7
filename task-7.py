import datetime

def createFile():
    currTime = datetime.datetime.now()
    print(currTime)
    with open("timenow.txt", 'w') as file:
        file.write(str(currTime))

createFile()