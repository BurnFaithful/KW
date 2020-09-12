json = {"name": "Youngmin",
        "age": 26,
        "location": "의정부시",
        "phone_number": "010-3346-9910",
        "friends":
            [
                {"name": "KwonWoo", "age": 21},
                {"name": "JaeWook", "age": 21},
            ]
        }

print(json)
print(json.keys())
print(json.values())
print(json['name'])
# print(json['friends'])
friends = json["friends"]
for friend in friends:
    print(friend)