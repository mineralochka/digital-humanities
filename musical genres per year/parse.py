import re

times = {}

with open("music.csv", "r") as infile:
    for line in infile.read().split("\n")[1:-1]:
        years = line.split(",")[1]
        date = map(int, re.findall(r'\d+', years))  # get all (1 or 2) numeric sequences from string
        if len(date) > 1:
            year = date[1]
        else:
            year = date[0]

        year = year // 10 * 10  # convert to decade

        if year in times.keys():
            times[year] += 1
        else:
            times[year] = 1

with open("parsed.tsv", "w") as outfile:  # Ctrl-C -> Pages/Excel -> Ctrl-V
    for x in sorted(times.keys()):
        outfile.write(str(x) + "\t" + str(times[x]) + "\n")
