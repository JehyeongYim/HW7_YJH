import numpy as np
def main():
    arr = np.array([[1,2],[3,4]])
    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])
    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    B = np.array([-15,-21,18])
    
    d = np.linalg.det(arr)
    eigval, eigvec = np.linalg.eig(arr)

    c = np.cross(vec1,vec2)

    x = np.linalg.inv(A).dot(B)
    
    print("Eigenvalues: ",eigval)
    print("Eigenvectors: ",eigvec)
    print("Determinant: ",round(d,2))
    print("Cross product: ",c)
    print("Solution: ",x)
    
        
if __name__=='__main__':
    main()
