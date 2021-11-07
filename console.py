# from models.guitar import Guitar
from models.manufacturer import Manufacturer

# import repositories.guitar_repository as guitar_repostiory
import repositories.manufacturer_repository as manufacturer_repository

manufacturer1 = Manufacturer("Gibson",1902,"Michigan")
manufacturer_repository.save(manufacturer1)
# guitar1 = Guitar("Les Paul","Black","Gibson","electric",6,2015,300,400)
# guitar_repostiory.save(guitar1)