class Calculator:
	def __init__(self, Input): 
		inputList = [y for x,y in enumerate(Input)] 
		self.numList = [] 
		self.operator = [] 
		self.tempNum = ''
		self.N = ['1','2','3','4','5','6','7','8','9','0', '.'] 
		numList, operator = self.formNumber(inputList)
		numList, operatort = self.solve(numList, operator)
		while ('+' in operator) or ('-' in operator) or ('*' in operator) or ('/' in operator):
			numList, operator = self.solve(numList, operator)
		self.result = numList[0]

	def solveBrackets(self, Input):
		inputList = [y for x,y in enumerate(Input)]
		numList, operator = [], []
		tempNum = ''
		for y,x in enumerate(inputList):
			if str(x) in self.N:
				tempNum += str(x)
			else:
				if tempNum != '':
					numList.append(float(tempNum))
				tempNum = ''
				operator.append(x)
			if y+1 is len(inputList):
				if tempNum != '':
					numList.append(float(tempNum))
				tempNum = ''
		numList, operator = self.solve(numList, operator)
		while ('+' in operator) or ('-' in operator) or ('*' in operator) or ('/' in operator):
			numList, operator = self.solve(numList, operator)
		return numList[0]

	def formNumber(self, inputList):
		tempNum = ''
		numList = []
		operator = []
		brackets = False
		for y,x in enumerate(inputList):
			if str(x) is '(':
				brackets = True 
				continue 
			elif str(x) is ')':
				brackets = False 
				tempNum = self.solveBrackets(tempNum)
				numList.append(tempNum)
				continue
			if brackets:
				tempNum += str(x)
			else:
				if str(x) in self.N:
					tempNum = tempNum + str(x) 
				else:
					if tempNum != '':
						numList.append(float(tempNum))
					tempNum = ''
					operator.append(x)
				if y+1 is len(inputList):
					numList.append(float(tempNum))
					tempNum = ''
		return numList, operator 

	def solve(self, numList, operator):
		for x,y in enumerate(operator):
			if y is '/':
				numList[x] = float(numList[x]) / numList[x+1]
				numList.remove(numList[x+1])
				operator.remove(y)
		for x,y in enumerate(operator):
			if y is '*':
				numList[x] = float(numList[x]) * numList[x+1]
				numList.remove(numList[x+1])
				operator.remove(y)
		for x,y in enumerate(operator):
			if y is '+':
				numList[x] = float(numList[x]) + numList[x+1]
				numList.remove(numList[x+1])
				operator.remove(y)
		for x,y in enumerate(operator):
			if y is '-':
				numList[x] = float(numList[x]) - numList[x+1]
				numList.remove(numList[x+1])
				operator.remove(y)
		return numList, operator

while True:
	try:
		cal = Calculator(input("Equation: ")) 
		print(cal.result)
	except:
		print("error")