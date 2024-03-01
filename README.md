
# Artificial Intelligence Lab 4
## Overview
This program demonstrates the implementation of two supervised learning algorithms: k-Nearest Neighbors (kNN) and Naive Bayes, with an additional implementation of the unsupervised k-Means algorithm for extra credit. It can operate in three modes based on command-line arguments: kNN, Naive Bayes, or k-Means.

## Running the Program
The program accepts various command-line arguments to specify the mode of operation and other parameters:

Example usage:
python3 program.py -train training_data.csv -test test_data.csv -K 3

### Flags
- `-train`: Specifies the training data file (CSV format).
- `-test`: Specifies the testing data file (CSV format, not used in kMeans).
- `-K`: If > 0, use kNN with this value of K; if 0, use Naive Bayes.
- `-C`: If > 0, apply Laplacian correction with this value; 0 means no correction.
- `-v`: Optional verbose flag for detailed output.
- `-d`: [Extra Credit only] Specifies the distance function ('e2' for Euclidean squared, 'manh' for Manhattan).
- Additional arguments: [Extra Credit only] A list of centroids for kMeans.

Note: It is illegal for both `-K` and `-C` to be greater than 0.

## Input Format
Both the training and testing data files are CSV files where each line represents a record. The last entry in a row is the label (alphanumeric), and the preceding entries are integer features.

## Algorithms

### kNN
- Uses Euclidean distance squared (weighted) for classification.
- Requires parameter `-K` to indicate the number of nearest neighbors.
- Computes distances to training points and uses their weighted vote for classification.

### Naive Bayes
- Loads training data and computes conditional and pure probabilities.
- For prediction, uses argmax per class for label prediction.
- Accepts a Laplacian correction parameter `-C`.

### kMeans (Extra Credit)
- Clusters data points around specified centroids.
- Alternates between clustering and recalculating centroids until convergence.
- Outputs final centroids and clustering results.

## Output
The program records true positives, false positives, and negatives for precision and recall calculations. Precision and recall are printed for each label in fraction form.

#
