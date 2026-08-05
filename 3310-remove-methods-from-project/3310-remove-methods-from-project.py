class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:

        # Step 1: Graph banana
        graph = [[] for _ in range(n)]

        for caller, called in invocations:
            graph[caller].append(called)

        # Step 2: Suspicious methods find karna using DFS
        suspicious = [False] * n

        stack = [k]
        suspicious[k] = True

        while stack:
            current_method = stack.pop()

            for called_method in graph[current_method]:
                if not suspicious[called_method]:
                    suspicious[called_method] = True
                    stack.append(called_method)

        # Step 3: Check whether an outside method
        # calls a suspicious method
        for caller, called in invocations:
            if not suspicious[caller] and suspicious[called]:
                return list(range(n))

        # Step 4: Return only non-suspicious methods
        remaining_methods = []

        for method in range(n):
            if not suspicious[method]:
                remaining_methods.append(method)

        return remaining_methods