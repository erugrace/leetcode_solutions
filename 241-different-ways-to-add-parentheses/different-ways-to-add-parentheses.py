class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = {"+", "-", "*"}
        def dfs(expr):
            results = []
            #base case
            if not any(c in op for c in expr):
                return [int(expr)]
            #recursive case
            for i,char in enumerate(expr):
                if char in op:
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == "+":
                                results.append(l+r)
                            elif char == "-":
                                results.append(l-r)
                            else:
                                results.append(l*r)
            return results
        return dfs(expression)










#         2-1-1
#           left  right
#       1st  (2)-(1-1)= 2
#       2nd (2-1)-(1)= 0
        
#         [0,2]

# #base case: when there is no operator
# if no operator:
#     return [int(expr)]
# # recursive part: when there is an operator
# for i, char in enumerate(expr):
#    (2*(3-(4*5))) = -34           (2*3-4)* 5           
#    1st                                      
#    left =2                                  
#                left    right                
#    right= 3-4*5 1st 3 -(4*5)  = -17         
#                 2nd (3-4)*5   = -5
#                 [-17,-5]

#     left = 2 = [2]
#     right = [-17, -5]
#      for l in left:
#         for r in right:
#             if +:
#                 l + r
#             elif -:
#                 l - r
#             else:
#                 l * r

# results = [-34, -10]

# (2*3)-(4*5)
#  1st
#  left = 2*3 
#         1st (2) * (3)
#         left = [2]
#         right = [3]
#         [6]
#  right = 4*5
#         left = [4]
#         right = [5]
#         [20]



#  left = [6]
#  right = [20]
#  [-14]
#  results = [-34, -10, -14]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna