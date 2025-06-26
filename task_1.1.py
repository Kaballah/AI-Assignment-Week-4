plpCommunity = [
    {"name": "Ronnie", "age": 25, "city": "Nairobi", "isStudent": True},
    {"name": "JsDaddie", "age": 29, "city": "Nakuru", "isStudent": False},
    {"name": "Ransford", "age": 22, "city": "Kericho", "isStudent": True},
    {"name": "Sophia", "age": 24, "city": "Mombasa", "isStudent": True},
    {"name": "Myra", "age": 21, "city": "Limuru", "isStudent": True},
    {"name": "Jane", "age": 20, "city": "Naivasha", "isStudent": True},
    {"name": "Chaikin", "age": 27, "city": "Kisumuu", "isStudent": False}]
    
# print(plpCommunity[1]["name"])
sorted_output = sorted(plpCommunity, key=lambda d: d['name'])
print(sorted_output)