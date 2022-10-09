
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
            local_max=0
            for year, i in zip(year_range, range(2, len(row))):
                writer.writerow([row[0], year, row[i]])
                local_max = max(local_max, float(row[i]))
            return local_max

        mmax = 0
        for row in data:
            mmax = max(mmax, write_row(row))

        print(mmax)


if __name__ == "__main__":
    main()