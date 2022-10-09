
import csv

year_range = list(range(1991, 2022))

def main():
    with open("./unemployment.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = [r for r in reader]

    with open("./unemployment.split.csv", "w") as fw:
        writer = csv.writer(fw)
        writer.writerow(["Country", "Year", "Rate"])
        def write_row(row):
            for year, i in zip(year_range, range(2, len(row))):
                writer.writerow([row[0], year, row[i]])

        for row in data:
            write_row(row)


if __name__ == "__main__":
    main()