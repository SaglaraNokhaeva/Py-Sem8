data = open('Database.txt','r',encoding='UTF-8')
DB ={}
for s in data.readlines():
    DB.append(s) 
data.close()
print(DB)

def init (a):
    global flag
    flag=a