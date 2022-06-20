import random

class Player:

    def __init__(self, pseudo, health, attack1, attack2, shield):
        self.pseudo = pseudo # set the name of the player
        self.health = health # set the health of the player
        self.attack1 = attack1 # set the damage of attack1 of the player
        self.attack2 = attack2 # set the damage of attack2 of the player
        self.shield = shield # set shield of the player, is in %
        self.protection = 0 # When the player want to use the shield, he have to transformed it into protection
        self.attack2_cooldown = 3 # set the cooldown of the attack2
        self.initial_stat = [self.health, self.attack1, self.attack2]
        print('Welcom', self.pseudo)
        self.show_stats()

    def show_stats(self): # show the health, the damage of the attack 1 and 2, the shield and the protection
        print('here is your stats : \n Health :', self.health, '/ Attack1 :', \
        self.attack1, ' / Attack2 :', self.attack2, ' / Shield :', self.shield, '%', ' / protection :', self.protection, '%')

    def use_attack1(self, enemy): # attack the enemy with attack1 (the monster), I put enemy in the case where I want to create a 2 player game
        enemy.monster_lose(self.attack1)
        if self.attack2_cooldown != 3:  # decrease the cooldown of the attack 2 if there is one
            self.attack2_cooldown += 1
        if self.shield != 100 and self.protection == 0: #add 25% to the shield if the player don't have protection and the shield isn't max 100
            self.shield += 25

    def use_attack2(self, enemy):# attack the enemy with attack2 (the monster)
        if self.attack2_cooldown == 3: # check if the player respect the cooldown
            self.attack2_cooldown = 1 # put the cooldown to 1
            enemy.monster_lose(self.attack2)
            if self.shield != 100 and self.protection == 0: # give shield
                self.shield += 25
        else:
            print("You can't do this now, you have to whait", 3 - self.attack2_cooldown, 'turn, before to do this')
            action(int(input('\n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n'))) # if the player don't respect the cooldown,
# he comeback to the action choise

    def use_shield(self): # transforme shield into protection
        self.protection += self.shield
        self.shield = 0
        print('You are protected of', self.protection, '% of the damage in the next attack')

    def protection_end(self): # remove the protection (it will be used after the monster attack)
        self.protection = 0

    def lose(self, damage): # player lose health (it will be used after the monster attack)
        damage = int(damage * (100 - self.protection) / 100) # use the protection
        self.health -= damage
        self.protection_end()
        space('the monster inflicted ' + str(damage) + ' damage on you')
        if self.health <= 0: # if the player no longer have health, he die
            self.dead()

    def dead(self): # if the player no longer have health, the game is over
        space('You are dead face of the ' + str(monster.number))
        if input('press a key to leave the game \n') != False:
            exit()

class Monster:

    def __init__(self, number, health, attack1, attack2): # setup monster
        self.number = number # How many monsters you faced
        self.health = health # The health of the actual monster
        self.attack1 = attack1 # the damage of the attack1 of the monser
        self.attack2 = attack2 # the damage of the attack1 of the monser
        self.initial_stat = [self.number, self.health, self.attack1, self.attack2]

    def monster_stats(self): # show the number, the health, the attack1 and the attack2 of the monster
        print('here is monster stats : \n number :', self.number, '/ Health :', self.health, \
        '/ Attack1 :', self.attack1, ' / Attack2 :', self.attack2)

    def monster_attack(self):# attack of the monster
        if random.randint(1, 3) == 3: # 1 chance out of 3 to do the attack2 and 2 chance out of 3 to do the attack1
            player.lose(self.attack2)
        else:
            player.lose(self.attack1)


    def monster_dead(self):# if the monster have no health
        print('You kill the monster', self.initial_stat[0], '!')
        self.number = self.initial_stat[0] + 1 # put the monster nomber + 1
        self.health = int(self.initial_stat[1] * random.uniform(1.05, 1.2)) # restores monster health and increases it
        self.attack1 = int(self.initial_stat[2] * random.uniform(1.05, 1.2)) #  increases monster attack1
        self.attack2 = int(self.initial_stat[3] * random.uniform(1.05, 1.2)) #  increases monster attack1

        player.health = int(player.initial_stat[0] + (player.initial_stat[0] * random.uniform(0.05, 0.2))) #restore and increases pleyer health
        player.attack1 = int(player.initial_stat[1] + (player.initial_stat[1] * random.uniform(0.05, 0.2))) # increases player attack1
        player.attack2 = int(player.initial_stat[2] + (player.initial_stat[2] * random.uniform(0.05, 0.2))) # increases player attack2

        self.initial_stat = [self.number, self.health, self.attack1, self.attack2]
        player.initial_stat = [player.health, player.attack1, player.attack2]
        action(int(input('\n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n'))) # start the fight whith the new monster


    def monster_lose(self, damage): # monster lose health
        self.health -= damage
        if self.health <= 0:
            self.monster_dead() # if the monster no long have health, it die
        else:
            space('You did ' + str(damage) + ' to the monster, now it have ' + str(self.health) + 'point of life')#show the attack impacts


def space(message): # make spaces and underscores to have a clean terminal
    print('\n \n \n \n \n _____________________________________________')
    print(message)

def action(event): # loop of the game
    if event == 0: # show player stats
        player.show_stats()
        action(int(input(' \n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n')))
    if event == 1: #show monster stats
        monster.monster_stats()
        action(int(input(' \n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n')))
    if event == 2: # use attack1
        player.use_attack1(monster)
    if event == 3: # use attack2
        player.use_attack2(monster)
    if event == 4: # use shield
        player.use_shield()
        action(int(input(' \n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n')))

    monster.monster_attack() # the monster attack

    action(int(input('\n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n')))

pseudo = input("Wath's your username? \n") # ask the player username
player = Player(pseudo, health=400, attack1=100, attack2=300, shield=100) # set the player assets
monster = Monster(number=1, health=500, attack1=120, attack2=300) # set the monster assets


action(int(input('\n \n Wath you wanna do ? \n press 0 to show your stats / press 1 to show the monster stats / \
press 2 to use attack1 / press 3 to use attack2 / press 4 to use shield \n'))) # start the first loop
