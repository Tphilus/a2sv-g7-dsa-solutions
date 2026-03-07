class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        start = 0
        lastGas = 0

        for i in range(len(gas)):
            lastGas += gas[i] - cost[i]

            if lastGas < 0:
                start = i + 1
                lastGas = 0

        return start