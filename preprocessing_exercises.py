import numpy as np
import pandas as pd
import random as rd
import os 
from os.path import dirname


def main():
    os.makedirs(dirname(__file__) + '/d2l_ch2_ppe', exist_ok=True)
    data_file = os.path.join(dirname(__file__) + '/d2l_ch2_ppe', 'preprocessing_exercises.csv')

    with open(data_file, 'w') as f:
        f.write('NumRooms, NumBath, SQFT, YearBuilt, Price\n')
        i = 0
        while i < 10:
            rooms = [np.nan, np.random.randint(1,4)]
            bath = [np.nan, np.random.randint(1,4)]
            price = [np.nan, np.random.randint(100000, 200000)]
            sqft = [np.nan, np.random.randint(1000, 4000)]
            built = [np.nan, np.random.randint(1900, 2000)]
            randomvect = ([str(rd.choice(rooms)),str(rd.choice(bath)),str(rd.choice(sqft)),str(rd.choice(built)),str(rd.choice(price))])
            line = ','.join(randomvect) + '\n'
            f.write(line)
            i += 1
    
    data = pd.read_csv(data_file)
    # print(data)
    inputs, outputs = data.iloc[:,0:4], data.iloc[:,4]
    npinputs = np.array(inputs.values)
    i, counter, maxnan, clmn_maxnan = 0, 0, 0, 0
    while i < 4:
        j = 0
        while j < 10:
            if np.isnan(npinputs[j,i])==True:
                counter += 1
            j += 1
        if counter > maxnan:
            maxnan = counter
            clmn_maxnan = i
        counter = 0
        i += 1
    data = data.drop(data.columns[clmn_maxnan], axis = 1)
    print(data,'\n\n\n')
    npdata = np.array(data.iloc[:,:].values)
    print(npdata)
main()
