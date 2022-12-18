import model
import view

def number_show_menu():
    value_1=view.show_menu()
    if value_1==1:
        value_2=view.number_find_worker()
        model.init(value_2)
        result=model.find_worker()
        view.view_data(result)
    elif value_1==2:
        value_2=view.number_find_post()
        model.init(value_2)
        result=model.find_worker_post()
        view.view_data(result)
    elif value_1==3:
        values=view.number_find_salary()
        value_2=values[0]
        value_3=values[1]
        model.init1(value_2,value_3)
        result=model.find_worker_post()
        view.view_data(result)
    # elif value_1==4:

    # elif value_1==5:

    # elif value_1==6:

    # elif value_1==7:

    # elif value_1==8:

    # elif value_1==9:

    