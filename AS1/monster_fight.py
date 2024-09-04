# monster_fight.py

from status import player_status, monster_status, game_status
from story import game_state
import random

class MonsterFight:
    def __init__(self):
        self.game_status = game_status

    def check_conditions(self):
        if self.game_status == "active" and game_state == "BossFight":
            self.combat_loop()  # Start the combat loop if the game is active and in BossFight

    def combat_loop(self):
        while self.game_status == "active":
            if game_state == "BossFight":
                # You can invoke these methods directly based on commands
                print(self.player_attack())
                print(self.monster_attack())
                self.check_victory_conditions()

    def player_attack(self):
        player_damage = random.randint(player_status['strength'] - 10, player_status['strength'] + 10)
        monster_status['health'] -= player_damage
        return f"Player attacked monster for {player_damage} damage. Monster health: {monster_status['health']}"

    def player_heal(self):
        player_status['health'] += 10
        return f"Player healed for 10 health. Player health: {player_status['health']}"

    def monster_attack(self):
        monster_damage = random.randint(monster_status['strength'] - 10, monster_status['strength'] + 10)
        player_status['health'] -= monster_damage
        return f"Monster attacked player for {monster_damage} damage. Player health: {player_status['health']}"

    def check_victory_conditions(self):
        if player_status['health'] <= 0:
            self.game_status = "Defeat"
            self.on_defeat()
        elif monster_status['health'] <= 0:
            self.game_status = "Victory"
            self.on_victory()

    def on_defeat(self):
        print("You have been defeated")
        # Add logic to switch to the Lose window

    def on_victory(self):
        print("You have defeated the monster")
        # Add logic to switch to the Win window

# To use it:
# monster_fight = MonsterFight()
# monster_fight.check_conditions()  # Start the combat if conditions are met
