import pandas as pd 
class DataReading: 
    def __init__(self,filepath): 
        self.file=filepath 
 
    def read_file(self): 
        df=pd.read_csv(self.file) 
        return df
    
if __name__=="__main__": 
    obj=DataReading(r"../winequality_red.csv") 
    r=obj.read_file() 
    print(r)