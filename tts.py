import PySimpleGUI as sg
import pyttsx3
layout = [     [sg.Text('Select the type of voice:',text_color='#f2d4a2',background_color='#c39797'),sg.Radio('Male', 'RADIO1',key=('male'),default=True,background_color='#ff52a5'), 
    
    
    sg.Radio('Female', 'RADIO1', key=('female'),background_color='#a89ee0')],
    [sg.Text('Enter text to be spoken:',text_color='brown',background_color='yellow')],
    [sg.Input(key='text'),sg.Button('Speak',button_color='#85ab8b'),sg.Button('Exit',button_color='#711997')],
    # [sg.Text('Volume:'),sg.Text('Speed:',pad=(150,0))],
    # [sg.Slider(range=(0,10),default_value=5,orientation='h',size=(20,15),key='-VOLUME-'),
    #  sg.Slider(range=(0,10),default_value=5,orientation='h',size=(20,15),key='-SPEED-')]
]

window =sg.Window('Text to Speech App',layout,background_color='#f2d4a2')

while True:
    event,values = window.read()
    engine = pyttsx3.init()
    
    if event== sg.WIN_CLOSED:
        break
    elif event == 'Speak':
        text = values['text']
        voices = engine.getProperty('voices') 
        # rate = engine.getProperty('rate')   


        if values['male']:
           engine.setProperty('voice', voices[0].id)
        else:
           engine.setProperty('voice', voices[1].id)
        
        engine.say(text)
        engine.runAndWait()
        # speed = values['-SPEED-']
        # volume = values['-VOLUME-']
window.close()





#voices = engine.getProperty('voices')  
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for    male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#NAME:BERLINDA ACHEAMPONG
#ID:10986852
#DEPARTMENT:BIOMEDICAL ENGINEERING

