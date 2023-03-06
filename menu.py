import json


def add():
    # missing server logic
    ID = input("\nPlease input ID: ")
    fName = input("Please input First Name: ")
    lName = input("Please input Last Name: ")
    score = input("Please input Score: ")

    data = {"Option": 1, "id": ID, "name": fName, "last_name": lName, "score": score}

    json_data = json.dumps(data)  # creating json object
    print("Successfully Added")
    return json_data


def display():
    ID = input("\nPlease input ID: ")
    # missing server logic
    print(f"\nStudent {ID} Info:")
    data = {"Option": 2, "ID": ID}

    json_data = json.dumps(data)  # creating json object

    return json_data


def display_score():
    score = input("\nPlease input Score: ")
    print(f"\nAll of the students with score: {score}")
    data = {"Option": 3, "score": score}

    json_data = json.dumps(data)  # creating json object

    return json_data


def displayAll():
    print("\nAll Students in the Database: ")
    data = {"Option": 4}

    json_data = json.dumps(data)  # creating json object

    return json_data


def deleteID():
    ID = input("\nPlease input ID: ")

    print(f"{ID} has been deleted.")

    data = {"Option": 5, "ID": str(ID)}

    json_data = json.dumps(data)  # creating json object

    return json_data


def exitOut():
    exit()
