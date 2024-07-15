import pandas as pd
import numpy as np
from IPython.display import display, Markdown
import pulp

model = pulp.LpProblem("Maximising profits for Tetravaal", pulp.LpMaximize)

variable_names = ['X1', 'X2']

variables = pulp.LpVariable.dicts("grams of ingredient",
                                     (i for i in variable_names),
                                     lowBound=0,
                                     cat='Continuous')

coefficients = [2.5, 2, 3, 2.24]

# Objective function
model += (
    pulp.lpSum([
        coefficients[i] * variables[variable_names[i]]
        for i in range(len(variable_names))])
), "Cost"


# And the constraints, the Matrix A
A=[[1, 0, 0, 0], #Coefficients of the first constraint
   [0, 1, 0, 0], #Coefficients of the second constraint
   [0, 0, 1, 0], #Coefficients of the third constraint
   [1, 1, 0, 1]] #Coefficients of the fourth constraint


# And vector b
b = [2000, 1900, 1000, 1200] #limits of the availability constraints

constraint_names = ['Eggplant', 'Zuccini', 'Pepper', 'Tomatoes']

# Constraints
for i in range(len(A)):           
    model += pulp.lpSum([
        A[i][j] * variables[variable_names[j]] 
        for j in range(len(variable_names))]) <= b[i] , constraint_names[i]

A2 = [[1, 1, 1, 1],
      [1, 1, -1, -1]]
    # Solve our problem
model.solve(solver=pulp.GUROBI(msg = 0))
print(pulp.LpStatus[model.status])