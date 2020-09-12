import string

str = string.ascii_lowercase

for index, i in enumerate(str[:3]):
    print(f"[{index}] -> [{i}]")