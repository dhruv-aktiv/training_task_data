
# METHOD OVERLOADING


class Operations:

    def add(a, b):
        return f"{a + b}"

    def add(a, b, c):
        return f"{a + b + c}"

    def add(self, a, b, c, d):
        return f"{a + b + c + d}"


ope = Operations()
# print(ope.add(5, 6))
# print(ope.add(5, 6, 1))
# print(ope.add(5, 6, 5, 10))
