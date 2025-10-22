from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

room_areas = map(lambda room: room["length"] * room["width"], rooms)
total_area = reduce(lambda a, b: a + b, room_areas)

print(f"Общая площадь квартиры: {total_area:.2f} метров квдратных")