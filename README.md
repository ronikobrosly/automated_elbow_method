# automated_elbow_method

For some types of unsupervised learning analyses, machine learning practitioners have typically needed to examine a plot and make a somewhat subjective judgement call to tune the model (the so-called "elbow method"). I can think of two examples of this but others certainly exist:
1) In any sort of clustering analysis: finding the appropriate number of clusters by plotting the within-cluster sum of squares against the number of clusters.
2) When reducing feature space via PCA or a Factor Analysis: using a Scree plot to determine the number of components/factors to extract.

For one-off analyses, using your eyeballs and some subjectivity might be fine, but what if you are using these methods as part of a pipeline in an automated process? I came across a very simple and elegant solution to this, which is described by Mu Zhu in this paper. Lots of heuristics exist to solve this but I've found this method to be particularly robust.
Zhu's idea is to generate the data you would typically generate to identify the elbow/kink. Then, he treats this data as a composite of two different samples, separated by the cutoff he is trying to identify. He loops through all possible cutoffs, in an attempt to find the cutoff that maximizes the profile log-likelihood (using sample means and a pooled SD in the calculations).
