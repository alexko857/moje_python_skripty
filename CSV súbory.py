import csv

def add_year(file_path):
    output_file = file_path.replace(".csv", "2.csv")

    with open(file_path, "r", newline="", encoding="utf-8") as fp:
        reader = csv.reader(fp)
        header = next(reader)
        header.insert(3, "Year")  # pridáme nový stĺpec Year na pozíciu 3
        rows = []

        for r in reader:
            if not r:
                continue
            title = r[2]  # pôvodný názov s rokom

            # použitie rfind na nájdenie posledných zátvoriek
            start = title.rfind("(")
            end = title.rfind(")")
            if start != -1 and end != -1:
                rok = title[start+1:end]       # vyberieme rok
                r[2] = title[:start].strip()   # odstránime rok z Title
            else:
                rok = ""

            r.insert(3, rok)   # pridáme rok do riadku
            rows.append(r)     # pridáme riadok na koniec zoznamu

    with open(output_file, "w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(header)  # zapíšeme hlavičku
        writer.writerows(rows)   # zapíšeme všetky riadky

    return output_file


def movies_by_year(year, file_path="tabulka2.csv"):
    with open(file_path, "r", newline="", encoding="utf-8") as fp:
        reader = csv.reader(fp)
        header = next(reader)

        title_index = header.index("Title")
        year_index = header.index("Year")

        for r in reader:
            if not r:
                continue
            if r[year_index] == str(year):
                print(r[title_index])


# použitie
new_file = add_year("tabulka.csv")
movies_by_year(2015, new_file)