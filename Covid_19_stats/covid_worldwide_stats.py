from covid import Covid

covid = Covid()


confirmed = covid.get_total_confirmed_cases()
active = covid.get_total_active_cases()
deaths = covid.get_total_deaths()
recovered = covid.get_total_recovered()

print("---------- Worldwide Covid-19 Stats ----------")
print("Total confirmed cases: ", confirmed)
print("Total active cases: ", active)
print("Total deaths: ", deaths)
print("Total recovered: ", recovered)
