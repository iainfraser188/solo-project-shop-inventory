from models.guitar import Guitar
from models.manufacturer import Manufacturer

import repositories.guitar_repository as guitar_repostiory
import repositories.manufacturer_repository as manufacturer_repository

# clear tables
guitar_repostiory.delete_all()
manufacturer_repository.delete_all()
# add manufacturers to database
manufacturer1 = Manufacturer("Gibson",1902,"Michigan")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("Taylor",1974,"El Cajon")
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer("Fender",1946,"Fullerton")
manufacturer_repository.save(manufacturer3)
manufacturer4 = Manufacturer('iain',1982,"falkirk")
manufacturer_repository.save(manufacturer4)




# adds guitars to database
guitar1 = Guitar("Les Paul","Black",manufacturer1,"electric",6,2015,400,550,5)
guitar_repostiory.save(guitar1)
guitar2 = Guitar("Les Paul","White",manufacturer1,"electric",6,2015,300,400,3)
guitar_repostiory.save(guitar2)
guitar3 = Guitar("Academy 100","Tobaco Sunburst",manufacturer2,"Acoustic",6,2020,200,350,10)
guitar_repostiory.save(guitar3)
guitar4 = Guitar("Dreadnought","Black",manufacturer2,"Acoustic",12,2020,400,650,12)
guitar_repostiory.save(guitar4)
guitar5 = Guitar("Telecaster","Sunburst",manufacturer3,"electric",6,2009,340,500,2)
guitar_repostiory.save(guitar5)
guitar6 = Guitar("Les Paul","Green",manufacturer1,"electric",6,2015,400,550,5)
guitar_repostiory.save(guitar6)
guitar7 = Guitar("Les Paul","Sunburst",manufacturer1,"electric",6,2015,400,550,4)
guitar_repostiory.save(guitar7)
guitar8 = Guitar("Les Paul","Red",manufacturer1,"electric",6,2015,400,550,8)
guitar_repostiory.save(guitar8)
guitar9 = Guitar("Academy 200","Black",manufacturer2,"Acoustic",6,2020,200,350,2)
guitar_repostiory.save(guitar9)
guitar10 = Guitar("Academy 100","Red",manufacturer2,"Acoustic",6,2020,200,350,5)
guitar_repostiory.save(guitar10)
guitar11 = Guitar("Telecaster","Black",manufacturer3,"electric",6,2009,340,500,6)
guitar_repostiory.save(guitar11)
guitar12 = Guitar("Telecaster","White",manufacturer3,"electric",6,2009,340,500,3)
guitar_repostiory.save(guitar12)


