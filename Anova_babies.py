import pandas as pd

import scipy.stats as st

from statsmodels.stats.multicomp import pairwise_tukeyhsd

from statsmodels.stats.multicomp import MultiComparison as multi


file_input = input("Please Input the File Name:")


df = pd.read_excel("/Users/thaishand/Library/Containers/com.microsoft.Excel/Data/Desktop/" + file_input + ".xlsx"
)

#print(df)

#rdf = st.f_oneway(df["x1"],df["x2"],df["Age"])

#rdf = st.f_oneway(df["x1"]df["x2"]df["age"]=="3",df["x1"]df["x2"]df["age"]=="12",df["x1"]df["x2"]df["age"]=="24")


rdf1 = st.f_oneway(df["x1"]df["age"]=="3",df["x1"]df["age"]=="12",df["x1"]df["age"]=="24")


rdf2 = st.f_oneway(df["x2"]df["age"]=="3",df["x2"]df["age"]=="12",df["x2"]df["age"]=="24")


print ("Anova Results:", rdf1, rdf2)

#mc = multi(df["x1"], df["x2"], df["Age"])

#mcresults = mc.tukeyhsd()
#print(mcresults)
