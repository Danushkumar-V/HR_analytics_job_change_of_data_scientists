import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle
import typeconv

hr_dataset = pd.read_csv("D:/DK/Dev/HR_analytics_job_change_of_data_scientists/aug_train.csv")
hr_dataset = hr_dataset.drop(['enrollee_id', 'city', 'city_development_index'], axis = 1)
hr_dataset.dropna(subset = ['experience'], inplace = True, axis = 0)
hr_dataset =hr_dataset.fillna(method= "ffill")
hr_dataset.dropna(subset = ['company_size', 'company_type'], axis = 0, inplace = True)
hr_dataset_aftertypecov = typeconv.typeconvo(hr_dataset)
hr_dataset_target = hr_dataset_aftertypecov['target']
print(hr_dataset_target)
hr_dataset_features = hr_dataset_aftertypecov.drop('target', axis = 1)
print(hr_dataset_features)
knn = KNeighborsClassifier(n_neighbors =5)
knn.fit(hr_dataset_features, hr_dataset_target)
a = knn.predict(hr_dataset_features)    
print(a)
pickle.dump(knn, open('ml_model.pkl', 'wb'))