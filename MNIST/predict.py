#encoding=utf-8
import string, random
import numpy as np
import pylab as pl
from sklearn import linear_model, svm, ensemble, cross_validation
#from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import KNeighborsClassifier as KNN
from numpy import *
import hog
x=[]
y=[]
m=[]

def hierarchical_features(images,cell_len=4,overlap=2):
	res=[]
	for image in images:
		x=[]
		for i in arange(0,len(image[0]),cell_len-overlap):
			for j in arange(0,len(image[0]),cell_len-overlap):
				sum=0
				for ii in range(i,i+cell_len):
					for jj in range(j,j+cell_len):
						if ii<len(image) and jj<len(image):
							sum+=image[ii][jj]
				x.append(sum)
		res.append(x)
	return res

num=0
for line in open('mnist_train.csv'):
	if num==0:
		num+=1
		continue
	else:
		lst=map(string.atoi,line.strip('\n').split(','))
		y.append(lst[0])
		x.append(lst[1:])
		image=[]
		for i in range(28):
			i1=1+i*28
			i2=1+(i+1)*28
			l=lst[i1:i2]
			image.append(l)
		m.append(image)
#f=hierarchical_features(m,4,2)
#'''
x_hog=[]
for image in m:
	#print hog.hog(image)
	x_hog.append(hog.hog(image))
for i in range(10):
	print x_hog[i]
x_hog=array(x_hog)
#'''
#clf=ensemble.RandomForestClassifier(n_estimators=100)
#clf=svm.SVC()
clf=svm.SVC(kernel='poly',degree=2,coef0=1)
#clf=linear_model.LogisticRegression(C=0.1,penalty='l1')
#clf=linear_model.SGDClassifier(loss="hinge", penalty="l2")
x=array(x)
y=array(y)
#f=array(f)
'''
z=[]
num=0
for line in open('mnist_test.csv'):
	if num==0:
		num+=1
		continue
	else:
		lst=map(string.atoi,line.strip('\n').split(','))
		z.append(lst)
clf.fit(x,y)
res=clf.predict(z)
for r in res:
	print r
	#print string.atoi(r)
'''
#交叉验证
scores=cross_validation.cross_val_score(clf,x_hog,y,cv=5)
print scores.mean()
