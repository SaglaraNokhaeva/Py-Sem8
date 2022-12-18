# data = open('Database.txt','r',encoding='UTF-8')
# DB =[]
# for s in data.readlines():
#     worker=dict(s.split("=") for s in s.split(","))
#     DB.append(worker) 
# data.close()
# print(DB)

find_key='Иванов Иван Иванович'

def init (f_k):
    global find_key
    find_key=f_k

def find_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    print(list(filter(lambda item: item['ФИО'] == find_key, DB)))

find_worker()