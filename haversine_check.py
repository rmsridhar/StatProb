import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from haversine import haversine

#calc_distance is a function to calculate distance between pickup and dropoff coordinates using Haversine formula.

#haversine((45.7597, 4.8422),(48.8567, 2.3508))
pickup=(45.7597,4.8422)
drop=(48.8567,2.3508)
print(pickup)
print(haversine(pickup,drop,))
