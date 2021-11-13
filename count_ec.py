import sys
import pandas as pd

l = []
for line in sys.stdin:
    l.append(line.rstrip())
df = pd.read_csv("proteins_ids.csv",index_col=0,sep=",")
counts = df.loc[l].groupby("EC number").size().reset_index()
counts.loc[-counts["EC number"].str.contains(";")].rename(columns={0:"counts"}).to_csv(sys.argv[-1],index=None)

import numpy as np

all_enzymes = pd.read_csv('Figure1_data.csv',index_col=0)
enzyme_counts = pd.read_csv(sys.argv[-1],index_col=0)
inter = np.intersect1d(enzyme_counts.index,all_enzymes.index)
enzyme_counts_filtered = enzyme_counts.loc[inter]

df = pd.DataFrame(enzyme_counts_filtered.T.values @ all_enzymes.loc[inter].values,index = enzyme_counts_filtered.columns,columns=all_enzymes.columns).T
df = df.rename(columns={"counts":"Relative abundance"})
(df / df.sum()).to_csv(f"{sys.argv[-1][:-4]}_IFDP.tsv")
