'''
You have been hired by a large stout brewery in order to improve the quality testing of their beer. Your superiors want you to devise a way of determining whether a batch of beer is likely to be good enough for sale using a small sample of beers from this batch. Luckily for you, a smart Englishman found a solution to this problem a bit more than a hundred years ago...

Your task in this kata is to implement a function to do Student's one-sample t-test. In the current problem, you will be testing for alcohol content. Your function will receive :

A list of the alcohol content of each beer in a sample of beers : sample
A target alcohol content : pop_mean
A probability threshold : alpha
By calculating a t value for the sample, you will be able to determine whether the current batch is likely to have an average alcohol content close to the target, or not. In statistical terms, if the likelihood that the current sample of beers was taken from the population of beers with a mean of pop_mean (the target alcohol content) is too small (it is too different from the "average" sample), then the whole batch will be rejected.

Specifically, your solution will calculate a t statistic (formula below) and compare it to a "critical" t value, corresponding to the threshold. You are given a table of critical t values (t_table), containing only positive values of t (the t distribution is symmetrical) which you may access like so : t_table[degrees_of_freedom - 1][probability]. Degrees of freedom in a one sample t-test are equal to n - 1, where n is the sample size. If the sample's t value is greater than the "critical" t value (and therefore less probable), then your function will return "Reject". Else, your function will return "Good to drink". All samples will range in size from 2 to 20.

Formula for the t statistic :

Where x̄ is the sample mean, μ0 is the population mean, s is the sample standard deviation and n is the sample size.
Formula for the sample standard deviation (s) :

Where N is the sample size, xi is observation i and x̄ is the sample mean.
Kata inspired by this.
'''

def t_test(sample, pop_mean, alpha):
    n = len(sample)
    sample_mean = sum(sample) / n
    stdv = (sum((i - sample_mean) ** 2 for i in sample) / (n - 1)) ** 0.5
    t_value = (n ** 0.5) * (sample_mean - pop_mean) / stdv
    t_cv = t_table[n - 2][alpha]
    if abs(t_value) > t_cv:
        return 'Reject'
    else:
        return 'Good to drink'
