
import numpy as np
import cv2

class myMatrix:
    def __init__(self,image_matrix):
        # Random image matrix
        # image_matrix = np.random.randint(10, size=(5, 4))
        self.image_matrix = image_matrix
        # laplacian Filter matrix
        self.mask = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        # get rows and columns
        (self.rows, self.cols) = (len(self.image_matrix), (len(self.image_matrix[0])))
        # print(rows,colums)
        # create new image matrix
        self.new_image_matrix = np.arange(self.rows * self.cols).reshape(self.rows, self.cols)
        self.maxPixel = -9223372036854775807
        self.minPixel = 9223372036854775807

    # methods
    def check(self,x,y):
        return ( x >=0 and x < self.rows) and (y >= 0 and y < self.cols)

    def laplaceFilterHelper(self,x,y):
        new_value = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if(self.check(x+i,y+j)):
                    new_value += self.mask[1+i][1+j] * self.image_matrix[x + i][y + j]
                    # print("(%d\t%d)" %(i,j), end="\t")
            # print()
        return new_value

    def printArray(self,array):
        print(np.matrix(array))


    def Normalize(self,pixel):
        # minPixel = self.new_image_matrix.min()
        # maxPixel = self.new_image_matrix.max()
        return int(255*(pixel - self.minPixel)/(self.maxPixel - self.minPixel))



    def LaplacianFilter(self,image):
        for i in range(self.rows):
            for j in range(self.cols):
                image[i][j] = self.laplaceFilterHelper(i, j)
                if(image[i][j] < self.minPixel): self.minPixel = image[i][j]
                if (image[i][j] > self.maxPixel): self.maxPixel = image[i][j]
                # print(image_matrix[i][j], end=" ")
            #     print(new_image_matrix[i][j], end="\t")
            # print()

    def Filter(self):
        ################# MAIN ####################
        print("Random Image Matrix:")
        self.printArray(self.image_matrix)

        print("\nMask:")
        self.printArray(self.mask)

        # Applying Laplacian Filter and Normalize
        print("\nResult Matrix:")
        self.LaplacianFilter(self.new_image_matrix)

        self.printArray(self.new_image_matrix)

        print("\nNormalize Matrix:")
        normalize_matrix = np.vectorize(self.Normalize)(self.new_image_matrix)
        self.printArray(normalize_matrix)
        return normalize_matrix
    # end methods


######### MAIN ########


# m = myMatrix(np.random.randint(10, size=(5, 4)))
# m.Filter()

