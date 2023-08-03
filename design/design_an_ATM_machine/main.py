from typing import List


class ATM:

    def __init__(self):
        self.banknotes = [0] * 5
        self.types = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in range(4, -1, -1):
            taken = min(amount // self.types[i], self.banknotes[i])
            amount -= taken * self.types[i]
            ans[i] = taken
        if amount:
            return [-1]
        for i in range(5):
            self.banknotes[i] -= ans[i]
        return ans

# Your ATM object will be instantiated and called as such:

obj = ATM()
banknotesCount = [0,10,0,3,0]
amount = 500
obj.deposit(banknotesCount)
param_2 = obj.withdraw(amount)