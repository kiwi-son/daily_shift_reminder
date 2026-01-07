import pandas as pd

from datetime import datetime

dt=datetime.now()
def storing(file, name, emp, coll):
    df=pd.read_excel(file,sheet_name=-1)
    pos=df[(df.iloc[:,1]==name) & (df.iloc[:,2]==emp)].index.tolist()
    a=pos[0]
    shift=""
    l=df.iloc[a,10:]
    for i,j in enumerate(l):
        shift=j
        col1=df.iloc[:,i+10]
        k=col1[col1==shift].index.to_list()
        manpower=[]
        for b in k:
            if df.iloc[b,1]!=name:
                manpower.append(df.iloc[b,1])
        data={
        "date": datetime(dt.year, dt.month,i+1),
        "manpower": manpower,
        "shift":shift
        }
        
        coll.insert_one(data)


    