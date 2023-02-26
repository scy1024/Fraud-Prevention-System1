import joblib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

#加载输入的数据
df = pd.read_csv('insurance_claims.csv')
input_data=[60,23,842643,1997/11/20,'OH',500/1000,500,1215.36,3000000,432220,'MALE','MD','protective-serv','reading','wife',0,0,2015/1/22,'Single' 'Vehicle' 'Collision','Rear Collision','Total Loss','Ambulance,SC','Northbend','6655 5th Drive',9,1,'YES',1,0,'NO',56520,4710,9420,42390,'Saab',95,2000,'N']#这里是输入的数据
# input_data=[]





df=df.drop(index=df.index)
df.loc[len(input_data)]=input_data
df=df.append(pd.concat([df]*20), ignore_index=True)


#数据编码

df.replace('?', np.nan, inplace = True)
df['collision_type'] = df['collision_type'].fillna(df['collision_type'].mode()[0])
df['property_damage'] = df['property_damage'].fillna(df['property_damage'].mode()[0])
df['police_report_available'] = df['police_report_available'].fillna(df['police_report_available'].mode()[0])
to_drop = ['policy_number','policy_bind_date','policy_state','insured_zip','incident_location','incident_date',
           'incident_state','incident_city','insured_hobbies','auto_make','auto_model','auto_year', '_c39']
df.drop(to_drop, inplace = True, axis = 1)
df.drop(columns = ['age', 'total_claim_amount'], inplace = True, axis = 1)

#数据划分
X = df.drop('fraud_reported', axis = 1)
y = df['fraud_reported']
cat_df = X.select_dtypes(include = ['object'])
cat_df = pd.get_dummies(cat_df, drop_first = True)
num_df = X.select_dtypes(include = ['int64'])
X = pd.concat([num_df, cat_df], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
num_df = X_train[['months_as_customer', 'policy_deductable', 'umbrella_limit',
       'capital-gains', 'capital-loss', 'incident_hour_of_the_day',
       'number_of_vehicles_involved', 'bodily_injuries', 'witnesses', 'injury_claim', 'property_claim',
       'vehicle_claim']]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(num_df)
scaled_num_df = pd.DataFrame(data = scaled_data, columns = num_df.columns, index = X_train.index)
X_train.drop(columns = scaled_num_df.columns, inplace = True)
X_train = pd.concat([scaled_num_df, X_train], axis = 1)


#模型加载
input_data=X_test[7:8].values.tolist()[0]
test_model=joblib.load('dtc.model')
test_input=pd.DataFrame(columns=input_data)
test_input.loc[len(test_input)]=input_data
test_result=test_model.predict(pd.DataFrame(test_input))
if test_result[0]=='N':
    print('车险欺诈识别结果为：不涉及车险欺诈')
elif test_result[0]=='Y':
    print('车险欺诈识别结果为：涉及车险欺诈')