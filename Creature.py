import time

class Creature:
    def __init__(self, life, defense, damage):
        self.level = 1
        self.experience = 0
        self.life = life
        self.defense = defense
        self.damage = damage
        self.critical = 10

    def attack(self, target):
        target.life -= max(0, self.damage - target.defense)

    def attack_creature(self, hero, creature):
        while True:
            print("Now you are attacking creatures.")
            time.sleep(2)
            hero.attack(creature)
            if creature.life <= 0:
                print("Creature is dead. You won!")
                break
            print(f"Creature has {creature.life} life left.")
            time.sleep(2)

            print("Now the creature is attacking you.")
            time.sleep(2)
            creature.attack(hero)
            if hero.life <= 0:
                print("You are dead. You lost!")
                break
            print(f"You have {hero.life} life left.")

    def main(self):
        hero = Creature(100, 10, 20)  # Example stats for the hero
        creature = Creature(50, 5, 15)  # Example stats for the creature

        print("""
              1 - Attack Creatures
              2 - Attack Boss
              """)
        choice = int(input("What do you want to do? "))
        if choice == 1:
            self.attack_creature(hero, creature)

# Run the game
game = Creature(100, 10, 20)
game.main()
