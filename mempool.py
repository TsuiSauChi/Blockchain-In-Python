# Modifiction of Stack to store data
class Mempool:
    def __init__(self):
        self.index = -1
        self.data = list()

    def add(self, value):
        self.index += 1
        self.data.append(value)

    def delete(self, value):
        if self.isEmpty():
            print("Data Block is Empty")
        else:
            self.data.remove(value)

    def isEmpty(self):
        if self.index == -1:
            return True
        else:
            return False

    def sort(self):
        self.data = sorted(self.data)
        return self.data

    def getList(self):
        return self.data