from User import User


class SocialNetwork:
    _net = None

    def __new__(cls, name):
        if cls._net is None:
            cls._net = super(SocialNetwork, cls).__new__(cls)
            cls._net.status = False
            print(f"The social network {name} was created!")
            return cls._net

    def __init__(self, name):
        if not SocialNetwork._net.status:
            self.name = name
            self.users = []
            SocialNetwork._net.status = True

    def sign_up(self, name, password):
        if 3 < len(password) < 9:
            if self.name_check(name) is None:
                temp = User(name, password)
                self.users.append(temp)
                return temp

    def name_check(self, name):
        for user in self.users:
            if name == user.name:
                return user
        return None

    def log_in(self, name, password):
        login_user = self.name_check(name)
        if login_user is not None:
            if login_user.pass_check(password):
                login_user.connect = True
                print(f"{name} connected")

    def log_out(self, name):
        logout_user = self.name_check(name)
        if logout_user is not None:
            logout_user.connect = False
            print(f"{name} disconnected")

    def __str__(self):
        network_string = f"{self.name} social network:\n"
        for user in self.users:
            network_string += user.__str__() + "\n"
        return network_string

