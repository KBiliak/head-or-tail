while True:
    with open("head_tail.txt", "r") as file:
        content = file.readlines()

    side = input("Throw the coin and enter head or tail here: ") + "\n"

    content.append(side)

    with open("head_tail.txt", "w") as file:
        file.writelines(content)

    nr_heads = content.count("head\n")
    percentage = nr_heads / len(content) * 100

    print(f"Heads: {percentage}%")

