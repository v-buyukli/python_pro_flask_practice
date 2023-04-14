import csv


def inches_to_cm(inches):
    return round(inches * 2.54, 2)


def pounds_to_kg(pounds):
    return round(pounds / 2.2046, 2)


def get_avg_values():
    with open("hw.csv", "r") as csvfile:
        next(csvfile)
        heights = 0
        weights = 0
        count = 0

        for row in csv.reader(csvfile):
            try:
                heights += float(row[1])
                weights += float(row[2])
                count += 1
            except IndexError:
                continue

    avg_height_inches = heights / count
    avg_weight_pounds = weights / count
    avg_height_cm = inches_to_cm(avg_height_inches)
    avg_weight_kg = pounds_to_kg(avg_weight_pounds)

    return avg_height_cm, avg_weight_kg
