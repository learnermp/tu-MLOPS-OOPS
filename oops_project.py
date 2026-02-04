class ChatBook:
    __user_id = 0  # class variable to keep track of user IDs
    def __init__(self):
        self.__name = "Encapsulated Man"
        self.id = ChatBook.__user_id
        ChatBook.__user_id += 1  # Increment the class variable for the next user
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()
    # getter and setter   
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    @staticmethod
    def get_id(): # self is not required for static method
        return ChatBook.__user_id
    
    @staticmethod 
    def set_id(new_id): # self is not required for static method
        ChatBook.__user_id = new_id
    def menu(self):
        user_input = input(""" Welcome to chatbook! How you want to proceed?
                           1. press 1 to signup
                           2. press 2 to login
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit
                           
                           -->>""")
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.send_message()
        else:
            print("Exiting the application. Goodbye!")
            return
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
    def write_post(self):  
        if self.loggedin:
            post_content = input("Write your post here: ")
            print(f"Post published successfully!: {post_content}")
        else:
            print("Please login to write a post.")
        self.menu()

    def send_message(self):
        if self.loggedin:
            friend = input("Enter your friend's username: ")
            message = input("Enter your message: " )
            print(f"Message sent to {friend}: {message}")
        else:
            print("Please login to send messages.")
        self.menu()

if __name__ == "__main__":
    user1 = ChatBook()
    print(user1.id)
    user2 = ChatBook()
    print(user2.id)
    ChatBook.set_id(10) # staticmethod is accessed using class name
    print(ChatBook.get_id()) # staticmethod is accessed using class name
    user3 = ChatBook()
    print(user3.id)
    user4 = ChatBook()
    print(user4.id)
    print(user2.get_name())
    user2.set_name("NewName")
    print(user2.get_name())
