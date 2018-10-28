#python 3.5.2

import numpy as np
from PIL import Image,ImageStat
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
        while(flag == 0 and iteration<=10):
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
                print ("Error is",error," after ",iteration,"iteration")

                if(error<=e):
                    flag=1
        print ("Centroids at Convergence")
        print (new_centroid)
        return new_centroid,new_clusters	        
	
def drawWindow(result,cluster,img_width,img_height):
        img = Image.new('RGB', (img_width, img_height), "white")
        p = img.load()
        i=0
        for x in range(img_width):
             for y in range(img_height):
                   RGB_value = result[cluster[i]]
                   RGB_value = [int(RGB_value[0]),int(RGB_value[1]),int(RGB_value[2])]
                   p[x,y] = tuple(RGB_value)
                   i+=1
        img.save('output.jpg')

img_input = input("Enter image name(without any extension):")
img = img_input + ".jpg"
im = Image.open(img)
img_width, img_height = im.size
px = im.load()

arr = []
for i in range(img_width):
	for j in range(img_height):
		pixel = px[i,j]
		arr.append(pixel)

k = int(input("No.of CLusters - "))
e = float(input("Threshold error - "))

centroid = []

for i in range(k):
	centroid.append(arr[i])

result,cluster = kmeans(arr,centroid,e)
drawWindow(result,cluster,img_width,img_height)

	

