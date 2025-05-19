import pandas as pd 
from sklearn.feature_selection import VarianceThreshold 
 
class Feature_Selection:
 
    def __init__(self,dataframe): 
        self.data=dataframe 
     
    def varience_threshold(self): 
        X=self.data.drop(columns=['quality']) 
        y=self.data['quality'] 
        vt=VarianceThreshold(threshold=0.2) 
        d=vt.fit_transform(X) 
        f_name=vt.get_feature_names_out() 
     
        new_df=pd.DataFrame(d,columns=f_name) 
        data_frame=pd.concat([new_df,y],axis=1) 
        return data_frame 
 
if __name__=="__main__": 
    pass 