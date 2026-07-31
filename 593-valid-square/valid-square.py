class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def distance(a,b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2 
        dists = []
        points = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i+1, 4):
                dists.append(distance(points[i],points[j]))
        dists.sort()
        if dists[0] > 0 and dists[0]==dists[1] == dists[2] == dists[3] and dists[4] == dists[5]:
            return True
        return False

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna