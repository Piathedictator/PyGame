#WP7
#7.1
print("Zuerst muss das math modul import werden. Man erstellt die Lambda Funktion wie angegeben, aus der Wurzel der addierten Quardrate von Vector Element an Index 1. (vec_elem[0]) und Vector Element an Index 2. (vec_elem[1]) von jedem Vector. Nachdem die Lambda Funktion alle Längerberechnet hat, werden sie durch .sort sortiert")
import math

vectors = [(9, 1), (8, 2), (7, 3), (6, 4), (5, 5)]

vectors.sort(key=lambda vec_elem: vec_elem[0]**2 + vec_elem[1]**2)
#print(vectors)

#7.2
import random

def approximate_pi(N=10000):
    inside_circle = 0

    for item in range(N):
        # Generate random (x, y) coordinates between [0, 1)
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check if the point is inside the unit circle
        if x**2 + y**2 < 1:
            inside_circle += 1

    # Calculate pi approximation based on the ratio
    pi_estimate = (inside_circle / N) * 4
    return pi_estimate

# Example usage
print(approximate_pi(100000))  # Higher N gives a better approximation
