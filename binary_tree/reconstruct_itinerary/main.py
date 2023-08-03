from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for el in tickets:
            if el[0] in graph:
                graph[el[0]].append(el[1])
            else:
                graph[el[0]] = [el[1]]
        for el in graph:
            # переворачиваем, чтобы потом было дешево удалять последний элемент
            graph[el].sort(reverse=True)
        stack = ["JFK"]
        ans = []
        while stack:
            curr = stack[-1]
            if curr in graph and graph[curr]:
                stack.append(graph[curr].pop())
            else:
                ans.append(stack.pop())
        return ans[::-1]

    def findItineraryDFS(self, tickets: List[List[str]]) -> List[str]:
        def dfs(stop):
            while flights[stop]:
                dfs(flights[stop].pop())
            result.append(stop)

        flights = {}
        for fr, to in sorted(tickets, reverse=True):
            if fr in flights:
                flights[fr].append(to)
            else:
                flights[fr] = [to]
        result = []
        dfs("JFK")
        return result[::-1]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(Solution().findItinerary(tickets))