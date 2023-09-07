"""
File reserved for the sorting algorithm.
Based on departure stations and arrival stations.
"""

def sort_boarding_cards(boarding_cards):
    departure_dict = {}
    destination_dict = {}

    for i, bc in enumerate(boarding_cards):
        departure_dict[bc.from_station] = i
        destination_dict[bc.to_station] = i

    start_city = None
    for city in departure_dict.keys():
        if city not in destination_dict:
            start_city = city
            break

    sorted_boarding_cards = []
    current_city = start_city

    while current_city in departure_dict:
        index = departure_dict[current_city]
        sorted_boarding_cards.append(boarding_cards[index])
        current_city = boarding_cards[index].to_station

    return sorted_boarding_cards