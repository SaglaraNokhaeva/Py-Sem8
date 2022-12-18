data = open('Database.txt','r',encoding='UTF-8')
DB =[]
for s in data.readlines():
    worker=dict(s.split("=") for s in s.split(","))
    DB.append(worker) 
data.close()
print(DB)

# def init (a):
#     global flag
#     flag=a