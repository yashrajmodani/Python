#bank interest calculator

class bank_interest_calculator:
    __interest_rate = 8.6
    __interest_rate_SeniorCitizen = 8.4

    def __init__(self,amount, duration, seniorCitizen):
        self.amount = amount
        self.duration = duration
        self.seniorCitizen = seniorCitizen

    def simple_interest_calculator(self):
        if self.seniorCitizen == True:
            return (self.amount*self.__interest_rate_SeniorCitizen*self.duration)/100
        else:
            return (self.amount*self.__interest_rate*self.duration)/100


greeed = bank_interest_calculator(10000,4,True)
print(greeed.simple_interest_calculator())

greeed = bank_interest_calculator(10000,4,False)
print(greeed.simple_interest_calculator())





