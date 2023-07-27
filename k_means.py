import numpy as np
import matplotlib.pyplot as plt


def initialize_centroids(points, k):
    """ randomly initialize k number of points representing centroids of 'k' clusters """
    num_of_points = len(points)
    centroids = [None, None]
    centroids[0] = np.random.randint(low=np.min(points[0]), high=np.max(points[0]), size=k)
    centroids[1] = np.random.randint(low=np.min(points[1]), high=np.max(points[1]), size=k)
    return centroids


def compute_distances(points1, points2):
    """ distance between 2 set of points in 2D plane """
    points1 = np.array(points1)
    points2 = np.array(points2)
    distances = np.sqrt(np.sum(np.square(points1 - points2), axis=1))
    return distances
    

def get_labels(points, centroids):
    """ labels = idx of minimum value of arr of dim = (points, k) along columns """
    l = len(centroids)
    labels = [np.argmin(compute_distances([point]*l, centroids)) for point in points]
    return labels


def update_centroids(points, labels, k):
    """ mean of all the points with same label kth centroid (x_mean(k), y_mean(k))"""
    centre_dict, counter = {}, {}
    centroids = [0]*k
    for i in range(len(points[0])):
        label = labels[i]
        if label in centre_dict.keys():
            centre_dict[label][0] += points[0][i]
            centre_dict[label][1] += points[1][i]
            counter[label] += 1
        else:
            centre_dict[label] = [points[0][i], points[1][i]]
            counter[label] = 1
            
    for j in range(len(centroids)):
        n = counter[j]
        centroids[j] = [centre_dict[j][0]/n, centre_dict[j][1]/n]
        
    return centroids


def should_stop(old_centroids, new_centroids, threshold=1e-5):
    """ if distance based shift between old and new centroid in below threshold then stop """
    distance = np.sum(compute_distances(old_centroids, new_centroids))
    
    if distance <= threshold:
        return True
    else:
        return False


def k_means(points, k):
    """ 
    segment the population based on the number of given clusters (k) 
    Time Complexity: O(kNI), I: number of iterations
    Space Complexity: O(k+N), where k is impliit allocation
    """
    labels = None
    
    # initialize centroids randomly
    centroids = initialize_centroids(points, k)
    iterations = 0
    while True:
        old_centroids = centroids
        labels = get_labels(points, centroids)
        centroids = update_centroids(points, labels, k)
        
        if should_stop(old_centroids, centroids):
            print("Total iterations required are: {}".format(iterations))
            break
        
        iterations += 1
        
    return labels


if __name__ == "__main__":
    a = np.random.multivariate_normal(mean=[-2.0, -2.0], cov=[[1.0, 0], [0, 1.0]], size=25).T
    b = np.random.multivariate_normal(mean=[2.0, -2.0], cov=[[0.5, 0], [0, -0.5]], size=50).T
    c = np.random.multivariate_normal(mean=[2.0, 3.0], cov=[[-0.3, 0], [0, 0.3]], size=50).T
    d = np.random.multivariate_normal(mean=[-1.0, 2.0], cov=[[0.8, 0], [0, 1.0]], size=20).T
    points = np.hstack((a, b, c, d))
    k = 4
    
    # plt.scatter(points[0], points[1])
    
    print(k)
    print(points)
    labels = k_means(points, k)
    print(labels)