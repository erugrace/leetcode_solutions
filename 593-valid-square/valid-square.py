class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a,b):
            return (a[0]- b[0])**2 + (a[1]- b[1])**2
        points = [p1,p2,p3,p4]
        dist = []
        for i in range(4):
            for j in range(i+1, 4):
                dist.append(distance(points[i],points[j]))
        dist.sort()
        if dist[0] != 0 and dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5]:
            return True
        return False



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna