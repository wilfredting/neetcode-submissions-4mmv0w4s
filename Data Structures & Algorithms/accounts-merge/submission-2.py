class UnionFind:
    def __init__(self):
        self.user = {}
        self.parent = {}
        self.rank = {}

    def __find__(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def add(self, n, user):
        if n not in self.parent:
            self.user[n] = user
            self.parent[n] = n
            self.rank[n] = 1

    def union(self, n1, n2):
        p1, p2 = self.__find__(n1), self.__find__(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True

    def output(self):
        
        output = {}
        for email in self.parent:
            p = self.__find__(email)
            if p not in output:
                output[p] = [email]
            else:
                output[p].append(email)
        final = []
        for parent, emails in output.items():
            final.append([self.user[parent]] + sorted(list(set(emails))))
        return final

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind()
        for account in accounts:
            user = account[0]
            # for i, email in enumerate(account[1:]):
            #     union.add(email, user)
            #     if i > 0:
            #         union.union(account[1], account[i])
            first_email = account[1]
            for i in range(1, len(account)):
                union.add(account[i], user)
                union.union(first_email, account[i])

        return union.output()
        