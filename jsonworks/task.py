from json import load

f=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\jsonworks\\countries.json",encoding="UTF-8")

country_data = load(f)

# 1.Number of data
# print(len(country_data))

# 2. Find the largest populated country.    

# def get_population(c):
#     return c.get("population")

largest_populated_country = max(country_data, key=lambda c:c.get("population"))
# print(f"{largest_populated_country.get("name")} : {largest_populated_country.get("population")}")

#3.find the country with lowest population

def get_population(dic):

    return dic.get("population")

min_population=min(country_data,key=get_population)

# print(min_population)

# 4. Which countries have more than one official language?

country_language_filter = [c.get("name") for c in country_data if len(c.get("languages")) > 1]
# print(country_language_filter)

# 5. Find the country with the smallest area.

def get_area(c):
    return c.get("area") if c.get("area") is not None else float('inf')

smallest_country = min(country_data, key=get_area)
# print(smallest_country.get("name"))

# 6. List all countries with a capital that starts with the letter 'A'.

country_capitalA = [c.get("name") for c in country_data if c.get("capital") is not None and c.get("capital").startswith("A")]
# print(country_capitalA)

# 7. List countries that have more than one timezone.

country_timezone_filter = [c.get("name") for c in country_data if len(c.get("timezones")) > 1]
# print(country_timezone_filter)

# 8. Find the country with the highest latitude.

def get_latitude(c):
    return c.get("latlng")[0] if c.get("latlng") is not None else 0

highest_lat_country = max(country_data, key=get_latitude)
# print(highest_lat_country.get("name"))

# 9. List all countries with a population less than 1 million.

countries_population_filter = [c.get("name") for c in country_data if c.get("population") < 1000000]
# print(countries_population_filter)

# 10. Find countries where the capital city's name is the same as the country's name.

countries_capital_filter = [c.get("name") for c in country_data if c.get("capital") == c.get("name")]
# print(countries_capital_filter)

# 11.country which is intependent

country=[i.get("name") for i in country_data if i.get("independent")==True]

# print(country)

# 12.subregion=westernasia

subregion=[i.get("name") for i in country_data if i.get("subregion")=="Western Asia"]

# print(subregion)

# 13. Find all countries where the currency is Euro (EUR) and not in the region Europe.
        
def is_euro(c):
    if c.get("currencies") != None:
        for curr in c.get("currencies"):
            return curr.get("code") == "EUR" 

country_currency_filter = [c.get("name") for c in country_data if is_euro(c) and c.get("region") != "Europe"]
print(country_currency_filter)

# 14. Find the countries that are located in the region Asia and have a border with India.

def is_border_with_ind(c):
    if c.get("borders") is not None:
        if "IND" in c.get("borders"):
            return True

countries_region_filter = [c.get("name") for c in country_data if is_border_with_ind(c) and c.get("region") == "Asia"]
# print(countries_region_filter)


        