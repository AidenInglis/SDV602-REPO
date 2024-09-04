#SECTION - monster_fight.py

from status import player_status, monster_status
from story import game_state, set_game_state
import random #for the damage range

class MonsterFight:
    def __init__(self):
        self.game_status = "active"  # Initializes the game status

    def player_attack(self):
        #player attacks the monster handling
        if self.game_status == "active":
            player_damage = random.randint(player_status['strength'] - 10, player_status['strength'] + 10)#attack within a range.
            monster_status['health'] -= player_damage#health of the monster after the attack
            self.check_victory_conditions()#check if the player has won or lost
            return f"Player attacked monster for {player_damage} damage. Monster health: {monster_status['health']}"
        

    def player_heal(self):
        #the player heals themselves
        if self.game_status == "active":
            player_status['health'] += 10#add 10 health to the player
            return f"Player healed for 10 health. Player health: {player_status['health']}"

    def monster_attack(self):
        #monster attacks player
        if self.game_status == "active" and monster_status['health'] > 0:#if the monster is alive
            monster_damage = random.randint(monster_status['strength'] - 10, monster_status['strength'] + 10)#attacks within a range.
            player_status['health'] -= monster_damage#health - damage
            self.check_victory_conditions()#check if the player has won or lost
            print(f"Monster attacks player for {monster_damage} damage.")#for debugging
            print(f"Player health after attack: {player_status['health']}")#for debugging
            return f"Monster attacked player for {monster_damage} damage. Player health: {player_status['health']}"

    def check_victory_conditions(self):
        if player_status['health'] <= 0:#if the player's health is less than or equal to 0
            self.game_status = "Defeat"#set the game status to defeat
            self.on_defeat()#call the defeat function
        elif monster_status['health'] <= 0:#if the monster's health is less than or equal to 0
            self.game_status = "Victory"#set the game status to victory
            self.on_victory()#call the victory function

    def on_defeat(self):
        print("You have been defeated")
        set_game_state('Lose')#set the game state to lose
        print(game_state)


    def on_victory(self):
        print("You have defeated the monster")
        set_game_state('Win')#set the game state to win
        print(game_state)
