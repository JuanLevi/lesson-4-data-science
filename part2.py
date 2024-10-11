
import pandas as pd

data = pd.read_csv('titanic.csv')


over18 = data.loc[data["Age"]>18,"Name"]
print(over18)

maleNames=data.loc[data['Sex']=="male","Name"]
print(maleNames)



section=data.iloc[12:25,0:2]
print(section)



section1=data.iloc[18:19,1:2]
print(section1)

data.iloc[18:19,1:2]=1

section2=data.iloc[18:19,1:2]
print(section2)

data.to_csv('change.csv')



data["40y"]=data["Age"]+40
data.to_csv('change2.csv')



data["FareAge"]=data["Fare"]/data["Age"]
data.to_csv('change3.csv')



data_rename=data.rename(
    columns={"Pclass":"Passenger Class","Parents/Children Aboard":"Family Aboard"}
)
print(data_rename)



print(data["FareAge"].mean()) #mean -> medium

print(data["Age"].min()) #min -> minumn

print(data["Fare"].max()) #max

#multiple
print(data[["Age","Fare"]].max())


print(data.agg({
    "Age":['min','max','mean','std','median'],
    "Fare":['sum','mean','median','std']
}))



print(data[["Sex","Age"]].groupby("Sex").mean())

print(data[["Pclass","Age"]].groupby("Pclass").mean())



x=data.sort_values(by="Pclass",ascending=True)
print(x.head())