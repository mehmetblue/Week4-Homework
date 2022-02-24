"""
3) Requests

General Information:
I want to choose random information with the requests module.

Acceptance Criteria
* Get the name, surname, city and country information of a random person by using the requests module.

(Example=> name:Amber, surname: Murray, city: Salisbury, country: United Kingdom)
* Make lowercase and adjacent by removing the spaces.
(Example=> ambermurraysalisburyunitedkingdom)

* Then randomly shuffle the location of all the characters.
(Example=> mberarrumasyarubsiluniydetmdoingk)
* Apply this process for 100 different people and write in a list.

* Find that has the most characters and print it.

"""

import requests
import random


## empty list for storing the concataned and sampled items
lst = []


## counter storage to stop the execution
count = 0

## to stop function at the number of wanted
while count < 100 :


    ## to get informations from the url
    r = requests.get("https://randomuser.me/api/")


    ## to pick up the requered information and make lowercase 
    # and adjacent by removing the spaces and convert to string
    name = (str(r.json()["results"][0]["name"]["first"]).replace(" ", "")).lower()
    surname = (str(r.json()["results"][0]["name"]["last"]).replace(" ", "")).lower()
    city = (str(r.json()["results"][0]["location"]["city"]).replace(" ", "")).lower()
    country = (str(r.json()["results"][0]["location"]["country"]).replace(" ", "")).lower()


    ## to concatenate the all informations
    sentence = name + surname + city + country


    ## to convert the str to list
    lst_sentence = list(sentence)


    ## randomly shuffle the locations of all the characters
    random.shuffle(lst_sentence)


    ## append the every the sentence to the storage list
    lst.append("".join(lst_sentence))
    

    ## counter to stop the execution
    count += 1


## to see the list (control block)
#print(lst, end="\n\n")


## to see the longest element of the list
result = max(lst, key=len)
print(f"The longest element of the list: {result}")


## to see all the list by their length (check blok)
#for i in lst:
    #print(i, len(i))