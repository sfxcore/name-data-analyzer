import requests 

def gender_data(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def age_data(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    if response.status_code == 200:
        return response.json()
    else: 
        return None

def country_data(name):
    response = requests.get(f"https://api.nationalize.io?name={name}")
    if response.status_code == 200:
        return response.json()
    else:
        return None
        
name = input("Input your name: ")

gender = gender_data(name)
age = age_data(name)
country = country_data(name)

print(f"\nHello dear, {name.title()} :D")

if gender:
    print("Your assumed gender: ", gender["gender"], f"(accuracy: {gender['probability']})")
if age:
    print("Estimated age: ", age["age"], f"(found {age['count']} people with this name)")    
if country:
    print("Countries where this name is most common:")
    for co in country["country"]:
        if co["probability"] > 0.3:
            print("–", co["country_id"].upper(), f"({co['probability']})")
else: 
    print("Ups... something went wrong")
