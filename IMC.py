import PySimpleGUI as sg

sg.theme('TanBlue')

layout = [
  [sg.Text('IMC')],
  [sg.Text('Massa '),sg.Input(size=(5,1))],
  [sg.Text('Altura'),sg.Input(size=(5,1))],
  [sg.Push(),sg.Button('Calcular'),sg.Push()]
]

window = sg.Window('IMC',layout=layout,font='Monaco 18')

while True:
  event, value = window.read()
  if event == 'QUIT' or event== sg.WIN_CLOSED:
    break
