PROGRAM_OPTIONS = """
    Please enter one of the following options:

    - (press any key) to enter height and width
    - 'q' to quit
    """
MENU_PROMPT_START = f"""
    Build a chessboard with given height and width. 
    An asterisk symbol(*) is a black cell and a space symbol( ) is a white cell
    This is an example for height = 4 and width = 12:
    * * * * * *
     * * * * * *
    * * * * * *
     * * * * * *
    {PROGRAM_OPTIONS}
    """
MENU_PROMPT_DURING_PROGRAM = f'\nWould you like to run this program again? {PROGRAM_OPTIONS}'
