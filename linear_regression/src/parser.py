import numpy  as np
import pandas as pd

# PARSE COVID DATA
# Base set --- https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
def ParseCovidDataset(raw_data_path = "../data/COVID19.csv", country_name = "countryterritoryCode", cases_mode = "dayily", cases_name = "cases"):

    raw_covid_data = pd.read_csv(raw_data_path)
    raw_covid_data.rename(columns = {cases_name : "cases"}, inplace = True)
    
    #del raw_covid_data["dateRep"]
    #del raw_covid_data["day"]
    #del raw_covid_data["month"]
    #del raw_covid_data["year"]
    #del raw_covid_data["deaths"]
    #del raw_covid_data["countriesAndTerritories"]
    #del raw_covid_data["geoId"]
    #del raw_covid_data["popData2019"]
    #del raw_covid_data["continentExp"]
    #del raw_covid_data["Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"]

    countries = []
    rfactor = []

    for country in raw_covid_data[country_name].unique().tolist():
    
        # Get only "cases" column for each country in right order
        country_df = raw_covid_data.loc[raw_covid_data[country_name] == country] 
        country_df = country_df.reindex(index=country_df.index[::-1])
        
        #del country_df["countryterritoryCode"]
        if cases_mode == "total":
            country_df = country_df.assign(**{"difference": country_df["cases"].diff()})
            country_df = country_df.loc[country_df["cases"] > 0]
            country_df = country_df.assign(fraction=lambda x: 100 * x.difference / x.cases)
        else:
            country_df = country_df.assign(**{"total_cases": np.cumsum(country_df["cases"].tolist())})
            country_df = country_df.loc[country_df["total_cases"] > 0]
            country_df = country_df.assign(fraction=lambda x: 100 * x.cases / x.total_cases)
    
        countries.append(country)   
        rfactor.append(country_df["fraction"].mean() / 2)
    
    covid_data = pd.DataFrame({"ISO-code" : countries, "rfactor" : rfactor})
    return covid_data

def AddParameter(df, parameter_name):
    parameter_path = "../data/" + parameter_name + ".csv"
    parameter_data = pd.read_csv(parameter_path)
    del parameter_data["Country"]
    mx = parameter_data[parameter_name].max()
    mn = parameter_data[parameter_name].min()
    parameter_data[parameter_name] = parameter_data[parameter_name].map(lambda x: (x - mn)/(mx - mn))
    df = pd.merge(df, parameter_data, on="ISO-code")
    return df

data = ParseCovidDataset()
data = AddParameter(data, "Sex-ratio")
data = AddParameter(data, "Median age")
data = AddParameter(data, "Urbanization rate")
data.to_csv("../data/clear_data.csv")
