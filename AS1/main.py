#SECTION - main.py
import PySimpleGUI as sg #import PySimpleGUI library
from command_parser import parse_command #parse the command
from story import show_current_place, game_places, get_game_state #game state and current place and places
from status import player_status, monster_status  #return health and strength details
from inventory import has_item#the player has the health potion or not

#SECTION - make_a_window function
def make_a_window():
    #this function creates a specific personalised windows based off of different game states.
    sg.theme('Dark Blue 3')
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(key='-IN-', size=(20, 1), font='Any 14')]
    current_state = get_game_state()
    print(f"Creating window for game state: {current_state}")#NOTE - for debugging

    if current_state == 'BossFight':
        # Boss Room layout with combat actions and stats
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Attack'), sg.Button('Heal')]
        image_file = r'assets/Boss.png'
        #the room layout with the presented stats.
        stats_layout = [
            [sg.Text(f"Player Health: {player_status['health']}", key='-PLAYER-HEALTH-'), 
             sg.Text(f"Player Strength: {player_status['strength']}", key='-PLAYER-STRENGTH-')],
            [sg.Text(f"Monster Health: {monster_status['health']}", key='-MONSTER-HEALTH-'), 
             sg.Text(f"Monster Strength: {monster_status['strength']}", key='-MONSTER-STRENGTH-')]
        ]
        heal_button = sg.Button('Heal', disabled=not has_item('health_potion'))
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Attack'), heal_button]

    elif current_state == 'Win':
        # Win screen layout
        buttons = [sg.Button('Exit')]
        image_file = r'assets/Boss.png' #random image
        stats_layout = [[sg.Text('Congratulations! You defeated the monster!', font='Any 18')]]

    elif current_state == 'Lose':
        # Lose screen layout
        buttons = [sg.Button('Exit')]
        image_file = r'assets/Boss.png'  #random image
        stats_layout = [[sg.Text('You were defeated by the monster. Better luck next time!', font='Any 18')]]

    elif current_state == 'Room3':
        # Regular layout for room3
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Pickup')]
        image_file = r'assets/forest.png'
        stats_layout = [
            [sg.Text(f"Player Health: {player_status['health']}", key='-PLAYER-HEALTH-'),
             sg.Text(f"Player Strength: {player_status['strength']}", key='-PLAYER-STRENGTH-')]
        ]


    else:
        # Regular layout for rooms 1-4 except 3
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
        image_file = r'assets/forest.png'
        #player health and attack stats
        stats_layout = [
            [sg.Text(f"Player Health: {player_status['health']}", key='-PLAYER-HEALTH-'),
             sg.Text(f"Player Strength: {player_status['strength']}", key='-PLAYER-STRENGTH-')]
        ]

    #Connect the input and buttons together
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    #sorts the overall layout for the window.
    layout = [
        [sg.Image(image_file, size=(100, 100), key="-IMG-"), 
         sg.Text(show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
        *stats_layout,  # Include stats if available
        [command_col]
    ]
    #return created windows
    return sg.Window('Adventure Game', layout, size=(520, 400))

# main.py
if __name__ == "__main__":
    window = make_a_window()#create window
    previous_state = get_game_state()#track prev state

    while True:
        event, values = window.read()#read inputs and button-presses

        if event == 'Enter':#handles when enter is pressed
            current_story = parse_command(values['-IN-'])#parse the command to get the current story
            window['-OUTPUT-'].update(current_story)
            window['-IMG-'].update(game_places[get_game_state()]['Image'], size=(100, 100))#updating image
            
            if get_game_state() in ['Room3', 'BossRoom', 'BossFight', 'Win', 'Lose']:
                #this was for debugging but turned out to be really helpful for getting data to refresh when i needed changes.
                if previous_state != get_game_state():
                    window.close()
                    window = make_a_window()

            previous_state = get_game_state()

        elif event == 'Pickup': 
            #for when pickup is called on room3
            pickup_message = parse_command('pickup')
            window['-OUTPUT-'].update(pickup_message)
            window['Pickup'].update(disabled=True)

        elif event in ['Attack', 'Heal']:
            #when player is in combat with monster
            action_result = parse_command(event.lower())#lowers the capitalisation of the letters
            window['-OUTPUT-'].update(action_result)

            if monster_status['health'] > 0:#if health is greater than 0 then attack
                monster_action_result = parse_command('monster_attack')
                current_output = window['-OUTPUT-'].get()  
                window['-OUTPUT-'].update(f"{current_output}\n{monster_action_result}")#update window text

                window['-PLAYER-HEALTH-'].update(f"Player Health: {player_status['health']}")#update player health
                window['-MONSTER-HEALTH-'].update(f"Monster Health: {monster_status['health']}")#update monster health
                
            if get_game_state() == 'BossFight':
                window['-PLAYER-HEALTH-'].update(f"Player Health: {player_status['health']}")#update player health
                window['-MONSTER-HEALTH-'].update(f"Monster Health: {monster_status['health']}")#update monster health

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:#handles the exit button.
            break

    window.close()
