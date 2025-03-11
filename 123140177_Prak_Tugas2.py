import random

class Robot:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack_enemy(self, enemy):
        # Membuat sistem serangan robot bisa meleset dengan kemungkinan 20%
        if random.random() < 0.2:
            heal_amount = random.randint(5, 15)  # Jika meleset maka robot akan mendapatkan pemulihan HP
            enemy.hp += heal_amount
            print(f"{self.name} menyerang {enemy.name} tetapi meleset! {enemy.name} memulihkan {heal_amount} HP!")
        else:
            damage = random.randint(10, 20)  #Serangan robot di setting acak antara 10-20
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan menyebabkan {damage} damage!")

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def play_round(self):
        print(f"{self.robot1.name} HP: {self.robot1.hp}")
        print(f"{self.robot2.name} HP: {self.robot2.hp}")

        # Serangan robot 1
        self.robot1.attack_enemy(self.robot2)
        if not self.robot2.is_alive():
            print(f"{self.robot2.name} kalah!")
            return False

        # Serangan robot 2
        self.robot2.attack_enemy(self.robot1)
        if not self.robot1.is_alive():
            print(f"{self.robot1.name} kalah!")
            return False

        return True

    def start_game(self):
        print("Pertarungan dimulai!")
        while self.play_round():
            pass
        print("Permainan selesai!")


robot1 = Robot("Ambatron", 100)
robot2 = Robot("Probe", 100)

game = Game(robot1, robot2)
game.start_game()