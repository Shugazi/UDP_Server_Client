import socket
import json

# database
with open("data.json", "r") as f:
    dataFile = json.load(f)

# creating a socket object
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# getiing the Eros IP
host = socket.gethostbyname(socket.gethostname())

# binding the socket to a public host and port
serverSock.bind((host, 12345))

print("Program started, waiting....\n")


def dataHandler(dataJ, address):
    option = dataJ["Option"]
    if option == 1:
        del dataJ['Option']
        dataFile.append(dataJ)
        with open("data.json", "w") as f:
            json.dump(dataFile, f)
    if option == 2:
        with open("data.json", "r") as f:
            dataDisplay = json.load(f)
        id = dataJ['ID']
        result = None
        for obj in dataDisplay:
            if obj.get("id") == id:
                result = obj
                break
        # Print the result
        if result:
            msg = str(result)
            serverSock.sendto(msg.encode(), address)
        else:
            msg = str(f"No student found with id {id}")
            serverSock.sendto(msg.encode(), address)
    if option == 3:
        with open("data.json", "r") as f:
            dataDisplayScore = json.load(f)
        score = dataJ['score']
        result = []
        for entry in dataDisplayScore:
            if entry.get("score") == score:
                result.append(entry)
        if len(result) == 0:
            msg = str(f"No student found with Score value of: {score}")
            serverSock.sendto(msg.encode(), address)
        else:
            msg = str(result)
            serverSock.sendto(msg.encode(), address)
    if option == 4:
        with open("data.json", "r") as f:
            dataDisplayAll = json.load(f)
        msg = str(dataDisplayAll)
        serverSock.sendto(msg.encode(), address)
    if option == 5:
        with open("data.json", "r") as f:
            dataDelete = json.load(f)
        id = dataJ["ID"]
        for obj in dataDelete:
            if obj.get("id") == id:
                dataDelete.remove(obj)
        with open("data.json", "w") as f:
            json.dump(dataDelete, f)


while True:
    # receiving data from the client
    data, address = serverSock.recvfrom(1024)
    if not data:
        break  # break out of loop if no data
    if data.decode("utf-8") == "exit":
        break

    # handle the received data
    dataRead = json.loads(data.decode('utf-8'))
    print(f"Received: {dataRead} \n")
    dataHandler(dataRead, address)

# close the server socket
serverSock.close()
