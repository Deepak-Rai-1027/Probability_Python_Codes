# Probability of an event A given another event B has already occured. 
# In this case the new universe is event B (the new sample space omega)
# Main objective is to calculate the portion of A in event B.


# Example 
# Calculate the probability a student gets an A (80% +) in math, given they miss 10 or more classes.
import pandas as pd
import numpy as np

df = pd.read_csv('student-alcohol-consumption/student-mat.csv')
print(df.head(3))

print(len(df))

# We are only concerned with the columns, 'absences' (number of absences) and 'G3' (final grade from 0 to 20)

# Let's create a couple of dummy variables.

# Adding a column 'grade_A' for students with 80% or higher final score.
df['grade_A'] = np.where(df['G3']*5 >= 80, 1, 0)

# Adding a column 'high_absenses' for students which missed 10 or more classes. 
df['high_absenses'] = np.where(df['absences'] >= 10, 1, 0)

# Adding one more column for making a pivot table.
df['count'] = 1

# Drop all columns which won't be use in this example.
df = df[['grade_A', 'high_absenses', 'count']]
print(df.head())

# Create a pivot table
pv_table = pd.pivot_table(df, values='count', index=['grade_A'], columns=['high_absenses'], aggfunc=np.size, fill_value=0)
print(pv_table)

# Let's calculate some probabilities:
# P(A) : probability of a grade of 80% or higher
prob_A = (35+5) / len(df) 
print('Probability - P(A):', prob_A)

# P(B) - probability of missing 10 or more math classes
prob_B = (78+5) / len(df)
print('Probability - P(B):', prob_B)

# Join Probability P(A,B) or P(A and B)
prob_A_and_B = 5 / len(df) 
print('Probability - P(A,B):', prob_A_and_B)

# Conditional Probability: Probability P(A|B) - Students getting higher grade (80% +) given they missed 10 or more classes. 
cond_prob = prob_A_and_B / prob_B
print('Probability - P(A|B):', cond_prob)