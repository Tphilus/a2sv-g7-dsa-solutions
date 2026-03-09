class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        count, player, trainer = 0, len(players) - 1, len(trainers) - 1
        while trainer >= 0 and player >= 0:
            if players[player] <= trainers[trainer]:
                count += 1
                trainer -= 1
            
            player -= 1
        
        return count