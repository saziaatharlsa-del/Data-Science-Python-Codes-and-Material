#work with data to understand patterns, solve problems, and make decisions. Descriptive Statistics and Probability help us understand data and draw meaningful conclusions.

#Concept	                    Why do we use it in Data Science?

#Mean, Median, Mode	            To understand the typical or central value in a dataset.
#Variance & Standard Deviation	To understand how much the data varies or spreads out.
#Range & Percentiles	        To understand the minimum–maximum spread and the relative position of values.
#Probability	                To estimate the likelihood of events, such as customer churn or product demand.
#Normal Distribution	        To understand bell-shaped data patterns and support statistical analysis.
#Uniform Distribution	        To model situations where values have equal probability density across a range.
#Binomial Distribution	        To calculate probabilities involving a fixed number of success/failure trials.
#Central Limit Theorem (CLT)	To understand why sample means tend toward a normal distribution, supporting statistical inference.
#Confidence Intervals	        To estimate a population value using a range rather than a single number.
#Hypothesis Testing (t-tests)	To evaluate whether an observed difference between groups provides statistically significant 
#                                evidence of a real difference.


#Descriptive statistics

import numpy as np
from statistics import multimode
marks = np.array([60, 70, 70, 80, 90])
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Mode:", multimode(marks.tolist()))
print("Variance:", np.var(marks))
print("Standard deviation:", np.std(marks))
print("Range:", np.max(marks) - np.min(marks))
print("25th percentile:", np.percentile(marks, 25))
print("75th percentile:", np.percentile(marks, 75))


##Concept	        #Simple meaning

#Mean	            Average marks
#Median	            Middle value after sorting
#Mode	            Most frequently occurring value
#Variance	        How spread out values are, measured in squared units
#Standard deviation	How far values typically spread around the mean
#Range	            Maximum minus minimum
#Percentile	        Position of a value within a dataset


#Basic probability

#probability using a die.

#P(A)= Favourable outcomes / Total equally likely outcomes

#For a fair six-sided die:

#- Probability of getting 4 = 1/6
#- Probability of getting an even number = 3/6=0.5
#- Probability of getting a number greater than 4 = 2/6

#Rules

#- Probability ranges from 0 to 1.
#- Complement: P(not A) = 1-P(A)
#- For mutually exclusive events: P(A or B)= P(A) + P(B)
#- For independent events: P(A and B) = P(A) X P(B)


#Normal, uniform and binomial distributions

#Normal distribution

#Data cluster around the average, forming a bell-shaped curve. 
# Example: approximately normally distributed measurement data.

#- loc = mean
#- scale = standard deviation

#Uniform distribution

#Values within a specified interval have equal probability density. 
# Example: generating random numbers between 0 and 1.

#- low = lower bound
#- high = upper bound


#Binomial distribution

#Counts the number of successes in a fixed number of independent trials, 
#each with the same success probability. 
#Example: number of heads in 10 coin tosses.

#- n = number of trials
#- p = probability of success

import numpy as np

import matplotlib.pyplot as plt

np.random.seed(42)
normal = np.random.normal(loc=50, scale=10, size=1000)
uniform = np.random.uniform(low=0, high=100, size=1000)
binomial = np.random.binomial(n=10, p=0.5, size=1000)

plt.hist(normal, bins=20)
plt.title("Normal Distribution")
plt.show()

plt.hist(uniform, bins=20)
plt.title("Uniform Distribution")
plt.show()

plt.hist(binomial, bins=range(12), align="left")
plt.title("Binomial Distribution: Number of Successes")
plt.xticks(range(11))
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# Original population
population = np.random.exponential(
    scale=50,
    size=10000
)

sample_means = []

# Take 1000 samples
for i in range(1000):

    sample = np.random.choice(
        population,
        size=30
    )

    sample_means.append(np.mean(sample))

# Plot sample means
plt.hist(sample_means, bins=30)
plt.title("Central Limit Theorem")
plt.xlabel("Sample Means")
plt.ylabel("Frequency")
plt.show()



import numpy as np
import pandas as pd

marks = [45, 50, 60, 70, 80, 85, 90, 95, 55, 65]

# NumPy
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("25th Percentile:", np.percentile(marks, 25))

# Pandas
df = pd.DataFrame({"Marks": marks})

print("Mode:", df["Marks"].mode().tolist())
print(df.describe())






import numpy as np
from scipy import stats

marks = [65, 70, 75, 68, 72, 80, 69, 74, 71, 76]

mean = np.mean(marks)

confidence_interval = stats.t.interval(
    confidence=0.95,
    df=len(marks)-1,
    loc=mean,
    scale=stats.sem(marks)
)

print("Mean:", mean)
print("95% Confidence Interval:", confidence_interval)



from scipy import stats

marks = [65, 70, 75, 68, 72, 80, 69, 74, 71, 76]

result = stats.ttest_1samp(
    marks,
    popmean=70
)

print("T-statistic:", result.statistic)
print("P-value:", result.pvalue)

if result.pvalue < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")




from scipy import stats

batch_A = [60, 65, 70, 68, 72]
batch_B = [80, 85, 75, 90, 85]

result = stats.ttest_ind(
    batch_A,
    batch_B,
    equal_var=False
)

print("T-statistic:", result.statistic)
print("P-value:", result.pvalue)

if result.pvalue < 0.05:
    print("Significant Difference")
else:
    print("No Significant Difference")



#Feature	 Normal	        Uniform	                    Binomial
#----------------------------------------------------------------------
#Shape	     Bell-shaped	Flat	                    Discrete bars
#Values	     Continuous	    Continuous or discrete	    Discrete counts
#Pattern	 Most values    near average	            Equal probability across possible values	Counts successes
#Example	 Exam marks	    Random number from 0–100	Heads in 5 tosses




#Topic	              What does it do?	    Example
#---------------------------------------------------------------------------
#Confidence Interval  Estimates a range	    Average marks may be between 64 and 76
#Hypothesis Testing	  Tests an assumption	Is the average marks really 70?
#t-test	              Compares averages	    Are Batch A and Batch B averages different?