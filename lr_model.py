from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score,mean_squared_error 
import os 
import joblib 
 
class Model_Development: 
    def __init__(self,x,y): 
        self.X=x 
        self.y=y 
 
    def model(self): 
        X_train,X_test,y_train,y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=5) 
        lr=LinearRegression() 
        lr.fit(X_train,y_train) 
        y_pred=lr.predict(X_test) 
        mse=mean_squared_error(y_test,y_pred) 
        r2=r2_score(y_test,y_pred) 
 
        dir=os.path.exists("model_file") 
         
        if not dir: 
            os.mkdir('model_file') 
 
        joblib.dump(lr,"model_file/lr_model.joblib") 
 
        return mse,r2