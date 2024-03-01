# Function to calculate the Euclidean distance between two points in n-dimensional space
def eucleadean_dist(x1, x2):
    distance = 0
    # Iterate over each dimension and calculate the squared difference
    for i in range(len(x1)):
        distance += (x1[i] - x2[i])**2
    # Take the square root of the sum of squared differences
    distance = distance**0.5
    return distance

# k-Nearest Neighbors classification algorithm
def kNN(train_data, test_data, K):
    # Remove any empty elements from the training and test data
    train = [ele for ele in train_data if ele != []]
    test = [ele for ele in test_data if ele != []]

    # Separate training and test data into labels and coordinates
    train_labels = []
    train_coordinates = []
    for row in train:
        train_labels.append(row[-1])
        train_coordinates.append(list(map(int, row[:-1]))) 
    test_labels = []
    test_coordinates = []
    for row in test:
        test_labels.append(row[-1])
        test_coordinates.append(list(map(int, row[:-1])))

    # Create a set of distinct labels present in both training and test data
    distinct_labels = set(train_labels + test_labels)
    distinct_labels = sorted(distinct_labels)

    # Initialize dictionaries to store true positive (TP), false negative (FN), 
    # and false positive (FP) counts for each label
    TP = {}
    FN = {}
    FP = {}
    for i in distinct_labels:
        TP[i] = 0
        FN[i] = 0
        FP[i] = 0

    final_class = []

    # Iterate over each test instance
    for i in range(len(test_coordinates)):
        pred_instances = []
        flag = 0
        # Iterate over each training instance
        for j in range(len(train_coordinates)):
            # Calculate the Euclidean distance between the test and training instances
            dist = eucleadean_dist(test_coordinates[i], train_coordinates[j])
            # Handle the case where distance is zero (avoid division by zero)
            if int(dist) == 0:
                weight = float('inf')
                pred_instances = (weight, train_labels[j])
                flag = 1
                break
            else:
                weight = 1/dist
                pred_instances.append((weight, train_labels[j]))
        
        # If no zero distance was encountered, perform kNN classification
        if flag == 0:
            # Sort the predictions based on weights in descending order
            top = sorted(pred_instances, key=lambda tup: tup[0], reverse=True)
            topk = top[:K]
            # Count the occurrences of each label in the top K predictions
            classify_count = {}
            for instance in topk:
                if instance[1] not in classify_count:
                    classify_count[instance[1]] = 1
                else:
                    classify_count[instance[1]] += 1
            # Determine the predicted class by selecting the one with the highest count
            max_freq = max(classify_count.values())
            # Store the predicted class for this test instance
            predicted_class = []
            for key, val in classify_count.items():
                if val == max_freq:
                    predicted_class.append(key)
            predicted_class = sorted(predicted_class)
            final_class.append(predicted_class[0])
        # If zero distance was encountered, use the label from that instance
        else:
            final_class.append(pred_instances[1])

        # Print the actual and predicted labels for each test instance
        print("want={} got={}".format(test_labels[i],final_class[-1]))

        # Update TP, FP, FN counts for each label based on classification results
        if test_labels[i] == final_class[-1]:
            TP[final_class[-1]] += 1
        else:
            FP[final_class[-1]] += 1
            FN[test_labels[i]] += 1
    # Print precision and recall for each label
    for label in distinct_labels:
        print('Label={} Precision={}/{} Recall={}/{}'.format(label, TP[label], TP[label] + FP[label], TP[label], TP[label] + FN[label]))
    # Return the final predicted classes for all test instances
    return final_class



        




