class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for person in range(len(tickets)):
            queue.append(person)
        time = 0
        while queue:
            time += 1
            person = queue.popleft()
            tickets[person] -= 1

            if person == k and tickets[person] == 0:
                return time
            if tickets[person]> 0:
                queue.append(person)
        return time
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna