#-------------------------------------------------------------------------
# AUTHOR: Kate Yuan
# FILENAME: decision_tree.py
# SPECIFICATION: reads a csv file contact_lens.csv and outputs a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
# X =
one = ['Young', 'Myope', 'Yes', 'Reduced']
two = ['Presbyopic', 'Hypermetrope', 'No', 'Normal']
three =['Prepresbyopic']
rowLen = len(db[0])
for i in range(len(db)):
  X.append([])
  for j in range(rowLen - 1):
    if db[i][j] in one:
        X[i].append(1)
    elif db[i][j] in two:
        X[i].append(2)
    elif db[i][j] in three:
        X[i].append(3)
print(X)

#encode the original categorical training classes into numbers and add to the vector Y.
#--> addd your Python code here
rowLen = len(db[0])
for i in range(len(db)):
  if db[i][rowLen - 1] == 'Yes':
      Y.append(1)
  elif db[i][rowLen - 1] == 'No':
      Y.append(2)
#print(Y)


#fitting the decision tree to the data using entropy as your impurity measure
#--> addd your Python code here
#clf =
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()