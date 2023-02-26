from typing import List

import joblib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings

class Module(object):
    def __init__(self, input_data: List[object]):
        self.input_data = input_data


    def getResult(self):
        warnings.filterwarnings('ignore')

        # 加载输入的数据
        df = pd.read_csv('insurance_claims.csv')
        # # input_data=df[7:8].values.tolist()[0]#这里是输入的数据  yes
        # input_data = df[2:5].values.tolist()[0]  # 这里是输入的数据  no
        # input_data=[134, 29, 687698, '2000/9/6', 'OH', '100/300', 2000, 1413.14, 5000000, 430632, 'FEMALE', 'PhD', 'sales', 'board-games', 'own-child', 35100, 0, '2015/2/22', 'Multi-vehicle Collision', 'Rear Collision', 'Minor Damage', 'Police', 'NY', 'Columbus', '7121 Francis Lane', 7, 3, 'NO', 2, 3, 'NO', 34650, 7700, 3850, 23100, 'Dodge', 'RAM', 2007, 'N', 0]

        # print(self.input_data)  # <class 'list'>

        df.loc[len(self.input_data)] = self.input_data
        df = df.append(pd.concat([df] * 20), ignore_index=True)

        df.replace('?', np.nan, inplace=True)
        df['collision_type'] = df['collision_type'].fillna(df['collision_type'].mode()[0])
        df['property_damage'] = df['property_damage'].fillna(df['property_damage'].mode()[0])
        df['police_report_available'] = df['police_report_available'].fillna(df['police_report_available'].mode()[0])
        to_drop = ['policy_number', 'policy_bind_date', 'policy_state', 'insured_zip', 'incident_location', 'incident_date',
                   'incident_state', 'incident_city', 'insured_hobbies', 'auto_make', 'auto_model', 'auto_year', '_c39']
        df.drop(to_drop, inplace=True, axis=1)
        df.drop(columns=['age', 'total_claim_amount'], inplace=True, axis=1)

        # 数据划分
        X = df.drop('fraud_reported', axis=1)
        y = df['fraud_reported']
        cat_df = X.select_dtypes(include=['object'])
        cat_df = pd.get_dummies(cat_df, drop_first=True)
        num_df = X.select_dtypes(include=['int64'])
        X = pd.concat([num_df, cat_df], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
        num_df = X_train[['months_as_customer', 'policy_deductable', 'umbrella_limit',
                          'capital-gains', 'capital-loss', 'incident_hour_of_the_day',
                          'number_of_vehicles_involved', 'bodily_injuries', 'witnesses', 'injury_claim', 'property_claim',
                          'vehicle_claim']]

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(num_df)
        scaled_num_df = pd.DataFrame(data=scaled_data, columns=num_df.columns, index=X_train.index)
        X_train.drop(columns=scaled_num_df.columns, inplace=True)
        X_train = pd.concat([scaled_num_df, X_train], axis=1)

        input_data = X_test[7:8].values.tolist()[0]
        test_model = joblib.load('dtc.model')
        test_input = pd.DataFrame(columns=input_data)
        test_input.loc[len(test_input)] = input_data
        test_result = test_model.predict(pd.DataFrame(test_input))
        if test_result[0] == 'N':
            return ('车险欺诈识别结果为：不涉及车险欺诈')
        elif test_result[0] == 'Y':
            return ('车险欺诈识别结果为：涉及车险欺诈')
