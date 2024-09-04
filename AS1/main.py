# main_game.py

import PySimpleGUI as sg
from command_parser import parse_command
from story import show_current_place, game_places, game_state
from status import player_status, monster_status, game_status

def make_a_window():
    #making a window for the game
    if game_state == 'BossRoom':

        sg.theme('Dark Blue 3')
        prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(key='-IN-', size=(20, 1), font='Any 14')]
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit'), sg.Button('Attack'), sg.Button('Heal')]
        content = [sg.TAB_LOCATION_BOTTOM_LEFT](player_status)
        command_col = sg.Column([prompt_input, buttons], element_justification='r')
        layout = [
            [sg.Image(r'assets/boss.png', size=(100, 100), key="-IMG-"), 
             sg.Text(show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
            [command_col]
        ]
        return sg.Window('Adventure Game', layout, size=(520, 350))
    else:
        sg.theme('Dark Blue 3')
        prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(key='-IN-', size=(20, 1), font='Any 14')]
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
        command_col = sg.Column([prompt_input, buttons], element_justification='r')
        layout = [
            [sg.Image(r'assets/forest.png', size=(100, 100), key="-IMG-"), 
            sg.Text(show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
            [command_col]
        ]

    return sg.Window('Adventure Game', layout, size=(520, 350))

if __name__ == "__main__":
    window = make_a_window()

    while True:
        event, values = window.read()
        if event == 'Enter': 
            current_story = parse_command(values['-IN-'])
            window['-OUTPUT-'].update(current_story)
            window['-IMG-'].update(game_places[game_state]['Image'], size=(100, 100))
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
    window.close()

