from sklearn import linear_model
import numpy as np



# with numpy
def func_numpy(x_train, y_train, x_test):
    X = np.asmatrix(np.array(x_train))
    Y = np.transpose(np.asmatrix(np.array(y_train)))
    X_test= np.asmatrix(np.array(x_test))
    Xt = np.transpose(X)
    
    # B = (X^T * X)^(-1) * X^T * Y
    B = np.dot(np.dot(np.linalg.inv(np.dot(Xt,X)), Xt), Y)
    Y_predicted = np.dot(X_test , B)
    
    for e in Y_predicted:
        print(f'{float(e):.2f}')

# with sklearn
def func_sklearn(x_train, y_train, x_test):
    lm = linear_model.LinearRegression()
    lm.fit(x_train, y_train)
    y_predicted = lm.predict(x_test)
    
    for e in y_predicted:
        print(f'{e:.2f}')

# print y predicted

if __name__ == '__main__':
    m, n = tuple(map(int, input().strip().split()))
    y_train = []
    x_train = []
    
    for i in range(n):
        inp = list(map(float, input().rstrip().split()))
        x_train.append(inp[:-1])
        y_train.append(inp[-1])
        
    q = int(input().strip())
    
    x_test = []
    for i in range(q):
        x_test.append(list(map(float, input().rstrip().split())))
        
    
    func_sklearn(x_train, y_train, x_test)
