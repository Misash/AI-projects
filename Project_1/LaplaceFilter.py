
import numpy as np



filter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

image_matrix = np.array(
              [[3,0,5,0],
              [3,0,1,0],
              [4,0,0,0],
              [7,0,7,0]])


def check(x,y):
    return ( x >=0 and x < rows) and (y >=0 and y < colums)

def laplaceFilter(x,y):
    new_value = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if(check(x+i,y+j)):
                new_value += filter[1+i][1+j] * image_matrix[x+i][y+j]
                # print("(%d\t%d)" %(i,j), end="\t")
        # print()
    return new_value



(rows,colums) = (len(image_matrix),(len(image_matrix[0])))
# print(rows,colums)

new_image_matrix = np.arange(rows*colums).reshape(rows,colums)

for i in range(rows):
    for j in range(colums):
        new_image_matrix[i][j] = laplaceFilter(i,j)
        # print(image_matrix[i][j], end=" ")
        print(new_image_matrix[i][j], end="\t")
    print()


