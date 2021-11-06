lst = []
for file in glob.glob("/home/labs/elinav/yotamco/Dietery_fiber/landscape/mice/merged/ec_maps/*tsv_ec.tsv"):
    df = pd.read_csv(file,index_col=0)
    lst.append(df.rename(columns = {"counts":file.split("/")[-1].split(".")[0]}))
mice_enz = pd.concat(lst,axis=1).fillna(0)
mice_enz = mice_enz.loc[(mice_enz / mice_enz.sum() < 1e-4).sum(axis=1) <10]
inter = np.intersect1d(enz_fib.index,mice_enz.index)
mice_fenz = mice_enz.loc[inter]
enzymes = mice_fenz.loc[(mice_fenz / mice_fenz.sum() < 1e-4).sum(axis=1) < 10].index
mice_fiber_coo = pd.DataFrame(mice_fenz.loc[enzymes].T.values @ enz_fib.loc[enzymes].values,index = mice_fenz.columns,columns=enz_fib.columns).T
mice_fiber_raa = mice_fiber_coo / mice_fiber_coo.sum()
