from collections import defaultdict
import csv


def main():
    with open("./employment_by_edu.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)

    m = defaultdict(lambda: defaultdict(lambda: []))
    for item in data:
        m[item[1]][item[2]].append(float(item[3]))


    with open("./employment_by_edu.2.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Edu", "Year", "Mean", "Median"])
        for edu, year_group in m.items():
            for year, val in year_group.items():
                writer.writerow([edu, year, sum(val) / len(val), val[len(val)//2]])


if __name__ == "__main__":
    main()
