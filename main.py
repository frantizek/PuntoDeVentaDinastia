""" importing required modules """
import os
import sys
import menu_utilities


def clear_screen():
    """Clean the screen so the script can display the new options.

    Args: None

    Returns: Nothing
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def operate_menu(menu_tuple, options):
    """Contains the logic to move within the options delivered in the menu to the user

    Args: 
         - menu_tuple: contains the pairs of displayed options and the corresponding action 
                       this can take you to another menu, process data or end the script.
         - options: matches the displayed menu number, with the actual number of options allowing
                    the logic to contain the specific number of choices

    Returns: Nothing
    """
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
    """Prints a string, then exit the program.

    Args: None

    Returns: Nothing
    """
    print("\n\n¡Namasté!\n")
    sys.exit()


def dummy_function():
    """This is a dummy function, that only prints a line. 
    Should be replaced later with the proper function.

    Args: None

    Returns: Nothing
    """
    print('\nEsta función no hace nada.\n')


def main():
    operate_menu(menu_utilities.main_menu, menu_utilities.FOUR_MENU_OPTIONS)


if __name__ == "__main__":
    main()
