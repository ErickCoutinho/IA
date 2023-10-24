import numpy as np
from src.utils import processing_all_features_sales_clean

def compute_RSS(predictions,y):
    RSS = np.sum(np.square(y - predictions))
    return RSS

def compute_MSE(predictions,y):
    MSE= np.sum(np.square(y-predictions))/len(predictions)
    return MSE
def compute_RMSE(predictions,y):
    MSE = compute_MSE(predictions, y)
    RMSE = np.sqrt(MSE)
    return RMSE
def compute_R_squared(predictions,y):
    var_pred = np.sum(np.square(predictions - np.mean(y)))
    var_data = np.sum(np.square(y-np.mean(y)))
    r_squared = np.divide(var_pred, var_data)
    return r_squared


X,y,predictions = processing_all_features_sales_clean()


print("RSS: {}".format(compute_RSS(predictions,y)))
print("MSE: {}".format(compute_MSE(predictions,y)))
print("RMSE: {}".format(compute_RMSE(predictions,y)))
print("R^2: {}".format(compute_R_squared(predictions,y)))