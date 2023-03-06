import socket
from menu import *

# Creating the sock object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Getting the Zeus IP
host = '147.26.231.153'

# connecting to a server on a specifed port
sock.connect((host, 12345))


def menuDisplay():
    print("\n1.) add ")
    print("2.) display student info")
    print("3.) display score")
    print("4.) display All")
    print("5.) delete id")
    print("6.) exit")
    option = int(input("Please enter an option:"))

    if option == 1:
        json_data = add()
        sock.send(json_data.encode("utf-8"))

    elif option == 2:
        json_data = display()
        sock.send(json_data.encode("utf-8"))
        data = sock.recv(1024)

        # trying to receive data
        print(data.decode())

    elif option == 3:
        json_data = display_score()
        sock.send(json_data.encode("utf-8"))
        data = sock.recv(1024)

        # trying to receive data
        my_data = data.decode().replace("'","\"")
        my_list = json.loads(my_data)
        for entry in my_list:
            print(entry)

    elif option == 4:
        json_data = displayAll()
        sock.send(json_data.encode("utf-8"))
        data = sock.recv(1024)

        # trying to receive data
        my_data = data.decode().replace("'","\"")
        my_list = json.loads(my_data)
        for entry in my_list:
            print(entry)

    elif option == 5:
        json_data = deleteID()
        sock.send(json_data.encode("utf-8"))
    elif option == 6:
        sock.send("exit".encode("utf-8"))
        sock.close()
        exit()


while True:
    menuDisplay()

# trying to send data
msg = "Hi test"
sock.send(msg.encode())

# trying to receive data
data = sock.recv(1024)

print(data.decode())

sock.close()
