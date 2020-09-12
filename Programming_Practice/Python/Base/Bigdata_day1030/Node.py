class SLNode:
    def __init__(self, value, link):
        self.value = value
        self.link = link

class DLNode:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next