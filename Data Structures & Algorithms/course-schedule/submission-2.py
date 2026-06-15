class Node:
    def __init__(self, course):
        self.course = course
        self.req = []
        self.completed = False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {}

        for [course, req] in prerequisites:
            if course not in course_map:
                course_map[course] = Node(course)
            node = course_map[course]

            if req not in course_map:
                course_map[req] = Node(req)
            req_node = course_map[req]
            node.req.append(req_node)

        def dfs(node, visited):
            if not node.req:
                node.completed = True
                return True

            if node in visited:
                return node.completed

            visited.add(node)

            for req in node.req:
                    if not dfs(req, visited):
                        return False

            visited.remove(node)

            return True

        for course in course_map:
            if not dfs(course_map[course], set()):
                return False

        return True
