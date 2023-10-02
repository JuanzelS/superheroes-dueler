

import random  # Import the random module at the beginning

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''
        Return a random value between 0 and the
        initialized max_damage strength.
        '''
        # Generate a random value for the attack
        random_value = random.randint(0, self.max_damage)
        return random_value

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize a Hero object with a name and starting health.

        Args:
          name (str): The name of the hero.
          starting_health (int, optional): The starting health of the hero. Default is 100.
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []  # Initialize the abilities list for the hero

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
import random  # Import the random module at the beginning

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''
        Return a random value between 0 and the
        initialized max_damage strength.
        '''
        # Generate a random value for the attack
        random_value = random.randint(0, self.max_damage)
        return random_value

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize a Hero object with a name and starting health.

        Args:
          name (str): The name of the hero.
          starting_health (int, optional): The starting health of the hero. Default is 100.
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []  # Initialize the abilities list for the hero

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    

