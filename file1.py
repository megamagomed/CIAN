from ast import Lambda

list_of_address = [(['Володарское шоссе', '23 км от МКАД', 'Космос', '29 минут на транспорте'], 'https://ramenskoye.cian.ru/sale/suburban/259373625/'), 
(['Ленинградское шоссе', '30 км от МКАД', 'Поваровка', '15 минут на транспорте'], 'https://solnechnogorsk.cian.ru/sale/suburban/239685880/'), 
(['Каширское шоссе', '13 км от МКАД', 'Ильинская', '20 минут на транспорте'], 'https://ramenskoye.cian.ru/sale/suburban/236322650/'), 
(['Ленинградское шоссе', '30 км от МКАД', 'Поваровка', '13 минут на транспорте'], 'https://solnechnogorsk.cian.ru/sale/suburban/272777773/'), 
(['Волоколамское шоссе', '20 км от МКАД', 'Дедовск', '6 минут на транспорте'], 'https://dedovsk.cian.ru/sale/suburban/263698649/'), 
(['Новорязанское шоссе', '26 км от МКАД', 'Отдых', '28 минут на транспорте'], 'https://ramenskoye.cian.ru/sale/suburban/272831718/'), 
(['Ярославское шоссе', '30 км от МКАД', 'Правда', '9 минут на транспорте'], 'https://ivanteyevka.cian.ru/sale/suburban/261435461/'), 
(['Ярославское шоссе', '24 км от МКАД', 'Правда', '13 минут на транспорте'], 'https://ivanteyevka.cian.ru/sale/suburban/271802950/'), 
(['Ленинградское шоссе', '22 км от МКАД', 'Планерная', '40 минут на транспорте', 'Крюково', '30 минут на транспорте'], 'https://solnechnogorsk.cian.ru/sale/suburban/274318055/'),
(['Ленинградское шоссе', '22 км от МКАД', 'Планерная', '40 минут на транспорте', 'Крюково', '30 минут пешком'], 'https://solnechnogorsk.cian.ru/sale/suburban/274318055/')] 
def sort_list_of_adress(arg):
    intermediate_list = []
    list_of_address_mod = []
    collection_of_address = {}
    for i in range(len(list_of_address)):
        for j in list_of_address[i][0]:
            intermediate_list.append(j)
        intermediate_list.append(list_of_address[i][1])
        list_of_address_mod.append(intermediate_list)
        intermediate_list = []    

    list_of_address_mod_sorted = sorted(list_of_address_mod, key=lambda el: int(el[len(el)-2][:2]))

    print(list_of_address_mod_sorted)

 

    
    for distance in list_of_address_mod_sorted:
        station = distance[len(distance)-3]
        time = distance[len(distance)-2]
        collection_of_address[distance[len(distance)-1]] = time, station   

    print(collection_of_address)
