def get_towns():
    with open('towns.txt','r') as file:
        towns = [i.replace('\n','') for i in file.readlines()]
    return towns

