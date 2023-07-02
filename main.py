import os

options_4 = {'1': 0, '2': 1, '3': 2, '4': 3, '0': 4}
options_2 = {'1': 0, '2': 1, '0': 2}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def operate_menu(menu_tuple, options):
    acceptable_options = options
    display_list = menu_tuple[0]
    command_list = menu_tuple[1]
    while True:
        clear_screen()
        for item in display_list:
            print(item)
        option = input('Teclea la opción: ')
        if option in acceptable_options:
            exec(command_list[acceptable_options[option]])
        else:
            print(f'\n{option} no es una opción aceptable.\n')


def exit_the_program():
    print("\n\n¡Namasté!\n")
    exit()


def dummy_function():
    print('\nEsta función no hace nada.\n')


ingresos_menu = ((
                     "[1] Ingreso de producto",
                     "[2] Regresar al menu principal.",
                     "[0] Salir del programa."),
                 ('dummy_function ()',
                  'operate_menu (main_menu, options_4)',
                  'exit_the_program ()'))

ventas_menu = ((
                    "[1] Captura venta",
                    "[2] Regresar al menu principal.",
                    "[0] Salir del programa."),
                ('dummy_function ()',
                 'operate_menu (main_menu, options_4)',
                 'exit_the_program ()'))

gastos_menu = ((
                    "[1] Captura gastos",
                    "[2] Regresar al menu principal.",
                    "[0] Salir del programa."),
                ('dummy_function ()',
                 'operate_menu (main_menu, options_4)',
                 'exit_the_program ()'))

corte_menu = ((
                    "[1] Genera corte semanal",
                    "[2] Regresar al menu principal.",
                    "[0] Salir del programa."),
                ('dummy_function ()',
                 'operate_menu (main_menu, options_4)',
                 'exit_the_program ()'))


main_menu = ((
                 "[1] Ingresos",
                 "[2] Ventas",
                 "[3] Gastos",
                 "[4] Corte Semanal",
                 "[0] Salir del programa."),
             ('operate_menu (ingresos_menu, options_2)',
              'operate_menu (ventas_menu, options_2)',
              'operate_menu (gastos_menu, options_2)',
              'operate_menu(corte_menu, options_2)',
              'exit_the_program ()'))

def main():
    operate_menu(main_menu, options_4)

if __name__ == "__main__":
    main()