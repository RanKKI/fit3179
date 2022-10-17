from collections import defaultdict
import csv


def main():
    with open("./employment_by_age_2021.2.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)
    k = defaultdict(lambda: [])
    kk = defaultdict(lambda: defaultdict(lambda: []))
    r = (2007, 2021)

    for row in filter(lambda x: x, data):
        name, group, year, val = row
        if not year:
            continue
        k[name].append(int(year))
        kk[name][int(year)].append(row)

    filtered_k = {}
    for name, years in k.items():
        if r[0] not in years or r[1] not in years:
            continue
        filtered_k[name] = years

    print(len(k))
    print(len(filtered_k))

    with open("./out.csv", "w") as f:
        writer = csv.writer(f)
        for name, years in filtered_k.items():
            for year in range(*r):
                writer.writerow([name, ])



if __name__ == "__main__":
    main()
