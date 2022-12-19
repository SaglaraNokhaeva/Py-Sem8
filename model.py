data = open('Database.txt','r',encoding='UTF-8')
DB =[]
for s in data.readlines():
    worker=dict(s.split("=") for s in s.split(","))
    DB.append(worker) 
data.close()
# print(DB)

find_key='Ivanov Ivan Ivanovich'

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
    return(list(filter(lambda item: item['fio'] == find_key, DB)))

def find_worker_post():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    return(list(filter(lambda item: item['post'] == find_key, DB)))

def find_worker_salary():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    return(list(filter(lambda item: (int(min_salary)<=int(item['salary'])) and (int(item['salary'])<=int(max_salary)), DB)))


def add_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    # find_key='Ivanov Ivan Ivanovich'
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    data.close
    new_worker =dict(fio=input("Введите ФИО: "), post=input("Введите должность: "),salary=input("Введите зарплату в рублях: "))
    data = open('Database.txt','a',encoding='UTF-8')
    data.write("\n")
    data.write('fio='+new_worker['fio'])
    data.write(',post='+new_worker['post'])
    data.write(',salary='+new_worker['salary'])
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
    new_DB=list(filter(lambda item: item['fio'] != find_key,DB))
    data = open('Database.txt','w',encoding='UTF-8')
    for item in new_DB:
        data.write('fio='+item['fio'])
        data.write(',post='+item['post'])
        data.write(',salary='+item['salary'])
    return new_DB
data.close()

def update_worker():
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    new_DB=list(filter(lambda item: item['fio'] != find_key,DB))
    data = open('Database.txt','w',encoding='UTF-8')
    for item in new_DB:
        data.write('fio='+item['fio'])
        data.write(',post='+item['post'])
        data.write(',salary='+item['salary'])
    new_worker =dict(fio=input("Введите ФИО: "), post=input("Введите должность: "),salary=input("Введите зарплату в рублях: "))
    new_DB.append(new_worker)
    data = open('Database.txt','a',encoding='UTF-8')
    data.write('fio='+new_worker['fio'])
    data.write(',post='+new_worker['post'])
    data.write(',salary='+new_worker['salary'])
    data.write("\n")
    return new_DB
data.close()


def exsport_csv():
    import csv    
    employee_info = ['fio', 'post', 'salary']
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    with open("people.csv", "w",encoding='utf8', newline="") as csv_file:
        j = csv.DictWriter(csv_file, fieldnames=employee_info)
        j.writeheader()
        j.writerows(DB)
data.close

def exsport_json():
    import json    
    employee_info = ['fio', 'post', 'salary']
    data = open('Database.txt','r',encoding='UTF-8')
    DB =[]
    for s in data.readlines():
        worker=dict(s.split("=") for s in s.split(","))
        DB.append(worker)
    final = json.dumps(DB, indent=2)
    data1 = open('people.json','a',encoding='UTF-8')
    data1.write(final) 
data.close  


     