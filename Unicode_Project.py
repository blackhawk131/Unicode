from pynput import keyboard
from pynput.keyboard import Key, Controller
list_input = []
key_controller = Controller()

handle_key = ['a','e','o','u','s','r','x','j','f', 'w', 'd']
double_key = {
    'a': 'â',
    'e': 'ê',
    'o': 'ô',
    'd': 'đ',
    'aw': 'ă',
    'ow': 'ơ',
    'uw': 'ư',
    'uow': 'ươ',
    'ă': 'a',
    'ơ': 'o',
    'ư': 'u',
	'af': 'à',
	'aj': 'ạ'
}

#aou_key = ['a', 'o', 'u']
#aouw_key = ['ă', 'ơ', 'ư']

stop_add_sign = False
is_fast_press = False

def on_press(key):
    global list_input
    global stop_add_sign
    global is_fast_press
    if not is_fast_press:
	
        try:
            print('alphanumeric key {0} presssed'.format(key.char))
            if len(list_input) == 0:
                list_input.append(key.char)
            else:
                if key.char in handle_key and not stop_add_sign:
                    #handle 'â, ê, ơ'
                    if (key.char == 'a' or key.char == 'e' or key.char == 'o' or key.char == 'd'):
                        if double_key[key.char] in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != double_key[key.char]: 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(key)
                                    list_input2.append(key)
                            list_input.clear()
                            list_input = list_input2
                            fast_press(key)
                            list_input.append(key)
                            stop_add_sign = True
                        elif key.char not in list_input:
                            list_input.append(key.char)
                        elif key.char in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != key.char: 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key[key.char])
                                    list_input2.append(double_key[key.char])
                            list_input.clear()
                            list_input = list_input2
                    #handle ă, ơ, ư, ươ
                    elif key.char == "w":
                        if 'ư' in list_input and 'ơ' in list_input and (list_input.index('ơ') - list_input.index('ư') == 1):
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'ư' or elem != 'ơ': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                elif elem == 'ư':
                                    fast_press(double_key['ư'])
                                    list_input2.append(double_key['ư'])
                                elif elem == 'ơ':
                                    fast_press(double_key['ơ'])
                                    list_input2.append(double_key['ơ'])
                            list_input.clear()
                            list_input = list_input2
                            fast_press(key)
                            list_input.append(key)
                            stop_add_sign = True
                        elif 'ă' in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'ă': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key['ă'])
                                    list_input2.append(double_key['ă'])
                            list_input.clear()
                            list_input = list_input2
                            fast_press(key)
                            list_input.append(key)
                            stop_add_sign = True
                        elif 'ơ' in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'ơ': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key['ơ'])
                                    list_input2.append(double_key['ơ'])
                            list_input.clear()
                            list_input = list_input2
                            fast_press(key)
                            list_input.append(key)
                            stop_add_sign = True
                        elif 'ư' in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'ư': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key['ư'])
                                    list_input2.append(double_key['ư'])
                            list_input.clear()
                            list_input = list_input2
                            fast_press(key)
                            list_input.append(key)
                            stop_add_sign = True
                        elif 'u' in list_input and 'o' in list_input and (list_input.index('o') - list_input.index('u') == 1):
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'u' and elem != 'o': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                elif elem == 'u':
                                    fast_press(double_key['u' + key.char])
                                    list_input2.append(double_key['u' + key.char])
                                elif elem == 'o':
                                    fast_press(double_key['o' + key.char])
                                    list_input2.append(double_key['o' + key.char])
                            list_input.clear()
                            list_input = list_input2 
                        elif 'a' in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'a': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key['a' + key.char])
                                    list_input2.append(double_key['a' + key.char])
                            list_input.clear()
                            list_input = list_input2 
                        elif 'o' in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'o': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key['o' + key.char])
                                    list_input2.append(double_key['o' + key.char])
                            list_input.clear()
                            list_input = list_input2 
                        elif 'u' in list_input:
                            list_input2 = []
                            for i in range(len(list_input) + 1):
                                fast_press(Key.backspace)
                            for elem in list_input:
                                if elem != 'u': 
                                    fast_press(elem)
                                    list_input2.append(elem)
                                else:
                                    fast_press(double_key['u' + key.char])
                                    list_input2.append(double_key['u' + key.char])
                            list_input.clear()
                            list_input = list_input2 
                        else:
                            list_input.append(key.char)

                else:
                    list_input.append(key.char)

            print(list_input)
        except AttributeError:
            if key == keyboard.Key.space:
                list_input.clear()
                stop_add_sign = False
            if key == keyboard.Key.backspace:
                if len(list_input) > 0:
                    list_input.remove(list_input[len(list_input) - 1])
                else:
                    stop_add_sign = False
            print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def fast_press(key):
    global key_controller
    global is_fast_press
    is_fast_press = True
    key_controller.press(key)
    key_controller.release(key)
    is_fast_press = False
	
# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()