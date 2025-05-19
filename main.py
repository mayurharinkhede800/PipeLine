from Read import DataReading 
from feature_engineering import Feature_Selection 
from lr_model import Model_Development 
from dotenv import load_dotenv 
import os 

load_dotenv() 
 
file_name=os.getenv("file_name") 
read_file=DataReading(file_name).read_file() 
data=Feature_Selection(read_file).varience_threshold() 
x=data.drop(columns=['quality']) 
y=data['quality'] 
mod=Model_Development(x,y).model() 
print(f"Mean Square Error : {round(mod[0],2)}") 
print(f"R2-Score : {round(mod[1],2)}") 

