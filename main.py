import sys
import csv
from naiveBayes import *   
from kNN import *
from kMeans import *


if __name__ == "__main__":
    # Main execution block
    # Extract command line arguments
    commandLst = sys.argv[1:]

    '''
    Flags:

    -train : the training file (more below)
    -test : the testing data file (not used in kMeans)
    -K : if > 0 indicates to use kNN and also the value of K (if 0, do Naive Bayes')
    -C : if > 0 indicates the Laplacian correction to use (0 means don't use one)
    [optional] a -v verbose flag that outputs each predicted vs actual label (could be useful for testing, but not required)
    [EC-only] -d e2 or -d manh indicating euclidean distance squared or manhattan distance to use
    arguments(EC-only): if a list of centroids is provided those should be used for kMeans
    Note: it is illegal for both K and C to be greater than 0 (they both default to 0)
    '''
    # Define default parameters
    K = 0
    C = 0
    verbose = 0

    centroids = []
    mode = 'naivebayes'
    k = 0
    laplacian = 0
    
    # Parse command line arguments and set parameters
    for i in range(len(commandLst)):
        arg = commandLst[i]
        if arg == '-train':
            print('Yes')
            index = commandLst.index(arg)
            trainfile = commandLst[index+1]
        if arg == '-test':
            index = commandLst.index(arg)
            testfile = commandLst[index+1]
        if arg == '-K':
            index = commandLst.index(arg)
            if int(commandLst[index+1])>0:
                k = int(commandLst[index+1])
                mode = 'knn'
        if arg == '-C':
            index = commandLst.index(arg)
            laplacian = int(commandLst[index+1])
        if arg == '-v':
            verbose = 1
        if arg == '-d':
            mode = 'kmeans'
            index = commandLst.index(arg)
            dist_func = commandLst[index+1]
        elif ',' in arg:
            mode = 'kmeans'
            templst = arg.split(',')
            for i in range(len(templst)):
                templst[i] = float(templst[i])
            centroids.append(templst)

    # Execute the chosen mode based on input flags
    if mode == 'knn':
        with open(trainfile, mode ='r') as file:
            trainfile = csv.reader(file)
            trainfile = list(trainfile)
        
        with open(testfile, mode ='r') as file:
            testfile = csv.reader(file)
            testfile = list(testfile)
        try:
            kNN(trainfile, testfile, k)
        except:
            raise ValueError("Invalid inputs. Try again")
        
    
    elif mode == 'naivebayes':
        with open(trainfile, mode ='r') as file:
            trainfile = csv.reader(file)
            trainfile = list(trainfile)
        
        with open(testfile, mode ='r') as file:
            testfile = csv.reader(file)
            testfile = list(testfile)

        try:
            naiveBayes(trainfile, testfile, laplacian, verbose)
        except:
            raise ValueError("Invalid inputs. Try again")

    elif mode == 'kmeans':
        with open(trainfile, mode ='r') as file:
            inputfile = csv.reader(file)
            inputfile = list(inputfile)

        try:
            kMeans(centroids, inputfile, dist_func)
        except:
            raise ValueError("Invalid inputs. Try again")
    
    else:
        raise ValueError("Commandline input not defined according to the given question")
    
    

    

    

    






    
