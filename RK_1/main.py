from operator import itemgetter
from models.part import Part
from models.manufacturer import Manufacturer
from models.part_to_manufacturer import PartToManufacturer

#Производители
manufacturers = [
    Manufacturer(1, 'Автомир'),
    Manufacturer(2, 'Стройматериалы'),
    Manufacturer(3, 'Икея'),
    Manufacturer(4, 'Детальки'),
    Manufacturer(5, 'Авто и грузовики'),
    Manufacturer(6, 'Робототехника'),
    Manufacturer(7, 'Мастерская Богданов')
]



# Детали
parts = [
    Part(1, 'Автомобильное масло',500,1),
    Part(2, 'Доска метровая',100,2),
    Part(3, 'Гаечный ключ на 9',200,7),
    Part(4, 'Шестерня для генераторов',10000,4),
    Part(5, 'Упаковка болтов',300,4),
    Part(6, 'Цепь велосипедная',350,7),
    Part(7, 'Машинный диск',2000,5),
    Part(8, 'Транзистор',1500,6)
]

parts_to_manufacturers = [
    PartToManufacturer(1,1),
    PartToManufacturer(1,7),
    PartToManufacturer(2,2),
    PartToManufacturer(2,3),
    PartToManufacturer(3,2),
    PartToManufacturer(3,4),
    PartToManufacturer(3,7),
    PartToManufacturer(4,4),
    PartToManufacturer(5,2),
    PartToManufacturer(5,4),
    PartToManufacturer(6,7),
    PartToManufacturer(6,4),
    PartToManufacturer(7,1),
    PartToManufacturer(7,5),
    PartToManufacturer(8,6),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(part.name, part.cost, manufacturer.name)
                   for manufacturer in manufacturers
                   for part in parts
                   if part.manufacturer_id == manufacturer.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(manufacturer.name, manufacturer.id, part_to_manufacturer.part_id)
                         for manufacturer in manufacturers
                         for part_to_manufacturer in parts_to_manufacturers
                         if manufacturer.id == part_to_manufacturer.manufacturer_id]

    many_to_many = [(part.name, part.cost, manufacturer_name)
                    for manufacturer_name, part_id, part_id in many_to_many_temp
                    for part in parts 
                    if part.id == part_id]

    print('Задание Д1')
    D1 = [(part.name, part.cost, manufacturer.name)
              for manufacturer in manufacturers
              for part in parts
              if part.manufacturer_id == manufacturer.id and part.name[-2:] == "ов"]
    print(D1)


    print('\nЗадание Д2')
    D2 = []
    for manufacturer in manufacturers:
        manufacurers_parts = list(filter(lambda i: i[2] == manufacturer.name, one_to_many))
        if len(manufacurers_parts) > 0:
            parts_costs = [cost for _, cost, _ in manufacurers_parts]
            parts_avg = sum(parts_costs) / len(parts_costs)
            D2.append((manufacturer.name, parts_avg))

    D2 = sorted(D2, key=itemgetter(1), reverse=True)
    print(D2)


    print('\nЗадание Д3')
    D3 = {}
    for manufacturer in manufacturers:
        if manufacturer.name.lower().startswith('а'):
            manufacturer_parts = list(
                filter(lambda i: i[2] == manufacturer.name, many_to_many))
            parts_names = [x for x, _, _ in manufacturer_parts]
            D3[manufacturer.name] = parts_names

    print(D3)


if __name__ == '__main__':
    main()