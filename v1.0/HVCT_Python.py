#Keyboard map https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
#Mouse input https://pynput.readthedocs.io/en/latest/mouse.html
#HVCT_Python v1.0 - HoneyFoxQueen
from pynput import keyboard, mouse #pip install pynput
import serial #pip install pyserial

def easy_param(_func, _params={}):
    _func(**_params)

com_port = ""   #nome porta seriale
baudrate = 9600
ser = serial.Serial(com_port, baudrate, timeout=0.1)

mouse_handler = mouse.Controller()
keyboard_handler = keyboard.Controller()

IR_CODES_KEY_MAPPING = {
    0x2C: keyboard.Key.space,   #premere spazio
    0x30: keyboard.Key.enter,   #premere enter
    0x2B: keyboard.Key.left,    #premere freccia sinistra
    0x28: keyboard.Key.right,   #premere freccia destra
    0x31: 'f'   #premere tasto f
}  
IR_CODES_MOUSE_MAPPING = {
    0x5C: {'val':{'button':mouse.Button.left}, 'exec_act': [mouse_handler.press, mouse_handler.release]},   #premere tasto sinistro
    0x58: {'val':{'dx':0,'dy':-5}, 'exec_act': [mouse_handler.move]},   #spostare mouse su
    0x59: {'val':{'dx':0,'dy':5}, 'exec_act': [mouse_handler.move]},    #spostare mouse giu
    0x5A: {'val':{'dx':-5,'dy':0}, 'exec_act': [mouse_handler.move]},   #spostare mouse sinistra
    0x5B: {'val':{'dx':5,'dy':0}, 'exec_act': [mouse_handler.move]}     #spostare mouse destra
}


while True:
    data = ser.readline().decode().strip()
    if data:
        dec_data = int(data, 16)
        print("Code:", hex(data), "\tMAPPING:", end=" ")
        if dec_data in IR_CODES_KEY_MAPPING:
            keyboard_handler.press(IR_CODES_KEY_MAPPING[dec_data])
            keyboard_handler.release(IR_CODES_KEY_MAPPING[dec_data])
            print("KEYBOARD")
        elif dec_data in IR_CODES_MOUSE_MAPPING:
            for exec_act in IR_CODES_MOUSE_MAPPING[dec_data]['exec_act']:
                easy_param(exec_act, IR_CODES_MOUSE_MAPPING[dec_data]['val'])
            print("MOUSE")
        else:
            print("---")
