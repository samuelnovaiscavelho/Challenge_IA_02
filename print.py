import pyautogui
import time

def print_tela():
    for i in range(1,3+1):
        foto = pyautogui.screenshot()
        time.sleep(4)
        foto.save('foto1%d.png'%(i))
        print('Working%d'%(i))
        
    print('worked')