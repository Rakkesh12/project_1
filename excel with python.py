import pandas as pd
read_file=pd.read_csv("C:\\Users\\user685\\PycharmProjects\\pythonProject\\new\\pokemon_data.csv")
#print(read_file)
#print(read_file.head(4))
#print(read_file[['Name','Type 1']])
#print(read_file.loc[(read_file['Type 1']=='Grass')])
#print(read_file.columns)
#print(read_file.iloc[2:5])
#print(read_file.sort_values(by=['Name','Speed'],ascending=[1,0]))
#print(read_file.sort_index(ascending=False))

"""read_file['total']=read_file['HP']+read_file['Speed']
#print(read_file)
read_file['total1']=read_file['HP']+read_file['Generation']
read_file=read_file.drop(columns=['total1'])"""
#print(read_file)

#read_file['total']=read_file.iloc[:,4:10].sum(axis=1)
#print(read_file['total'])
"""print(read_file.loc[(read_file['total' ]==534)])
read_file.loc[(read_file['Type 2']==' ',['Type 2'])]=['rl']
print(read_file['Type 2'])"""

"""raki=list(read_file.columns)
print(raki)
print(read_file[raki[0:4]+[raki[-1]]])"""

#print(read_file)
#print(read_file.iloc[1:721:2])
"""read_file['total']=read_file['Speed']+read_file['Attack']+read_file['Defense']
print(read_file.iloc[1:800:2])"""
#print(read_file.loc[(read_file['Speed']>=100)])
#read_file['total']=read_file.iloc[1:800:2]

#print(read_file)
"""a=read_file['Type 1']
b=read_file['Type 2']
a,b=b,a
#print(a,b)
print(read_file[['a','b']])
#print(read_file[['Type 1','Type 2']])"""
#print(read_file.columns)
#print(read_file.swaplevel(2,3))

#print(read_file['Name'])
#print(read_file.sort_values(by=['Name']))
#data_frame_1=read_file.loc[(read_file['Name']).str[0]=='A']
"""data_frame_1=read_file.loc[(read_file['Speed'])]
print(data_frame_1)"""

#print(read_file.columns)
#print(read_file)
dates=pd.date_range(16012001,periods=800)
values=pd.Series(1,range(800))
read_file['values']=values
#file=pd.DataFrame(read_file,index=dates)
#read_file['rakkesh']=dates
#read_file['#']=dates
print(read_file)