import PySimpleGUIWx as sg
import requests, json, os
from time import sleep

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

menu_def = ['UNUSED', ['Bitcoin', 'Ethereum', 'Chainlink', 'Cardano', '---', 'Exit']]

profile = os.environ['USERPROFILE']
tray = sg.SystemTray(menu=menu_def, filename=resource_path('coin.ico'))

# tray.ShowMessage('Starting', 'Now Starting the application')

while True:
    event = tray.Read()
    if event == 'Exit':
        break
    elif event == '__ACTIVATED__':
        os.system("start \"\" https://coinbase.com/dashboard")
    elif event == 'Bitcoin':
        tray.ShowMessage(event, 'Price ${:,}'.format(float(json.loads(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').text)['data']['amount'])))
    elif event == 'Ethereum':
        tray.ShowMessage(event, 'Price ${:,}'.format(float(json.loads(requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy').text)['data']['amount'])))
    elif event == 'Chainlink':
        tray.ShowMessage(event, 'Price ${:,}'.format(float(json.loads(requests.get('https://api.coinbase.com/v2/prices/LINK-USD/buy').text)['data']['amount'])))
    elif event == 'Cardano':
        tray.ShowMessage(event, 'Price ${:,}'.format(float(json.loads(requests.get('https://api.coinbase.com/v2/prices/ADA-USD/buy').text)['data']['amount'])))

    # tray.ShowMessage('Event', '{}'.format(event))
