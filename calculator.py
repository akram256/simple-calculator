class Calculator:
    """Class that calculation"""
    
    def __init__(self, Input):
        Input = Input.replace(" ", "")
        #Making a list of all letters of the Input
        inputList = [y for x,y in enumerate(Input)] 
        self.numList = [] 
        self.operatorList = []
        self.tempNum = ''
        #Accepted Characters for input as a number. 
        self.N = ['1','2','3','4','5','6','7','8','9','0', '.'] 

        # Splitting inputList into numList, operatorList for eg, 2+2, numList = ['2', '2'] operatorList = ['+']
        numList, operatorList = self.formNumber(inputList) 
        numList, operatorList = self.solve(numList, operatorList)
        operators = ('+' , '-', '*', '/', '^')
        while operators in operatorList:
            numList, operatorList = self.solve(numList, operatorList)
        self.result = numList[0]

    def solveBrackets(self, Input):
        inputList = [y for x,y in enumerate(Input)]
        numList, operatorList = [], []
        tempNum = ''
        for y,x in enumerate(inputList):
            if str(x) in self.N:
                tempNum += str(x)
            else:
                if tempNum != '':
                    numList.append(float(tempNum))
                tempNum = ''
                operatorList.append(x)
            if y+1 is len(inputList):
                if tempNum != '':
                    numList.append(float(tempNum))
                tempNum = ''
        numList, operatorList = self.solve(numList, operatorList)
        operators = ('+' , '-', '*', '/', '^')
        while operators in operatorList:
            numList, operatorList = self.solve(numList, operatorList)
        return numList[0]

    def formNumber(self, inputList):
        """ Pairs brackets together, so that the program knows which calculations to work out first"""
        tempNum = ''
        numList = []
        operatorList = []
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
                    operatorList.append(x)
                if y+1 is len(inputList):
                    numList.append(float(tempNum))
                    tempNum = ''
        return numList, operatorList 

    def solve(self, numList, operatorList):
        """This function loops through the current indexes of operators and works out the order in which the operators need to be 
                 arranged by comparing the operator_precedence values and seeing if a particular operator needs to be worked on
                 before or after another one """
        for x,y in enumerate(operatorList):
            if y is '^':
                numList[x] = float(numList[x]) ** numList[x+1]
                numList.remove(numList[x+1])
                operatorList.remove(y)
            elif y is '/':
                numList[x] = float(numList[x]) / numList[x+1]
                numList.remove(numList[x+1])
                operatorList.remove(y)
            
            elif y is '*':
                numList[x] = float(numList[x]) * numList[x+1]
                numList.remove(numList[x+1])
                operatorList.remove(y)
                
            elif y is '+':
                numList[x] = float(numList[x]) + numList[x+1]
                numList.remove(numList[x+1])
                operatorList.remove(y)
          
            elif y is '-':
                numList[x] = float(numList[x]) - numList[x+1]
                numList.remove(numList[x+1])
                operatorList.remove(y)
        return numList, operatorList 

while True:
    try:
        cal = Calculator(input("Enter An Equation: "))
        print(cal.result)
    except:
        print("Sorry There's an error")