import socket
from menu import *

# Creating the sock object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Getting the Eros IP
host = '147.26.231.153'

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
        sock.sendto(json_data.encode("utf-8"), (host, 12345))

    elif option == 2:
        json_data = display()
        sock.sendto(json_data.encode("utf-8"), (host, 12345))
        data, address = sock.recvfrom(1024)

        # trying to receive data
        print(data.decode())

    elif option == 3:
        json_data = display_score()
        sock.sendto(json_data.encode("utf-8"), (host, 12345))
        data, address = sock.recvfrom(1024)

        # trying to receive data
        my_data = data.decode().replace("'","\"")
        my_list = json.loads(my_data)
        for entry in my_list:
            print(entry)

    elif option == 4:
        json_data = displayAll()
        sock.sendto(json_data.encode("utf-8"), (host, 12345))
        data, address = sock.recvfrom(1024)

        # trying to receive data
        my_data = data.decode()
        if "'" in my_data:
            my_data = my_data.replace("'","\"")
        my_list = json.loads(my_data)
        for entry in my_list:
            print(entry)

    elif option == 5:
        json_data = deleteID()
        sock.sendto(json_data.encode("utf-8"), (host, 12345))
    elif option == 6:
        sock.sendto("exit".encode("utf-8"), (host, 12345))
        sock.close()
        exit()


while True:
    menuDisplay()

# trying to send data
msg = "Hi test"
sock.sendto(msg.encode(), (host, 12345))

# trying to receive data
data, address = sock.recvfrom(1024)

print(data.decode())

sock.close()
