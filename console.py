from models.guitar import Guitar
from models.manufacturer import Manufacturer

import repositories.guitar_repository as guitar_repostiory
import repositories.manufacturer_repository as manufacturer_repository

# add manufacturers to database
manufacturer1 = Manufacturer("Gibson",1902,"Michigan")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("Taylor",1974,"El Cajon")
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer("Fender",1946,"Fullerton")
manufacturer_repository.save(manufacturer3)




# adds guitars to database
guitar1 = Guitar("Les Paul","Black",manufacturer1,"electric",6,2015,400,550)
guitar_repostiory.save(guitar1)
guitar2 = Guitar("Les Paul","White",manufacturer1,"electric",6,2015,300,400)
guitar_repostiory.save(guitar2)
guitar3 = Guitar("Academy 100","Tobaco Sunburst",manufacturer2,"Acoustic",6,2020,200,350)
guitar_repostiory.save(guitar3)
guitar4 = Guitar("Dreadnought","Black",manufacturer2,"Acoustic",12,2020,400,650)
guitar_repostiory.save(guitar4)
guitar5 = Guitar("Telecaster","Sunburst",manufacturer3,"electric",6,2009,340,500)
guitar_repostiory.save(guitar5)