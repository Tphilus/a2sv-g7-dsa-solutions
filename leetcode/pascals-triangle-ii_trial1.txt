class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            nxt_element = row[i - 1] * (rowIndex - i + 1) // i
            row.append(nxt_element)
        
        return row