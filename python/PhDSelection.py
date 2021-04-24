import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sys.path.append(".")
#read the data
data = pd.read_excel ('IPEDS_data.xlsx' )

###########################   FIRST PART ##########################################
df1  = pd.DataFrame(data)
#Plot some scatter plots to see correlations
plt.scatter(df1['Applicants total'],df1['Admissions total'])
plt.xlabel('Applicants total')
plt.ylabel('Admissions total')
plt.show()
plt.scatter(df1['Applicants total'],df1['Enrolled total'])
plt.xlabel('Applicants total')
plt.ylabel('Enrolled total')
plt.show()

#Split the data in two sets: one part for fit and the other to compare with the model
shuffled = df1['Admissions total']/df1['Applicants total'].sample(frac=1)
data1 , test = np.array_split(shuffled, 2)
#parameter estimation
mu = np.mean(data1)+0.45006*np.std(data1)
beta = np.std(data1)*np.sqrt(6.)/np.pi
# Gumbel distribution
x = np.linspace(0,1,100)
z = 1./beta*np.exp((x-mu)/beta)*np.exp(-np.exp((x-mu)/beta))
#Compare model with data 
plt.plot(x,z,'r')
plt.hist(test, bins=10, density = True)
plt.xlabel('Acceptance rate')
plt.show()

#########################    SECOND PART    ########################### 

#select only some variables
df = pd.DataFrame(data , columns = ['Name','Offers Doctor\'s degree - research/scholarship', 'Estimated graduate enrollment, total', 'Tuition and fees, 2013-14'])

df.columns = df.columns.str.replace(' ', '')
df.columns = df.columns.str.replace(',', '_')
df.columns = df.columns.str.replace('-', '_')
df.columns = df.columns.str.replace("'", '')
df.columns = df.columns.str.replace("/", '_')

print()
print('THIS IS A HELP TOOL TO FIND INSTITUTIONS THAT OFFERS DOCTORAL PROGRAMS IN US')
print('ENTER THE MAX NUMBER OF GRAD ENROLLMENT (AVERAGE IS 1637):')
maxGrad=int(input())
print('ENTER THE MAX ANNUAL TUITION AND FEES (AVERAGE IS 20727):')
maxFee=float(input())
#Filter for only institutions that offers doctoral programs
df = df[df.OffersDoctorsdegree_research_scholarship == 'Yes']

#filter number of graduate studens
df = df[df.Estimatedgraduateenrollment_total < maxGrad]

#filter tuition and fees
df = df[df.Tuitionandfees_2013_14 < maxFee]

pd.set_option('display.max_rows', None)
print('THE POTENTIAL INSTITUTIONS ARE:\n')
print(df.Name)

