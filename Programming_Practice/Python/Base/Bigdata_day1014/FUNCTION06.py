import re
import sys
from urllib.request import urlopen

def urlOpenRead():
    f = urlopen("http://www.naver.com/")
    bytes_content = f.read()
    return bytes_content


def urlProcess(bytes_content):
    scanned_text = bytes_content[:1024].decode("ascii", errors="replace")

    match = re.search(r'charset["\']?([\w-]+)', scanned_text)
    if match:
        encoding = match.group(1)
    else:
        encoding = "utf-8"
    return encoding

def urlPrint(encoding, bytes_content):
    print("encoding :", encoding, file=sys.stderr)
    text = bytes_content.decode(encoding)
    print(text)


if __name__ == "__main__":
    bytes_content = urlOpenRead()
    encoding = urlProcess(bytes_content)
    urlPrint(encoding, bytes_content)

