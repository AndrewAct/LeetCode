class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        try:
            my_stack = []
            for item in tokens:
                if item not in "+-*/":
                    my_stack.append(int(item))
                else:
                    first, second = my_stack.pop(), my_stack.pop()
                    if item == "+":
                        my_stack.append(second + first)
                    elif item == "-":
                        my_stack.append(second - first)
                    elif item == "*":
                        my_stack.append(second * first)
                    else:
                        my_stack.append(int(float(second)/first))
            return my_stack.pop()
        except ValueError:
            return None