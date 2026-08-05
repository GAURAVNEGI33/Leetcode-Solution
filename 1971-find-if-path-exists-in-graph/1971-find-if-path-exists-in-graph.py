class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int
    ) -> bool:

        # Adjacency list banana
        graph = [[] for _ in range(n)]

        # Undirected graph: dono directions mein edge add hogi
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # DFS source se start hoga
        stack = [source]
        visited = set([source])

        while stack:
            current_node = stack.pop()

            # Destination mil gaya
            if current_node == destination:
                return True

            # Current node ke neighbours check karo
            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        # Poora graph explore karne ke baad bhi destination nahi mila
        return False