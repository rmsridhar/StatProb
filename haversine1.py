import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from haversine import haversine

#calc_distance is a function to calculate distance between pickup and dropoff coordinates using Haversine formula.
def calc_distance(df):
    pickup = (df['pickup_latitude'], df['pickup_longitude'])
    drop = (df['dropoff_latitude'], df['dropoff_longitude'])
    return haversine(pickup, drop)
#haversine((45.7597, 4.8422),(48.8567, 2.3508)
pickup=(df['45.7597'],df[4.8422])
drop=(df['48.8567'],df['2.3508'])
print(calc_distance(pickup,drop))
