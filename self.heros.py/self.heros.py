class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        found_hero = False
        # Loop through each hero in our list
        for hero in self.heroes:
            # If we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # Set our indicator to True
                found_hero = True
        # If we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not found_hero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # Add the Hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)
