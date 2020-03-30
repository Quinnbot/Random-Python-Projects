import numpy as np
import matplotlib.pyplot as plt
import math

N = 10  

points = []

for i in range(N):

    x = 30*np.random.rand()
    y = 30*np.random.rand()

    points.append([x,y])
    plt.scatter(x,y)

#print(points)

shortest = 0
shortestpoints = []

for i in range(N-1):
    for j in range(i+1,N-1):

        if shortest == 0:
            shortest = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2

            shortestpoints = [points[i],points[j]]

            print(shortest)
            print(points[i])
            print(points[j])

        elif ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2) < shortest :
            shortest = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2

            shortestpoints = [points[i],points[j]]

            print(shortest)
            print(points[i])
            print(points[j])
        else:
            print((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)


print("\n\n\n\n\n\n\nFINAL:")
print("points: ")
print(shortestpoints)
print("distance: ")
print(math.sqrt(shortest))

x1, x2 = shortestpoints[0][0] , shortestpoints[1][0]
y1, y2 = shortestpoints[0][1] , shortestpoints[1][1]

plt.plot([x1,x2],[y1,y2],'k-')
plt.show()