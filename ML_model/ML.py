import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression, LassoCV
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict
from sklearn import metrics

bitrate2 = pd.read_excel('traning_data.xls', sheet_name='2b', na_values='n/a')
bitrate3 = pd.read_excel('traning_data.xls', sheet_name='3b', na_values='n/a')
bitrate4 = pd.read_excel('traning_data.xls', sheet_name='4b', na_values='n/a')
bitrate5 = pd.read_excel('traning_data.xls', sheet_name='5b', na_values='n/a')
resolution2 = pd.read_excel('traning_data.xls', sheet_name='2s', na_values='n/a')
resolution3 = pd.read_excel('traning_data.xls', sheet_name='3s', na_values='n/a')
resolution4 = pd.read_excel('traning_data.xls', sheet_name='4s', na_values='n/a')
resolution5 = pd.read_excel('traning_data.xls', sheet_name='5s', na_values='n/a')
framerate2 = pd.read_excel('traning_data.xls', sheet_name='2r', na_values='n/a')
framerate3 = pd.read_excel('traning_data.xls', sheet_name='3r', na_values='n/a')
framerate4 = pd.read_excel('traning_data.xls', sheet_name='4r', na_values='n/a')
framerate5 = pd.read_excel('traning_data.xls', sheet_name='5r', na_values='n/a')
combi1 = pd.read_excel('traning_data.xls', sheet_name='combi1', na_values='n/a')
combi2 = pd.read_excel('traning_data.xls', sheet_name='combi2', na_values='n/a')
mpeg4 = pd.read_excel('traning_data.xls', sheet_name='mpeg4', na_values='n/a')

raw_data = pd.concat([bitrate2, bitrate3,bitrate4,bitrate5,resolution2,resolution3,resolution4,resolution5,framerate2,framerate3,framerate4,framerate5,combi1,combi2,mpeg4],sort=True)
#raw_data = pd.concat([bitrate2, bitrate3,bitrate4,bitrate5,resolution2,resolution3,resolution4,resolution5,framerate2,framerate3,framerate4,framerate5,combi1,combi2,mpeg4],sort=True)
raw_data.dropna()
#print(raw_data[raw_data.isnull().values==True])

###processing data standardscaler



######### create training data and testing data
x = raw_data[['duration', 'size', 'bite_rate', 'width', 'height', 'r_frame_rate', 'bitrate', 'resolution', 'framerate','mpeg4']]
y = raw_data[['percentage']]
scaler = StandardScaler()
scaler.fit(x)
X = scaler.transform(x)
#print(X)

reg = LinearRegression().fit(X,y)
#reg = linear_model.Lasso(alpha=0.1)
#reg = linear_model.BayesianRidge()
'''
reg = make_pipeline(StandardScaler(),
                    MLPRegressor(hidden_layer_sizes=(100, 100),
                                tol=1e-2, max_iter=500, random_state=0))
'''
def reg_predict(data, result):
    X_train, X_test, y_train, y_test = train_test_split(data, result, test_size=0.2, random_state=0)
    X_train, X_test, y_train, y_test
    reg.fit(X_train, y_train.values.ravel())
    y_pred = reg.predict(X_test)
    print("MES:", metrics.mean_squared_error(y_test, y_pred))
    print("RMSE：", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    return y_pred

def cross_predict(data, result):
    #result_ravel = result.ravel()
    predicted = cross_val_predict(reg, data, result.values.ravel(),cv=10)#target_newrdn.values returns a numpy ndarray and you perform ravel on that.
    print("MES:", metrics.mean_squared_error(result, predicted))
    print("RMSE：", np.sqrt(metrics.mean_squared_error(result, predicted)))
    print(predicted.size)

    return predicted

######### test model
#y_pred = reg_predict(X, y)
y_pred = cross_predict(X,y)

fig, ax = plt.subplots()
ax.scatter(y, y_pred)
#ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
