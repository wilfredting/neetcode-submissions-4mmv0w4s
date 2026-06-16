class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: set() for i in range(numCourses)}

        for [course, req] in prerequisites:
            adj_list[course].add(req)
        
        done = set()

        def dfs(course, visited):
            if course in done:
                return True
            if course in visited:
                return False

            visited.add(course)

            for req in adj_list[course]:
                if not dfs(req, visited):
                    return False

            visited.remove(course)
            done.add(course)

            return True

        for course in adj_list:
            if not dfs(course, set()):
                return False

        return len(done) == numCourses