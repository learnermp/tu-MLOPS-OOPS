class ChatBook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(""" Welcome to chatbook! How you want to proceed?
                           1. press 1 to signup
                           2. press 2 to login
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit
                           """)
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Exiting the application. Goodbye!")
            exit()
            # return

if __name__ == "__main__":
    obj = ChatBook()