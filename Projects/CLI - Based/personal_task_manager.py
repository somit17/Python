def print_Menu():
    """Show Main Menu"""
    print(f'1. Add a task')
    print(f'0. Exit')
    print('==============================================')
def main():
    while True:
        print_Menu()
        choice = input(f'Choose an option')

        if choice=='0':
            print(f'GoodBye')
            break

main()

