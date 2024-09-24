import pandas as pd

df = pd.read_csv("country_vaccinations.csv")
print(df.head())
# print(df.tail())

df["Vaccinated_rate"] = (df.people_fully_vaccinated/ df.total_vaccinations)*100

df['daily_vaccination'] = df['daily_vaccinations'].fillna(df['daily_vaccinations'].mean())


df.drop('source_name',axis=1)


sorted_by_vacc = df.sort_values(by="total_vaccinations",ascending=False)
print(sorted_by_vacc)

sorted_by_date = df.sort_values(by=['date','country'])
print(sorted_by_date)

df = df.rename(columns={'iso_code':'Country_code'})
print(df)

df.index = range(1,len(df)+1)
print(df)

df['people_fully_vaccinated'] = df['people_fully_vaccinated'].fillna(0)
print(df)
# print(df.sum())

