import os


class instruction:

    def __init__(self, message):
        self.message = message
        self.dan = "0"

    def fonction_principal(self):
        print(self.message[0])
        print(self.message[1])
        print(self.message[2])
        print(self.message[3])
        print(self.message[4])

    def condition(self):
        self.dan = str(input("Quel nombre: "))
        if self.dan == "1":
            print("Vous avez choisi 1")
            os.system("echo 1")
        elif self.dan == "2":
            print("Vous avez choisi 2")
            os.system("echo 2")

        elif self.dan == "3":
            print("Vous avez choisi 3")
            os.system("echo 3")

        elif self.dan == "4":
            print("Vous avez choisi 4")
            os.system("echo 4")

        elif self.dan == "5":
            print("Vous avez choisi 5")
            os.system("echo 5")

        else:
            print("erreur veuliiez ressayer")
            os.system("echo pas repertorie")

    def get_dan(self):
        return self.dan



