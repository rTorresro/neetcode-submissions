class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        # [2, 4, -4, -1]   
        # output = [2]

        # push 2
        # push 4
        # now we reach a negative
        # we wanna check what we recently pushed to what we currently face
        # 4 and -4
        # both explode since 4 = 4, no matter the sign
        # so now we just have 2
        # there comes -1
        # so then 1 < 2, so 2 stays
        # return 2

        stack = []

        for ast in asteroids:
            if ast < 0:
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                
                else:
                

                    while (stack and stack[-1] > 0 and abs(ast) > abs(stack[-1])):
                        stack.pop()
                    if stack and stack[-1] > 0 and stack[-1] == abs(ast):
                        stack.pop()
                    elif not stack or stack[-1] < 0:
                        stack.append(ast)
            else:
                stack.append(ast)
            
        return stack 
            







