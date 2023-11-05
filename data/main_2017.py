import csv
import numpy as np
from scipy.optimize import linprog

with open('data/combined_2017.csv', 'r') as data:
    data = np.array(list(csv.reader(data)))

keys = data[0]
values = data[1:]

Data_dictionary = {
    item[0]: {
        keys[i]: item[i]
        for i in range(1, len(keys))
    }
    for item in values
}

'''
Input Units: Fixed Asset, Equity, Operating Expenses, Interest Expenses, Impaired Loan

Output Units: Gross Loan, Total Deposits, Investment, Operating Income, Non-interest Income
'''

class Solution:

    def __init__(self, bank_name:str) -> None:
        self.bank_name = bank_name
        self.key_value = keys[1:] #['Fixed Asset' 'Equity' 'Operating Expenses' 'Interest Expenses' 'Impaired Loan' 'Gross Loan' 'Total Deposits' 'Investment' 'Operating Income' 'Non-interest Income']
        self.functionalization()
        self.linear_program()
        pass

    def functionalization(self) -> None:
        self.objective_function = np.array([1, *[0 for i in range(5)]]) #[E, w_Golomt*0, w_Khan*0, w_State*0, w_TDB*0, w_Xac*0] = Min

        self.equation = np.array([[0, *[1 for i in range(5)]]]) #[E*0, w_Golomt, w_Khan, w_State, w_TDB, w_Xac] = 1

        self.equation_value = np.array([1])
        

        self.inequality = np.array([ 
                [-1*int(Data_dictionary[self.bank_name][key]) if np.where(self.key_value == key)[0][0] < 5 else 0, *([ int(Data_dictionary[entry][key]) for entry in Data_dictionary])] for key in self.key_value
                ])

        self.inequality[5:] *= -1
        self.inequality_value = np.array([
            *[0 for i in range(5)],
            *[-1*int(Data_dictionary[self.bank_name][key]) for key in self.key_value[5:]]
            ])
        pass
    
    def linear_program(self):

        self.result = linprog(c=self.objective_function, A_ub=self.inequality, b_ub=self.inequality_value, A_eq=self.equation, b_eq=self.equation_value)
        pass

    def main(self) :
        if self.bank_name in Data_dictionary:
            if self.bank_name in Data_dictionary:
                print("THE RESULT FOR {} BANK: \n {}".format(self.bank_name.upper(), self.result))

Solution('Xac').main()

