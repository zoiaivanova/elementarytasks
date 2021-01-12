from interfaces import ConsoleInterface
from luckytickets.fn_lucky_tickets.main import main as fn_luckytickets
from luckytickets.oop_lucky_tickets.main import main as oop_luckytickets

MENU_PROMPT_START = """
There are 4 tasks to choose:
1) luckytickets in OOP style
2) luckytickets in FN style
3) chessboard in OOP style
4) chessboard in FN style

Please enter one of the following options:

- press corresponding number key to enter task number
- 'q' to quit\n
"""
TASKS = {
    '1': fn_luckytickets,
    '2': oop_luckytickets

}


def main(interface):
    selected_option = interface.user_input(MENU_PROMPT_START).strip().lower()
    while selected_option != 'q':
        task_function = TASKS.get(selected_option)
        if task_function:
            task_function(interface)
        else:
            interface.user_output('You entered a non-existent task number')

        selected_option = interface.user_input(MENU_PROMPT_START).strip().lower()


if __name__ == '__main__':
    main(ConsoleInterface())
