import pandas as pd
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from psi import calculate_psi

dev_df = pd.read_csv("./dev.csv")["p1"].to_numpy()  # read a CSV file inside the 'data" folder next to 'app.py'
oot1_df = pd.read_csv("./oot1.csv")["p1"].to_numpy()  # read a CSV file inside the 'data" folder next to 'app.py'
oot2_df = pd.read_csv("./oot2.csv")["p1"].to_numpy()  # read a CSV file inside the 'data" folder next to 'app.py'
val_df = pd.read_csv("./val.csv")["p1"].to_numpy()  # read a CSV file inside the 'data" folder next to 'app.py'

st.title("Application to Calculate PSI")  # add a title

option = st.selectbox(
     'Which Dataframe would you like to select?',
     ('oot1', 'oot2'))
selected_df = oot1_df if option =='oot1' else oot2_df

psi = calculate_psi(dev_df, selected_df, buckettype='quantiles', buckets=10, axis=1)

st.write("""

The calculated PSI value is: {:.2f}%

""".format(psi*100)
)

st.write("Below is the Data Frame for: {}".format(option))
st.write(selected_df) 

fig = plt.figure()
fig = sns.kdeplot(dev_df, shade=True)
fig = sns.kdeplot(selected_df, shade=True)
plt.xlabel('The P1 Values')
plt.ylabel('The Frequency')
sns.despine(left=True)
st.write(fig.figure)
