class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        j = 0
        i = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            startI, endI = firstList[i]
            startJ, endJ = secondList[j]

            if startI <= endJ and startJ <= endI:
                result.append([max(startI, startJ), min(endI, endJ)])
            
            if endI <= endJ:
                i += 1
            else:
                j += 1
        
        return result