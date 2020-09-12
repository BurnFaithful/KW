def inputFilter(min, max, errorFunc):
    isError = True
    while True:
        command = input("커맨드 입력 >> ")

        try:
            command = int(command)
            if command >= min and command <= max:
                isError = False
                break
            else:
                print(f"{min}부터 {max} 사이로 입력.")
        except ValueError:
            print("잘못된 입력")

        if isError is True:
            errorFunc()

    return command
