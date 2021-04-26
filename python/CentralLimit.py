
############## This program illustrates the Central limit theorem ###########
import numpy as np
import matplotlib.pyplot as plt

# define a function that samples numbers from a triangular distribution
# and takes the mean N times
def CentralLimit(N):
    arr = []
    for i in range (0, N):
        a = np.random.triangular(-3,1,15,size=100)
        arr.append(sum(a)/len(a))
    return arr

########## read from user the number of samples N (a large number would be better)
print('Enter the number of points to sample (consider a large number for better plots):')
n = int(input())
plt.rc('font', size=5)    

#plot histograms of the triangle distribution and the means taking 5%, 50%
# and 100% of data


fig, axs = plt.subplots(2, 2)
arr0 = np.random.triangular(-3,1,15,size=1000000)
axs[0,0].hist(arr0, bins=500, range = (-4.,16.), density=True)
axs[0,0].set_title('Triangular distribution')
axs[0,1].hist(CentralLimit(int(0.05*n)),bins=int(1.+10.*np.log(0.05*n)),density=True)
axs[0,1].set_title('Distribution of the means with N =' + str(int(0.1*n)) + ' samples')
axs[1,0].hist(CentralLimit(int(0.5*n)),bins=int(1.+10.*np.log(0.5*n)),density=True)
axs[1,0].set_title('Distribution of the means with N =' + str(int(0.5*n)) + ' samples')
axs[1,1].hist(CentralLimit(n),bins=int(1.+10.*np.log(n)),density=True)
axs[1,1].set_title('Distribution of the means with N =' + str(int(n)) + ' samples')
plt.show()
