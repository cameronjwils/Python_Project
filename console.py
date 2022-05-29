import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country('Spain')
country_repository.save(country1)
country2 = Country('Iceland')
country_repository.save(country2)
country3 = Country('America')
country_repository.save(country3)

city1 = City('Madrid', country1)
city_repository.save(city1)
city2 = City('Barcelona', country1)
city_repository.save(city2)
city3 = City('Reykjavik', country2)
city_repository.save(city3)
city4 = City('New York City', country3)
city_repository.save(city4)
city5 = City('Los Angeles', country3)
city_repository.save(city5)
city6 = City('Miami', country3)
city_repository.save(city6)