
import numpy as np
import cv2

def check(x,y):
    return ( x >=0 and x < rows) and (y >=0 and y < cols)

def laplaceFilterHelper(x,y):
    new_value = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if(check(x+i,y+j)):
                new_value += filter[1+i][1+j] * image_matrix[x+i][y+j]
                # print("(%d\t%d)" %(i,j), end="\t")
        # print()
    return new_value

def printArray(array):
    print(np.matrix(array))


def Normalize(pixel):
    return int(255*(pixel - minPixel)/(maxPixel - minPixel))



def LaplacianFilter(image):
    for i in range(rows):
        for j in range(cols):
            image[i][j] = laplaceFilterHelper(i, j)
            # print(image_matrix[i][j], end=" ")
        #     print(new_image_matrix[i][j], end="\t")
        # print()


#####################  MAIN #################################


img = cv2.imread("img2.jpg")





# laplacian Filter matrix
filter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

# Random image matrix
image_matrix = np.random.randint(10,size=(5,4))

# get rows and columns
(rows,cols) = (len(image_matrix),(len(image_matrix[0])))
# print(rows,colums)

# create new image matrix
new_image_matrix = np.arange(rows*cols).reshape(rows,cols)

print("Random Image Matrix:")
printArray(image_matrix)

print("\nMask:")
printArray(filter)

# Applying Laplacian Filter and Normalize
print("\nResult Matrix:")
LaplacianFilter(new_image_matrix)

minPixel = new_image_matrix.min()
maxPixel = new_image_matrix.max()

printArray(new_image_matrix)

print("\nNormalize Matrix:")
normalize_matrix = np.vectorize(Normalize)(new_image_matrix)
printArray(normalize_matrix)

