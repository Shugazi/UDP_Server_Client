import socket
import json

# database
with open("data.json", "r") as f:
    dataFile = json.load(f)
# creating a socket object
serverSock = socket.socket()

# getiing the Eros IP

host = socket.gethostbyname(socket.gethostname())

# binding the socket to a public host and port
serverSock.bind((host, 12345))

# setting the server to listen for incoming connections
serverSock.listen()

print("Program started, waiting....\n")

def dataHandler(dataJ):
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
            clientSock.send(msg.encode())
        else:
            msg = str(f"No student found with id {id}")
            clientSock.send(msg.encode())
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
            clientSock.send(msg.encode())
        else:
            msg = str(result)
            clientSock.send(msg.encode())
    if option == 4:
        with open("data.json", "r") as f:
            dataDisplayAll = json.load(f)
        msg = str(dataDisplayAll)
        clientSock.send(msg.encode())
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
    # waiting for client to connect
    clientSock, address = serverSock.accept()
    print(f"Connection from {address}")

    # receiving dataq from the client
    while True:
        data = clientSock.recv(1024)
        if not data:
            break  # breakjig out of loop no data
        if data.decode("utf-8") == "exit":
            break

        # send a response back to the client
        dataRead = json.loads(data.decode('utf-8'))
        print(f"Received: {dataRead} \n")
        dataHandler(dataRead)

    # closing the client sock
    clientSock.close()
    exit()
