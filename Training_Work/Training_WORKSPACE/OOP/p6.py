

# OVERRIDING

class Bank:

    def get_interest(self):
        return 0


class SBI(Bank):

    def get_interest(self):
        return 8


if __name__ == '__main__':
    sbi = SBI()
    print(f"SBI RATE OF INTEREST : {sbi.get_interest()}%")
