''' Constants needed to handle the menus '''
ONE_MENU_OPTIONS   = {'1': 0, '0': 1}
TWO_MENU_OPTIONS   = {'1': 0, '2': 1, '0': 2}
THREE_MENU_OPTIONS = {'1': 0, '2': 1, '3': 2, '4': 3}
FOUR_MENU_OPTIONS  = {'1': 0, '2': 1, '3': 2, '4': 3, '0': 4}
FIVE_MENU_OPTIONS  = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '0': 5}

# Available menues
ingresos_menu = ((
                     "[1] Ingreso de producto",
                     "[2] Regresar al menu principal.",
                     "[0] Salir del programa."),
                 ('dummy_function ()',
                  'operate_menu (menu_utilities.main_menu, menu_utilities.FOUR_MENU_OPTIONS)',
                  'exit_the_program ()'))

ventas_menu = ((
                    "[1] Captura venta",
                    "[2] Regresar al menu principal.",
                    "[0] Salir del programa."),
                ('dummy_function ()',
                 'operate_menu (menu_utilities.main_menu, menu_utilities.FOUR_MENU_OPTIONS)',
                 'exit_the_program ()'))

gastos_menu = ((
                    "[1] Captura gastos",
                    "[2] Regresar al menu principal.",
                    "[0] Salir del programa."),
                ('dummy_function ()',
                 'operate_menu (menu_utilities.main_menu, menu_utilities.FOUR_MENU_OPTIONS)',
                 'exit_the_program ()'))

corte_menu = ((
                    "[1] Genera corte semanal",
                    "[2] Regresar al menu principal.",
                    "[0] Salir del programa."),
                ('dummy_function ()',
                 'operate_menu (menu_utilities.main_menu, menu_utilities.FOUR_MENU_OPTIONS)',
                 'exit_the_program ()'))


main_menu = ((
                 "[1] Ingresos",
                 "[2] Ventas",
                 "[3] Gastos",
                 "[4] Corte Semanal",
                 "[0] Salir del programa."),
             ('operate_menu (menu_utilities.ingresos_menu, menu_utilities.TWO_MENU_OPTIONS)',
              'operate_menu (menu_utilities.ventas_menu, menu_utilities.TWO_MENU_OPTIONS)',
              'operate_menu (menu_utilities.gastos_menu, menu_utilities.TWO_MENU_OPTIONS)',
              'operate_menu(menu_utilities.corte_menu, menu_utilities.TWO_MENU_OPTIONS)',
              'exit_the_program ()'))
