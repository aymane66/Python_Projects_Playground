from covid import Covid

covid = Covid()

country = covid.get_status_by_country_name("Canada")
confirmed = country["confirmed"]
deaths = country["deaths"]
active = country["active"]
recovered = country["recovered"]

print("---------- Covid-19 Stats in Canada ----------")
print("Confirmed cases: ", confirmed)
print("Active cases: ", active)
print("Deaths: ", deaths)
print("Recovered: ", recovered)



