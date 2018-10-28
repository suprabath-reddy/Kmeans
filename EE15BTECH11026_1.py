#python 3.5.2

import numpy as np
import math

def euclidean_distance(a,b):
	dis = 0
	for i in range(0,len(a)):
		dis+=(a[i]-b[i])**2
	return math.sqrt(dis)

def distance(arr,centroid):
	dis_centroid = []
	for i in range(len(arr)):
		a = []
		for j in range(len(centroid)):
			a.append(euclidean_distance(centroid[j],arr[i]))
		dis_centroid.append(a)
	return dis_centroid

def clustering(arr,centroid):
	dis_centroid = distance(arr,centroid)
	cluster = []
	
	for i in range(len(arr)):
		cluster.append(np.argmin(dis_centroid[i]))

	return cluster

def kmeans(arr,centroid,e):
        new_centroid = centroid
        flag = 0
        iteration = 0
        while(flag == 0):
                iteration+=1
                error = 0
                new_clusters = clustering(arr,new_centroid)
                centroid = new_centroid
                new_centroid = []

                for i in range(len(centroid)):
                        a = []
                        for j in range(len(arr)):
                              if(new_clusters[j] == i):
                                   a.append(arr[j])
                        mean = np.mean(a, axis=0)
                        new_centroid.append(mean)

                for i in range(len(centroid)):
                         error+=euclidean_distance(centroid[i],new_centroid[i])
                print (error," after ",iteration,"iteration")

                if(error<=e):
                    flag=1
        print ("Centroids at Convergence")
        print (new_centroid)
        display(arr,new_clusters,len(centroid)) 	        

def display(arr,new_clusters,k):
	for i in range(k):
		print ("Cluster - ",i)
		for j in range(len(arr)):
			if(new_clusters[j]==i):
				print (arr[j])
	
d = int(input("Dimension of X - "))
N = int(input("No. of samples - "))

arr= []

print ("Enter one dimension of all samples and after that other dimension") # d*N matrix

for i in range(0,d):
	a = []
	for i in range(0,N):
		b = float(input(""))
		a.append(b)
	arr.append(a)

arr = np.transpose(arr) #Transposing X

k = int(input("No.of CLusters - "))
e = float(input("Threshold error - "))

centroid = []

for i in range(k):
	centroid.append(arr[i])

print (centroid)
kmeans(arr,centroid,e)


	
