**Investor segementation based on risk and reward patter is done using k-mean clustering**

**K-mean clustering:**
K-Means Clustering is a type of unsupervised machine learning algorithm that groups similar data points into clusters based on their features. The algorithm works by 
iteratively reassigning the data points to the closest cluster center and updating the cluster centers until convergence. The number of clusters (K) is a hyperparameter 
that must be specified before running the algorithm.

**Elbow Method**
The Elbow Method is a technique used to determine the optimal number of clusters (K) in K-Means Clustering. The method involves plotting the sum of squared errors (SSE) 
for each cluster against the number of clusters. The SSE is a measure of the total distance between the data points and their corresponding cluster centers.

**The Elbow Method works as follows:**
**Plot the SSE vs. K**: Plot the SSE for each cluster against the number of clusters (K).
**Identify the Elbow**: Look for the point where the SSE starts to decrease rapidly, indicating that the algorithm is overfitting. This is the "elbow" point.
**Choose K**: Choose the number of clusters (K) corresponding to the elbow point.

The Elbow Method is useful for determining the optimal number of clusters because it helps to avoid overfitting, which can occur when the algorithm is forced to fit the 
noise in the data. By choosing the number of clusters based on the Elbow Method, you can ensure that the algorithm is not overfitting and that the clusters are meaningful.
