def view_data(data):
    print(data)


def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def number_find_worker():
    return input("Введите ФИО сотрудника для поиска: ")


def number_find_post():
    return input("Введите должность сотрудников для поиска: ")

def number_find_salary():
    return [input("Введите нижний предел зарплаты: "), input("Введите верхний предел зарплаты: ")]

def number_delete_worker():
    return input("Введите ФИО сотрудника для удаления: ")

def number_update_worker():
    return input("Введите ФИО сотрудника для обновления: ")


