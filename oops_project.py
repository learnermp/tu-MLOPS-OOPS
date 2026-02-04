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
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Exiting the application. Goodbye!")
            exit()
            # return
    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print(f"User {self.username} signed up successfully!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == "":
            print("No user found. Please sign up first.")
            self.menu()
        else:
            uname = input("enter your email/username here: ")
            pword = input("enter your password here: ")
            if self.username == uname and self.password == pword:
                self.loggedin = True
                print(f"Welcome back, {self.username}!")
            else:
                print("Invalid credentials. Please try again.")
                print("\n")
                self.menu()

if __name__ == "__main__":
    obj = ChatBook()