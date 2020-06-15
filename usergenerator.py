# /usr/bin/python3
import json
import random

csaladNev = open("csaladnev.txt", "r", encoding="utf8")  # Rengeteg csalednev txtben
utoNev = open("utonev.txt", "r", encoding="utf8")  # Rengeteg utonev txtben
email = open("email.txt", "r", encoding="utf8")  # Nehany email cim szolgaltato
userdatabase = {}
try:
    dataBaseForTraining = open("db.json", "x", encoding='utf8') #elkeszitendo file ellenorzese.letezik vagy nem

except IOError :
    print("File is already exist please chose another name")
    newFileName = input("FileName: ((Please put '.json' at the end!! )) ")
    dataBaseForTraining = open(newFileName, "x", encoding='utf8')

dataBaseForTraining.write('''{"users":[ ''') # A fejlec megadasa.

dataBaseSize=int(input("How big Database is needed?"))
cnt = 1 
y = ''
while cnt < dataBaseSize+1:
    userdatabase["id"] = int(cnt)
    userdatabase["csaladnev"] =(csaladNev.readline().strip('\n')+" "+(utoNev.readline().strip('\n')
    userdatabase["email"] = csaladNev.readline().strip('\n')+utoNev.readline().strip('\n')+"@"+(email.readline().strip('\n')
    y = json.dumps(userdatabase, ensure_ascii=False).encode('utf8')
    dataBaseForTraining.write(y.decode())
    if cnt==dataBaseSize:
        dataBaseForTraining.write(']}')#lablec megadasa
    else:
        dataBaseForTraining.write(''',''')
    cnt += 1

print("Database is being created!")


#További adatok beszurasara is van lehetoseg a while alati reszben  olyan modon hogy az plusz sorban megadjuk az userdatabase key(kulcsat) illetve a hozza adni kivant erteket.
