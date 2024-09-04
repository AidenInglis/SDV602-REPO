import PySimpleGUI as sg
from command_parser import parse_command
from story import show_current_place, game_places, get_game_state
from status import player_status, monster_status  # Assuming these return health and strength details
from inventory import has_item

def make_a_window():
    sg.theme('Dark Blue 3')
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(key='-IN-', size=(20, 1), font='Any 14')]
    current_state = get_game_state()
    print(f"Creating window for game state: {current_state}")

    if current_state == 'BossFight':
        # Boss Room layout with combat actions and stats
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Attack'), sg.Button('Heal')]
        image_file = r'assets/boss.png'
        stats_layout = [
            [sg.Text(f"Player Health: {player_status['health']}", key='-PLAYER-HEALTH-'), 
             sg.Text(f"Player Strength: {player_status['strength']}", key='-PLAYER-STRENGTH-')],
            [sg.Text(f"Monster Health: {monster_status['health']}", key='-MONSTER-HEALTH-'), 
             sg.Text(f"Monster Strength: {monster_status['strength']}", key='-MONSTER-STRENGTH-')]
        ]
        heal_button = sg.Button('Heal', disabled=not has_item('health_potion'))
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Attack'), heal_button]
    elif current_state == 'Room3':
        # Regular layout for other rooms
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Pickup')]
        image_file = r'assets/forest.png'
        stats_layout = [
            [sg.Text(f"Player Health: {player_status['health']}", key='-PLAYER-HEALTH-'),
             sg.Text(f"Player Strength: {player_status['strength']}", key='-PLAYER-STRENGTH-')]
        ]
    else:
        # Regular layout for other rooms
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
        image_file = r'assets/forest.png'
        stats_layout = [
            [sg.Text(f"Player Health: {player_status['health']}", key='-PLAYER-HEALTH-'),
             sg.Text(f"Player Strength: {player_status['strength']}", key='-PLAYER-STRENGTH-')]
        ]

    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [
        [sg.Image(image_file, size=(100, 100), key="-IMG-"), 
         sg.Text(show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
        *stats_layout,  # Include stats if available
        [command_col]
    ]
    
    return sg.Window('Adventure Game', layout, size=(520, 400))

if __name__ == "__main__":
    window = make_a_window()
    previous_state = get_game_state()

    while True:
        event, values = window.read()

        if event == 'Enter':
            current_story = parse_command(values['-IN-'])
            window['-OUTPUT-'].update(current_story)
            window['-IMG-'].update(game_places[get_game_state()]['Image'], size=(100, 100))
            
            if get_game_state() in ['Room3', 'BossRoom', 'BossFight']:
                if previous_state != get_game_state():
                    window.close()
                    window = make_a_window()

            previous_state = get_game_state()

        elif event in ['Attack', 'Heal']:
            action_result = parse_command(event.lower())
            window['-OUTPUT-'].update(action_result)

            if get_game_state() == 'BossFight':
                window['-PLAYER-HEALTH-'].update(f"Player Health: {player_status['health']}")
                window['-PLAYER-STRENGTH-'].update(f"Player Strength: {player_status['strength']}")
                window['-MONSTER-HEALTH-'].update(f"Monster Health: {monster_status['health']}")
                window['-MONSTER-STRENGTH-'].update(f"Monster Strength: {monster_status['strength']}")

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break

    window.close()
