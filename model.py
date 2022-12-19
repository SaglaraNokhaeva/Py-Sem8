data = open('Database.txt','r',encoding='UTF-8')
DB =[]
for s in data.readlines():
    worker=dict(s.split("=") for s in s.split(","))
    DB.append(worker) 
data.close()
# print(DB)

find_key='Иванов Иван Иванович'

def init (f_k):
    global find_key
    find_key=f_k

def init1 (min_s, max_s):
    global min_salary
    global max_salary
    min_salary=min_s
    max_salary=max_s

def find_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    return(list(filter(lambda item: item['ФИО'] == find_key, DB)))

def find_worker_post():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    return(list(filter(lambda item: item['должность'] == find_key, DB)))

def find_worker_salary():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    return(list(filter(lambda item: (int(min_salary)<=int(item['зарплата'])) and (int(item['зарплата'])<=int(max_salary)), DB)))


def add_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    find_key='Иванов Иван Иванович'
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    data.close
    new_worker =dict(ФИО=input("Введите ФИО: "), должность=input("Введите должность: "),зарплата=input("Введите зарплату в рублях: "))
    data = open('Database.txt','a',encoding='UTF-8')
    data.write("\n")
    data.write('ФИО='+new_worker['ФИО'])
    data.write(',должность='+new_worker['должность'])
    data.write(',зарплата='+new_worker['зарплата'])
    data.write("\n")
    data.close()
    return new_worker


def delete_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    data.close
    new_DB=list(filter(lambda item: item['ФИО'] != find_key,DB))
    data = open('Database.txt','w',encoding='UTF-8')
    for item in new_DB:
        data.write('ФИО='+item['ФИО'])
        data.write(',должность='+item['должность'])
        data.write(',зарплата='+item['зарплата'])
    return new_DB
data.close()

def update_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    new_DB=list(filter(lambda item: item['ФИО'] != find_key,DB))
    data = open('Database.txt','w',encoding='UTF-8')
    for item in new_DB:
        data.write('ФИО='+item['ФИО'])
        data.write(',должность='+item['должность'])
        data.write(',зарплата='+item['зарплата'])
    new_worker =dict(ФИО=input("Введите ФИО: "), должность=input("Введите должность: "),зарплата=input("Введите зарплату в рублях: "))
    new_DB.append(new_worker)
    data = open('Database.txt','a',encoding='UTF-8')
    data.write("\n")
    data.write('ФИО='+new_worker['ФИО'])
    data.write(',должность='+new_worker['должность'])
    data.write(',зарплата='+new_worker['зарплата'])
    data.write("\n")
    return new_DB
data.close()
    

     