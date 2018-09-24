import numpy as np 
from scipy.stats import norm

def calc_logl(x,mu,sd):
  """
  Helper function to calculate log-likelihood
  """
  logl = 0
  for i in x:
    logl += np.log(norm.pdf(i, mu, sd))
  return logl

def find_optimal_k(data):
  """
  Provide a numpy array, returns index to serve as cut-off
  """
  profile_logl = []
  for q in range(1,len(data)):
    n = len(data)
    s1 = data[0:q]
    s2 = data[q:]
    mu1 = s1.mean()
    mu2 = s2.mean()
    sd1 = s1.std()
    sd2 = s2.std()
    sd_pooled = np.sqrt((((q-1)*(sd1**2)+(n-q-1)*(sd2**2)) / (n-2)))
    profile_logl.append(calc_logl(s1,mu1,sd_pooled) + calc_logl(s2,mu2,sd_pooled))
  return np.argmax(profile_logl)