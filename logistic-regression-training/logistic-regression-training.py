import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))


def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    n, d = X.shape #getting shape of the input matrix
    w = np.zeros(d) # initializing a weights vector of all zeros, the size being the size of the input matrix.
    b = 0.0 #initializing bias

    for i in range(steps):
        z = np.dot(X,w) + b  #calculating linear combination/sum
        p = _sigmoid(z)  #activating the linear combo using sigmoid
        l = -(1/n)*(np.sum(y*np.log(p) + (1-y)*np.log(1-p)))  #loss function
        dw = (1/n)*np.dot(X.T, (p-y))  #calculating the gradient of w wrt loss
        db = (1/n)*np.sum(p-y)  #calculating the gradient of b wrt loss
        w -= lr*dw  #updating backwards the weight
        b -= lr*db  #updating backwards the bias
        if i%100 == 0:
            print(f"Epoch {i}: Loss {l:.4f}")

    return w,b
    # Write code here
    pass