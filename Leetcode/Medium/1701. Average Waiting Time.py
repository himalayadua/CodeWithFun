from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res, finish = 0, 0
        for arrival, time in customers:
            if finish > arrival:
                finish += time 
            else: finish = arrival + time
            res += finish - arrival
        return res / len(customers)        