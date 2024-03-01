# Implementation of Naive Bayes classifier

# Count occurrences of a specific value in a given column
def count(val, col, train):
    ans = 0
    lis = [j[col] for j in train]
    for i in lis:
        if val == i:
            ans+=1
    return ans

def getProbability(attribute, train, laplacian, distinct_labels, verbose):
    classification = {}
    for label in distinct_labels:
        # Calculate prior probability P(C)
        num_label = count(label, -1, train)
        prob = 1
        prob = prob * num_label / len(train)
        i = 0
        if verbose:
            print('P(C={}) = [{} / {}]'.format(label, num_label, len(train)))
            
        while i<len(attribute):
            Ai = []
            new_sample = []
            # Extract samples with the specified label
            for j in train:
                if j[-1]==label:
                    new_sample.append(j)
                if j[i] not in Ai:
                    Ai.append(j[i])

            # Calculate conditional probability P(Ai | C)
            distinct_Ai = len(Ai)
            num = count(attribute[i], i, new_sample)
            if laplacian:
                num += laplacian
            denom = num_label
            if laplacian:
                denom += distinct_Ai*laplacian
            attributeProb = num / denom
            prob = prob * attributeProb
            if verbose:
                print('P(A{}={} | C={}) = {} / {}'.format(i, attribute[i], label, num, denom))
            i+=1

        classification[label] = prob
    
    # Print conditional probabilities
    for key, value in classification.items():
        if verbose:
            print('NB(C={}) = {}'.format(key, value))
    v = list(classification.values())
    k = list(classification.keys())
    
    # Return the label with the maximum conditional probability
    return k[v.index(max(v))]

def naiveBayes(train_list, test_list, laplacian, verbose):
    # Remove any empty elements from the training and test data
    train = [ele for ele in train_list if ele != []]
    test = [ele for ele in test_list if ele != []]

    # Separate training and test data into labels and coordinates
    train_labels = []
    train_attributes = []
    for row in train:
        train_labels.append(row[-1])
        train_attributes.append(row[:-1])
   
    test_labels = []
    test_attributes = []
    for row in test:
        test_labels.append(row[-1])
        test_attributes.append(row[:-1])

    # Create a set of distinct labels present in both training and test data
    distinct_labels = set(train_labels)
    distinct_labels = sorted(distinct_labels)
    distinct_testlabels = set(test_labels)
    distinct_testlabels = sorted(distinct_testlabels)

    # Initialize dictionaries to store true positive (TP), false negative (FN), 
    # and false positive (FP) counts for each label
    TP = {}
    FN = {}
    FP = {}
    for i in distinct_testlabels:
        TP[i] = 0
        FN[i] = 0
        FP[i] = 0
    predicted_class = []

    # Iterate over each test instance
    for i in range(len(test_attributes)):
        # Predict the class for the current test instance
        predicted_class = getProbability(test_attributes[i], train, laplacian, distinct_labels, verbose)
        # Update TP, FP, FN counts for each label based on classification results       
        if predicted_class == test_labels[i]:
            TP[predicted_class] += 1
            if verbose:
                print('match: "{}"'.format(predicted_class))
        else:
            FP[predicted_class] += 1
            FN[test_labels[i]] += 1
            if verbose:
                print('fail: got "{}" != want "{}"'.format(predicted_class, test_labels[i] ))
    
    # Print precision and recall for each label
    for label in distinct_labels:
        print('Label={} Precision={}/{} Recall={}/{}'.format(label, TP[label], TP[label] + FP[label], TP[label], TP[label] + FN[label]))
    
    # Return the predicted class for the last test instance (for illustrative purposes)
    return predicted_class
       
 