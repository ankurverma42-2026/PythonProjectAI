#Getting date from web and parsing
#hashlib contains most common hash methods like sha256, md5
import requests
from torch._export.db.examples import dictionary


def x():
    response= requests.get('https://jsonplaceholder.typicode.com/users')
    json_data = response.json()
    for demo in json_data:
        if demo['address']['city'] =="Gwenborough":
            print(f" Person name is {demo['name']} and emailID is {demo["email"]}")


def read():
    diction={}
    try:
        with open("./notes.txt",'r',encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No notes.txt file found")
    for line in content.split("\n"):
        abbreviation = line.split("=")[0]
        full_name = line.split("=")[1]
        diction[abbreviation.strip()] = full_name.strip()
    usr_input = input("Enter the abbreviation: ")
    for x in diction:
        if usr_input in x:
            print(diction[x])

def write():
    usr_input = input("Enter the abbreviation: \n")
    definition= input("Enter the definition: \n")
    with open("./notes.txt",'a',encoding="utf-8") as file:
        file.write("\n" + usr_input + "=" + definition)


def create_hash():
    x="pasword123"
    print(hash(x))

def sample_dict():
    x={"a":1, "b":2, "c":3, "d":4}
    y ={"x":10, "y":20, "z":30}
    print(x | y)

if __name__=='__main__':
    sample_dict()
