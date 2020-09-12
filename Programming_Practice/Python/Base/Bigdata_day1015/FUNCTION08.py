def coffee_machine(button):
    print("#1. 뜨거운 물을 준비한다.")
    print("#2. 종이컵을 준비한다.")

    if button == 1:
        print("#3. 보통 커피를 탄다.")
    elif button == 2:
        print("#3. 설탕 커피를 탄다.")
    elif button == 3:
        print("#3. 블랙 커피를 탄다")
    else:
        print("#3. 아무거나 탄다.")

    print("#4. 뜨거운 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")
    print()
    print("손님한테 커피를 드린다.")

button = int(input("어떤 커피(1. 보통 2. 설탕 3. 블랙): "))

print()
coffee_machine(button)
