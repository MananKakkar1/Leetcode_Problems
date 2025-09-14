def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossesDict = {}
        for match in matches:
            if match[1] not in lossesDict:
                lossesDict[match[1]] = 1
            else:
                lossesDict[match[1]] += 1
            if match[0] not in lossesDict:
                lossesDict[match[0]] = 0
        
        answer = [[], []]
        for key, value in lossesDict.items():
            if value == 0:
                answer[0].append(key)
            elif value == 1:
                answer[1].append(key)
                
        winners = sorted(answer[0])
        losers = sorted(answer[1])
        return [winners, losers]


# Time Complexity : O(n log n) where n is the number of matches. We iterate through the matches array once (O(n)) and then sort the winners and losers arrays (O(n log n)).
# Space Complexity : O(n) since we are using a hashmap to store the players and their

# Explanation: We create a hashmap to store the players and their number of losses. 
# We iterate through the matches array and update the hashmap accordingly.
# Finally, we iterate through the hashmap and add the players with 0 losses 
# to the winners array and the players with 1 loss to the losers array.
# We sort both arrays and return them as a list of lists.