
def city_country(city, country, population=0):
    if population==0:
        return city.title() + ', ' + country.title()
    else:
        return city.title() + ', ' + country.title() + ' - population ' + str(population)

