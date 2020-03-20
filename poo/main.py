class user :
    #class utilisateur
    def __init__(self, name, age):
    #attribution des variable
        self.name = name
        self.age = age
        self.id = id
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class root(user):
    def __init__(self, name, age, premium):
        super().__init__(name, age)
        self.premium = premium


utilisateurs1 = user("kali", 14)
superuser = root("root", 14, "premium")
print("Bienvenue", utilisateurs1.get_name(), "tu as", utilisateurs1.get_age(), "ans." )
print("Bienvenue", superuser.get_name(), "tu as", superuser.get_age(), "ans." )
