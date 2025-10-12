class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for curr, prev in prerequisites:
            adjList[curr].append(prev)

        taken = set()

        def dfs(curr):
            if curr in taken:
                return False
            if adjList[curr] == []:
                return True
            
            taken.add(curr)
            for prev in adjList[curr]:
                if not dfs(prev):
                    return False
            taken.remove(curr)
            adjList[curr] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


