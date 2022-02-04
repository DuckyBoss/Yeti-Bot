import json

import json

 
# function to add a new user in the Users.json file
def CreateUser(new_data, filename='Users.json'):
    with open(filename,'r+') as file:


        file_data = json.load(file)

        file_data["Users"].append(new_data)

        file.seek(0)

        json.dump(file_data, file, indent = 4)

    # python object to be appended
y = {"Username":"Ducky Boss#5318",
     "UserID": "600010784453558331",
     "AnswersCorrect": 0,
     "AnswerIncorrect": 0,
    }
     
CreateUser(y)