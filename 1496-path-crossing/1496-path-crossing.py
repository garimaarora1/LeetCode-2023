class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates_travelled = set()
        prev = (0,0)
        coordinates_travelled.add(prev)
        for char in path:
            x, y = prev
            if char == "N":
                y += 1
            elif char == "E":
                x += 1
            elif char =="S":
                y -= 1
            elif char == "W":
                x -= 1
            prev = (x,y)
            if prev in coordinates_travelled:
                return True
            coordinates_travelled.add(prev)
        return False
                
                
        