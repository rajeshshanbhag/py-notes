##this is just a blank python document for you to get started with
import pandas as pd

co2=pd.read_csv("data/egrid2016.csv")
co2

df1=co2[["PSTATABB","PNAME","PLCO2EQA"]]
df1=df1.rename(columns={
    "PSTATABB":"State_Code",
    "PNAME":"Plant_Name",
    "PLCO2EQA":"CO2 equi"
})
df1.head()

df2=(df1.groupby('State_Code')["CO2 equi"].sum())/1000
df2.reset_index()
df2.head()

pop=pd.read_csv("data/population2016.csv")
pop=pop.rename(columns={"NAME":"Name","POPESTIMATE2016":"Population_2016"})
pop.head()

stcd=pd.read_csv("data/state_codes.csv")
stcd=stcd.rename(columns={"State":"Name","Code":"State_Code"})
stcd.head()

pop1=pd.merge(pop,stcd,how='outer',on='Name')
pop1

pop1[pop1.State_Code.isnull()]
pop1=pop1.dropna()
pop1.reset_index()
pop1.head()

df3=pd.merge(pop1,df2,how='outer',on='State_Code')
df3.head()

df3['percapita']=(df3['CO2 equi']/df3['Population_2016'])*100000
df3.head()
df3.sort_values('percapita')