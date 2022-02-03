import pandas as pd

def new_dataframe(new_data):
    b=pd.DataFrame(new_data, columns=['gender','relevent_experience','enrolled_university','education_level','major_discipline'
                                ,'experience','company_size','company_type','last_new_job','training_hours'])
    return b