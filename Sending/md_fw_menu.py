#This file will contain a menu option.
#It just have common menu with packet information and send packet
#if your program (Send/Receive)require more than that, please refer to it and make another one in main file.
def print_menu():
    cloop=True
    while cloop:
            print (22 * "-" , "MENU" , 22 * "-")
            print ("\t1. [Infor] {:<24} ".format("Packet information"))
            print ("\t2. [Send] {:<24} ".format("Packet Send"))
            print ("\t0. [Exit] {:<24} ".format("Exit"))
            print (50 * "-")
            try:
                choice =input("Enter your choice [0-2]: ")
                if (int(choice) >=0 and int(choice) <=2):
                    cloop = False
            except ValueError:
                print('Invalid input! Please enter a number between 0 and 2.')
            return choice

if __name__ == '__main__':
    choice = print_menu()
    print(f"You selected option {choice}.")