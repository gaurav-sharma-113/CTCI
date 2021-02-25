import numpy as np
from scipy.ndimage import convolve1d
import time

def calcConv(M, K, ax):
    '''Function to convolve the given filter along the axis specified
    and also return the time spent in calculating the convolution
    ------------------------------------------------------------------
    Input arguments:
        M : The input matrix
        K : Filter
        ax : axis along which convolution is to be calculated
    ------------------------------------------------------------------
    Output:
        conv : 1D convolution along the specified axis. The mode of calculation
            is "constant" which means the padding is done by the constant value specified
            in the arguments (cval) which here is 0. This can be changed and following other 
            modes could be modified and applied : ‘reflect’, ‘nearest’, ‘mirror’, ‘wrap’
        time : time consumed in executing the operation '''

    start = time.time()
    conv = convolve1d(M, K, axis=ax, mode='constant', cval=0, output=np.int8)
    return conv, (time.time() - start)*1000

def minMax(D):
    '''Function to find and return the maximum and minimum value of
    the matrix given
    ------------------------------------------------------------------
    Input arguments:
        D : Input Matrix
    ------------------------------------------------------------------
    Output:
        max : Maximum value of the given matrix
        min : Minimum value of the given matrix '''
    
    return (D.max(), D.min())

def maticianChallenge():
    # 1. Read rows and columns 
    numRows = int(input("Input number of rows: "))
    numCols = int(input("Input number of columns: "))

    # 2. and 3. unsigned char matrix M and filling it with random non-negative numbers
    # The range of the random numbers is (0-255) 
    M = np.array(np.random.randint(0, 255, (numRows,numCols)).astype(np.ubyte))

    # Filter as given in the problem
    K = np.array([-1, 0, 1])

    # 4. and 5. Applying and storing the horizontal and vertical convolution result 
    # in Dx and Dy respectively
    Dx, timeDx = calcConv(M, K, 0)
    Dy, timeDy = calcConv(M, K, 1)

    # 6. Print the total time taken by the machine to calculate Dx and Dy
    print('Time to caculate Dx : %.2f ms'% (timeDx))
    print('Time to caculate Dy : %.2f ms' % (timeDy))

    # 7. Computing and printing the minimum and maximum values of Dx and Dy
    DxMax, DxMin = minMax(Dx)
    DyMax, DyMin = minMax(Dy)
    print("Minimum of Dx : %i and Maximum of Dx : %i" %(DxMin, DxMax))
    print("Minimum of Dy : %i and Maximum of Dy : %i" %(DyMin, DyMax))

if __name__ == "__main__":
    maticianChallenge()