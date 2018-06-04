import csv
import pandas as pd
from sklearn import tree
#DecisionTree classifier
from sklearn.tree import DecisionTreeClassifier

with open('voice_train.csv','rb') as f:
	reader = csv.reader(f)
	header = next(reader)
	column = len(header)
	#print column
	#train_set = np.empty(shape=[80,column])
	train_set = []
	for row in reader:
		del row[column-1]
		train_set.append(row)
		#print len(row)
df = pd.read_csv('voice_train.csv')
saved_column = df.label
train_result = []
for gender in saved_column:
	train_result.append(gender)
#print saved_column
#print train_set
print len(train_set)
print len(train_result)

clf = tree.DecisionTreeClassifier()
clf.fit(train_set,train_result)
with open('test.csv','rb') as file:
	pred_reader = csv.reader(file)
	head = next(pred_reader)
	col = len(head)
	print col
	rows = [r for r in pred_reader]
	#for row in pred_reader:
	#	row4=row[4]
	print rows[4]
	print clf.predict([rows[4]])
