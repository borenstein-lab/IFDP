import sys
import pandas as pd

l = []
for line in sys.stdin:
    l.append(line.rstrip())
df = pd.read_csv("proteins_ids.csv",index_col=0,sep=",")
counts = df.loc[l].groupby("EC number").size().reset_index()
counts.loc[-counts["EC number"].str.contains(";")].rename(columns={0:"counts"}).to_csv(sys.argv[-1],index=None)
