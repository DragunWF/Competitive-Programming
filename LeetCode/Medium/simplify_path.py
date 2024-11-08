# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [directory for directory in path.split("/") if directory]
        traversed = []
        for directory in directories:
            if directory == ".":
                continue
            if directory == "..":
                if traversed:
                    traversed.pop()
            else:
                traversed.append(directory)
        return f"/{'/'.join(traversed)}"
