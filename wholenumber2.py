# coding=utf-8

class WholeNumber:
    '''This class determine the nearest whole number, base on the Decimal Number given to it
    How to use the script is by instantiate the object with the required argument,
    It will return appropriate wholenumber
    '''

    DECIMAL_POINT = 2                   #We are using two-decimal place

    def __init__(self,fracNumber):          #This allow the class to be call with the argument like WholeNumber(8.987)
        self.getNUmber(fracNumber)

    def getNUmber(self, fracNumber):
        fracNumber = str(fracNumber)
        self.__isvalidFraction(fracNumber)


    def __isvalidFraction(self,fracNumber):
        try:
            self.intp, self.floatp = fracNumber.split('.')
            self.digitstripper(self.floatp)
        except ValueError:
            print('Enter Decimal Number')


    def digitstripper(self, floatp):
        if len(floatp) > WholeNumber.DECIMAL_POINT:
            floatp = floatp[:WholeNumber.DECIMAL_POINT]
        self.isWholeNum(floatp)

    def isWholeNum(self,floatp):
        iswhole = self.__checkLdigit__(floatp)
        if iswhole == True:
            if self.intp[0] != '-':                 #This section check if the given Number is Negative Fraction
                intp = int(self.intp)+1             # If YES, appropriate Value is return
                print (str(intp)+'.'+'00')
            else:
                intp = int(self.intp)-1
                print(str(intp)+'.'+'00')
        else:
            print(self.intp+'.'+'00')

    def __checkLdigit__(self,floatp):
        '''This Method grab the number immediate after decimal point and the the number after it and
        It does the following
        1. Check if the last number is less or greater than 5
        If YES, it increase the number to the left of it by 1 otherwise it does nothing
        2. if the  Number immediately after decimal point is less than 5, it return FALSE otherwise it return TRUE
        to the calling code
        '''
        a = int(floatp[0])
        b = int(floatp[1])
        if b not in range(1,4,1):
            a = a+1
            if a not in range(1,4,1):
                return True
            else:
                return False


WholeNumber(-75566.9957564)