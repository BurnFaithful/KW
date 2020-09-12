# 하노이탑 알고리즘


def move(disk, src, dst, tmp):
    if disk == 1:
        print(f"Move Disk : {disk} from {src} to {dst}")
    else:
        move(disk - 1, src, tmp, dst)
        print(f"Move Disk : {disk} from {src} to {dst}")
        move(disk - 1, tmp, dst, src)


if __name__ == "__main__":
    move(3, 'A', 'B', 'C')