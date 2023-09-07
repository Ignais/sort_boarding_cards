"""
File reserved for the structures and models of the application.
Models: BoardingCard.
"""

class BoardingCard:
    """
        Represents a boarding card with transportation details.

        :param transportation_id: Identifier of the transportation.
        :param transportation_type: Type of transportation (e.g., Train, Flight).
        :param seat_id: Seat identifier.
        :param from_station: Departure station.
        :param door_id: Door identifier (if applicable).
        :param box_office_id: Box office identifier (if applicable).
        :param to_station: Destination station.
        """
    def __init__(self, transportation_id: str, transportation_type: str,  seat_id: str,
                 from_station: str, door_id: str, box_office_id: str, to_station: str):
        self.transportation_id = transportation_id
        self.transportation_type = transportation_type
        self.seat_id = seat_id
        self.from_station = from_station
        self.door_id = door_id
        self.box_office_id = box_office_id
        self.to_station = to_station

    def __str__(self):
        return f"Take the {self.transportation_type} {self.transportation_id} " \
               f"from {self.from_station} to {self.to_station} {'Gate ' + self.door_id if self.door_id else ''}. " \
               f"{'Sit in seat '+ self.seat_id if self.seat_id else 'No seat assignment'}. " \
               f"{'Baggage drop at ticket counter '+ self.box_office_id if self.box_office_id else 'Baggage will we automatically transferred from your last leg'}."
