
# CLASS WITH INHERITANCE (MULTIPLE)


class Father:
    father_name = ''
    father_earning = int(0)

    def __init__(self, father_name, father_earning=0):
        self.father_name = father_name
        self.father_earning = father_earning

    def earn_more(self):
        self.father_earning += 230


class Child(Father):
    child_name = ''
    child_earning = int(0)

    def __init__(self, father_name, father_earning, child_name, child_earning=0):
        super().__init__(father_name, father_earning)
        self.child_name = child_name
        self.child_earning = child_earning

    def get_father_properties(self):
        print(f"Your name : {self.child_name}")
        print(f"Your earning : {self.child_earning}")
        print(f"Total earning(father + your) : {self.father_earning + self.child_earning}")


if __name__ == '__main__':
    input_father_name, input_father_earning, input_your_name, input_your_earning = input(
        "Enter father name, father earning,your name, your earning : ").split(',')

    input_father_name, input_father_earning = input_father_name, int(
        input_father_earning)

    input_your_name, input_your_earning = input_your_name, int(
        input_your_earning)
    child = Child(input_father_name, input_father_earning,
                  input_your_name, input_your_earning)
    child.earn_more()
    child.earn_more()
    child.earn_more()

    # child.father_earning
    child.get_father_properties()
