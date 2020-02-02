import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 34469
flag = 255  # Protocol flag


def reconnect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host, port))
        except socket.error or socket.gaierror or socket.herror:
            print("Connection failed, trying again...")
            continue
        print("Reconnected again!")
        break


while True:  # Initial connect
    try:
        s.connect((host, port))
    except socket.error or socket.gaierror or socket.herror:
        print("Connection failed, trying again...")
        continue
    break

while True:
    print("Waiting for data...")
    data = s.recv(4)
    if not data:
        reconnect()
        continue
    array = bytearray(data)
    fun_sel = 0
    if array[0] != flag:
        print("Flag check failed! The message is rejected.")
        continue
    if array[3] != array[1] + array[2]:
        print("Sum flag check failed! The message is rejected.")
        continue
    if array[1] == 1:  # Function 1
        fun_sel = 1
    elif array[1] == 2:  # Function 2
        fun_sel = 2
    elif array[1] == 3:  # Function 3
        fun_sel = 3
    elif array[1] == 4:  # Function 4
        fun_sel = 4
    elif array[1] == 5:  # Function 5
        fun_sel = 5
    else:
        print("Function selecting failed! The message is rejected.")
        continue
    value = 0
    if (fun_sel == 1) or (fun_sel == 2):
        value = array[2]
        print("Servo", fun_sel, "activated with value", value)
    elif fun_sel == 3:
        print("Micro ROV activated.")
    elif fun_sel == 4:
        value = array[2]
        if value == 1:
            print("LED 1 is on.")
        elif value == 0:
            print("LED 1 is off.")
        else:
            print("Value selecting failed! The message is rejected.")
            continue
    elif fun_sel == 5:
        value = array[2]
        if value == 1:
            print("LED 2 is on.")
        elif value == 0:
            print("LED 2 is off.")
        else:
            print("Value selecting failed! The message is rejected.")
            continue
s.close()
