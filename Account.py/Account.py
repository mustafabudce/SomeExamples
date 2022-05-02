import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("user created.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("User logged in")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("User logged out")

    def identity(self):
        if self.isLoggedIn:
            print(f"username : {self.currentUser.username}")
        else:
            print("Not logged in")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json", "w") as file:
            json.dump(list, file)


repository = UserRepository()

while True:
    print("Menu".center(50, "*"))
    choose = input("1-Register\n2-Login\n3-Logout\n4-İdentity\n5-Exit\nYour choose:")
    if choose == "5":
        break
    else:
        if choose == "1":
            username = input("username :")
            password = input("password :")
            email = input("email :")
            user = User(username=username, password=password, email=email)
            repository.register(user)
            print(repository.users)
        elif choose == "2":
            if repository.isLoggedIn:
                print("You have already logged in.")
            else:
                username = input("username :")
                password = input("password :")
                repository.login(username, password)
        elif choose == "3":
            repository.logout()
        elif choose == "4":
            repository.identity()
        else:
            print("wrong choose")
