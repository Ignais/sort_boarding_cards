This is a very simple application created to order boarding cards. 
The application structured in four files for a better understanding of the code. 
 1. The first models.py where is the BoardingCard class which results in our main structure. 
 2. The second sorting.py file contains the sorting algorithm, 
    focused on the departure city and the arrival city. 
 3. The third file has the main.py function where the application runs and the function that
    reads the data input from a TXT file is found. 
 4. In this file stack_boarding_cards.txt it is possible to enter the desired amount of cards always taking into account the      following format:
    Transportation_ID|Transportation_Type|Seat_ID|From_Station|Door_ID|Box Office_ID|To_Station
    without spaces between bars and words.
    
To keep it simple and fast, the application does not have many validations, but it is an element to 
take into account for a more complete application. Nor was a more complete data model created, 
being able to separate the station as a class and having the box offices and gates as attributes, as 
well as the transportation creating types and the seats as attributes.
