import sys

for name in sys.argv[1:]:
    words = []

    with open(name, "r") as infile:
        for line in infile.readlines()[1:]:
            words.append(int(line.rstrip().split(",")[1]))

    size_of_20 = int(0.2 * len(words))

    weight_of_20 = sum([x for x in words[:size_of_20 + 1]])

    total_weight = sum(words)

    print(float(weight_of_20) / float(total_weight))  # should be around 80%
