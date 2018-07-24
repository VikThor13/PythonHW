class Value:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value * (1 - instance.comission)


class Account:
    amount = Value()

    def __init__(self, comission):
        self.comission = comission



new_acc = Account(0.1)
new_acc.amount = 100

print(new_acc.amount)