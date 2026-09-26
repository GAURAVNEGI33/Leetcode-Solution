
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Store key-value pairs in a dictionary
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):

            # Normal character
            if s[i] != '(':
                result.append(s[i])
                i += 1

            else:
                # Move past '('
                i += 1

                # Find the closing ')'
                start = i

                while s[i] != ')':
                    i += 1

                # Extract the key
                key = s[start:i]

                # Add value if key exists, otherwise '?'
                if key in mp:
                    result.append(mp[key])
                else:
                    result.append('?')

                # Move past ')'
                i += 1

        return ''.join(result)

