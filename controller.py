import model
import view

def number_show_menu():
    value_1=view.show_menu()
    if value_1==1:
        value_2=view.number_find_worker()
        model.init(value_2)
        result=model.find_worker()
        view.view_data(result)