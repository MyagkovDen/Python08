import view
import model

def button_click():
    option = view.select_function()
    if option == 1: 
        model.input_text()
    elif option == 2:
        model.print_text()
    elif option == 3:
        model.check_text(input('Введите ключевое слово: '))
    elif option == 4:
        model.change_text()
    elif option == 5:
        model.delete_text()