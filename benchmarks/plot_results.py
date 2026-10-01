import csv

import matplotlib.pyplot as plt


def main() -> None:
    slots = []
    algorithms = {
        "Greedy": [],
        "Divide & Conquer": [],
        "Dynamic Programming": [],
        "Backtracking": [],
        "Branch & Bound": [],
    }

    with open("benchmarks/results.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            slots.append(int(row["slots"]))
            algorithms["Greedy"].append(float(row["greedy"]))
            algorithms["Divide & Conquer"].append(float(row["divide_conquer"]))
            algorithms["Dynamic Programming"].append(float(row["dynamic_programming"]))
            algorithms["Backtracking"].append(float(row["backtracking"]))
            algorithms["Branch & Bound"].append(float(row["branch_and_bound"]))

    for name, times in algorithms.items():
        plt.plot(slots, times, marker="o", label=name)

    plt.xlabel("Number of Parking Slots")
    plt.ylabel("Average Execution Time (ms)")
    plt.title("Parking Allocation Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("benchmarks/performance_graph.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
