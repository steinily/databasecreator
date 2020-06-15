# /usr/bin/python3
import json

csaladNev = open("csaladnev.txt", "r", encoding="utf8") # Rengeteg csalednev txtben
utoNev = open("utonev.txt", "r", encoding="utf8")  # Rengeteg utonev txtben
email = open("email.txt", "r", encoding="utf8")  # Nehany email cim szolgaltato
userdatabase={}
dataBaseForTraining=open("db4.json", "x",encoding='utf8')
y=''

cnt=1
while cnt<200:
    userdatabase["id"]=cnt
    userdatabase["csaladnev"]=csaladNev.readline().strip('\n')+" "+utoNev.readline().strip('\n')
    userdatabase["email"]=csaladNev.readline().strip('\n')+utoNev.readline().strip('\n')+"@"+email.readline().strip('\n')
    cnt += 1
    y=json.dumps(userdatabase,ensure_ascii=False).encode('utf8')
    dataBaseForTraining.write(y.decode())
    print(y)       



