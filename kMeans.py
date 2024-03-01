import copy

def manhattanDist(p1, p2):
    # Calculate the Manhattan distance between two points
    length = len(p1)
    dist = 0
    for i in range(length):
        dist += abs(p1[i] - int(p2[i]))
    return dist

def euclideanDist(p1, p2):
    # Calculate the Euclidean distance between two points
    length = len(p1)
    dist = 0
    for i in range(length):
        dist += (p1[i] - int(p2[i]))**2
    dist = dist**0.5
    return dist
    
def calculate_mean_coordinate(coordinates):
    # Calculate the mean coordinate for a list of coordinates
    # Determine the dimension of the coordinates
    dimension = len(coordinates[0])
    
    # Initialize sums for each dimension
    sums = [0] * dimension
    # Sum up all coordinates for each dimension
    for coord in coordinates:
        for i in range(dimension):
            sums[i] += int(coord[i])
    # Calculate mean for each dimension
    mean_coordinate = tuple(sum_val / len(coordinates) for sum_val in sums)
    return mean_coordinate

# Perform k-means clustering algorithm
def kMeans(centroids, input, d):
    # Remove empty elements from input
    input = [ele for ele in input if ele != []]

    # Convert input data to dictionary of points
    points = {}
    for data in input:
        coordinate = tuple(map(int, data[:-1]))  
        name = data[-1]
        points[name] = coordinate
    
    # Flag for convergence
    isdone = False
    # Dictionary to store points assigned to each centroid
    centroidAssignment = {tuple(c): [] for c in centroids} 

    while not isdone: 
        # Clear previous assignments
        for key in centroidAssignment.keys():
            centroidAssignment[key] = []
        # Assign each point to the nearest centroid
        for point in points.keys():
            minDist, nearestCentroid = float('inf'), None
            for centroid in centroidAssignment.keys():
                if d == 'manh':
                    dist = manhattanDist(centroid, points[point])
                elif d == 'e2':
                    dist = euclideanDist(centroid, points[point])
                else:
                    raise ValueError("Type of distance parameter not defined correctly")
                if dist < minDist:
                    minDist = dist
                    nearestCentroid = centroid
            centroidAssignment[nearestCentroid].append(points[point])

        # Calculate new centroids based on assigned points
        newCentroids = {}
        for centroid, assignedPoints in centroidAssignment.items():
            if assignedPoints:  
                newCentroid = calculate_mean_coordinate(assignedPoints)
                newCentroids[newCentroid] = assignedPoints
            else:
                newCentroids[centroid] = []

        # Check for convergence
        if set(newCentroids.keys()) == set(centroidAssignment.keys()):
            isdone = True
        else:
            centroidAssignment = newCentroids

    # Map points back to their original names
    newPoints = {}
    for key, val in points.items():
        newPoints[val] = key

    # Print the final clusters
    i = 1
    tempList = list(centroidAssignment.keys())
    while i <= len(tempList):
        print("C" + str(i) + " = " + "{", end='')
        print(newPoints[centroidAssignment[tempList[i-1]][0]], end='')

        for j in centroidAssignment[tempList[i-1]]:
            print(', ' + newPoints[j], end='')
        print('}')
        i += 1
    
    # Print the final centroid coordinates
    i = 0
    while i<len(tempList):
        if len(tempList[i]) >= 3:
            print('([' + str(tempList[i][0]) + ' ' + str(tempList[i][1]) + ' ' + str(tempList[i][2]) + '])')
        else:
            print('([' + str(tempList[i][0]) + ' ' + str(tempList[i][1]) + '])')
        i+=1

    return centroidAssignment

        
            

