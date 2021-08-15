"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def zero(func=None): 
    if func is None:
        return 0
    else:
        if func[0] == "+":
            return 0 + func[1]
        elif func[0] == "-":
            return 0 - func[1]
        elif func[0] == "*":
            return 0 * func[1]
        elif func[0] == "/":
            return int(0 / func[1])

def one(func=None): 
	if func is None:
		return 1
	else:
		if func[0] == "+":
			return 1 + func[1]
		elif func[0] == "-":
			return 1 - func[1]
		elif func[0] == "*":
			return 1 * func[1]
		elif func[0] == "/":
			return int(1 / func[1])
        
def two(func=None): 
	if func is None:
		return 2
	else:
		if func[0] == "+":
			return 2 + func[1]
		elif func[0] == "-":
			return 2 - func[1]
		elif func[0] == "*":
			return 2 * func[1]
		elif func[0] == "/":
			return int(2 / func[1])
        
def three(func=None): 
	if func is None:
		return 3
	else:
		if func[0] == "+":
			return 3 + func[1]
		elif func[0] == "-":
			return 3 - func[1]
		elif func[0] == "*":
			return 3 * func[1]
		elif func[0] == "/":
			return int(3 / func[1])
        
def four(func=None): 
	if func is None:
		return 4
	else:
		if func[0] == "+":
			return 4 + func[1]
		elif func[0] == "-":
			return 4 - func[1]
		elif func[0] == "*":
			return 4 * func[1]
		elif func[0] == "/":
			return int(4 / func[1])
        
def five(func=None): 
	if func is None:
		return 5
	else:
		if func[0] == "+":
			return 5 + func[1]
		elif func[0] == "-":
			return 5 - func[1]
		elif func[0] == "*":
			return 5 * func[1]
		elif func[0] == "/":
			return int(5 / func[1])
        
def six(func=None): 
    if func is None:
        return 6
    else:
        if func[0] == "+":
            return 6 + func[1]
        elif func[0] == "-":
            return 6 - func[1]
        elif func[0] == "*":
            return 6 * func[1]
        elif func[0] == "/":
            return int(6 / func[1])
        
def seven(func=None): 
    if func is None:
        return 7
    else:
        if func[0] == "+":
            return 7 + func[1]
        elif func[0] == "-":
            return 7 - func[1]
        elif func[0] == "*":
            return 7 * func[1]
        elif func[0] == "/":
            return int(7 / func[1])
    
def eight(func=None): 
    if func is None:
        return 8
    else:
        if func[0] == "+":
            return 8 + func[1]
        elif func[0] == "-":
            return 8 - func[1]
        elif func[0] == "*":
            return 8 * func[1]
        elif func[0] == "/":
            return int(8 / func[1])
            
def nine(func=None): 
    if func is None:
        return 9
    else:
        if func[0] == "+":
            return 9 + func[1]
        elif func[0] == "-":
            return 9 - func[1]
        elif func[0] == "*":
            return 9 * func[1]
        elif func[0] == "/":
            return int(9 / func[1])

def plus(num): return ["+", num]
def minus(num): return ["-", num]
def times(num): return ["*", num]
def divided_by(num): return ["/", num]