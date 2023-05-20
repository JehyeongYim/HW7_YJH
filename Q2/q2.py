import numpy as np
def main():
    Docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])

    Query = np.array([1,1,0,0,1,0])

    doc1 = np.matmul(Docs[0], Query.T)/(np.linalg.norm(Docs[0])*np.linalg.norm(Query))
    doc2 = np.matmul(Docs[1], Query.T)/(np.linalg.norm(Docs[1])*np.linalg.norm(Query))
    doc3 = np.matmul(Docs[2], Query.T)/(np.linalg.norm(Docs[2])*np.linalg.norm(Query))

    print("doc1=",round(doc1,2))
    print("doc2=",round(doc2,2))
    print("doc3=",round(doc3,2))
    
if __name__=='__main__':
    main()
