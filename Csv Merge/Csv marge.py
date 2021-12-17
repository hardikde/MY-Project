import glob ,os
import time

import pandas as pd

if (os.path.exists('mastre file.csv') and os.path.isfile('mastre file.csv')):
        os.remove('mastre file.csv')
        time.sleep(2)
        print("Old file deleted and Create New")

master_df =pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df.append(pd.read_csv(file))




# master_df.to_csv('mastre file.csv', index=False)
