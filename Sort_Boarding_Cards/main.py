from models import BoardingCard
from sorting import sort_boarding_cards

def create_boarding_cards_from_file(file_path):
    """
    Create a list of boarding cards from a text file.

    :param file_path: Path to the text file containing boarding card data.
    :return: List of BoardingCard objects.
    """
    boarding_cards = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into individual fields based on the separator (| in this case)
            fields = line.strip().split('|')
            if len(fields) == 7:
                transportation_id, transportation_type, seat_id, from_station, door_id, box_office_id, to_station = fields
                boarding_card = BoardingCard(transportation_id, transportation_type, seat_id, from_station, door_id, box_office_id, to_station)
                boarding_cards.append(boarding_card)
    return boarding_cards


if __name__ == '__main__':
    sorted_boarding_cards = []
    sorted_boarding_cards = sort_boarding_cards(create_boarding_cards_from_file("stack_boarding_cards.txt"))
    for index, card in enumerate(sorted_boarding_cards, start=1):
        print(f"{index}. {card}")
    print("You have arrived at your final destination")
