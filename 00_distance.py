sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

for city1 in sites:
    for city2 in sites:
        if city1 != city2:
            x1, y1 = sites[city1]
            x2, y2 = sites[city2]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if (city2, city1) not in distances:  
                distances[(city1, city2)] = distance

for (a, b), d in distances.items():
    print(f"{a} - {b}: {d}")