class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2: ].zfill(32)
        new_binary= binary[: : -1]
        return int(new_binary,2)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna