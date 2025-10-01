import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Sorting Algorithms
# -----------------------------

def bubble_sort(my_list):
    steps = 0
    a = my_list[:]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 1  # comparison
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps += 3  # swap
    return a, steps


def selection_sort(my_list):
    steps = 0
    a = my_list[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1  # comparison
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            steps += 3  # swap
    return a, steps


def insertion_sort(my_list):
    steps = 0
    a = my_list[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            steps += 1  # comparison
            a[j + 1] = a[j]
            steps += 1
            j -= 1
        a[j + 1] = key
        steps += 1
    return a, steps


# Recursive insertion sort (subarray version)
def insertion_sort_subarray(mylist, left, right):
    steps = 0

    def rec(i):
        nonlocal steps
        if i > right:
            return
        key = mylist[i]
        j = i - 1
        while j >= left and mylist[j] > key:
            steps += 1
            mylist[j + 1] = mylist[j]
            j -= 1
        mylist[j + 1] = key
        rec(i + 1)

    rec(left + 1)
    return mylist, steps


# Quick Sort (with randomized pivot to avoid recursion crash)
def quick_sort(my_list):
    steps = 0
    a = my_list[:]

    def partition(lo, hi):
        nonlocal steps
        pivot_index = random.randint(lo, hi)
        a[pivot_index], a[hi] = a[hi], a[pivot_index]
        steps += 3

        pivot = a[hi]
        i = lo - 1
        for j in range(lo, hi):
            steps += 1  # comparison
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                steps += 3
        a[i + 1], a[hi] = a[hi], a[i + 1]
        steps += 3
        return i + 1

    def _qs(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            _qs(lo, p - 1)
            _qs(p + 1, hi)

    _qs(0, len(a) - 1)
    return a, steps


# -----------------------------
# Step 2: Testing Scenarios
# -----------------------------

def test_cases(n=20):
    best = list(range(n))          # already sorted
    worst = list(range(n, 0, -1))  # reverse sorted
    avg = [random.randint(0, n) for _ in range(n)]
    return {"best": best, "worst": worst, "avg": avg}


# -----------------------------
# Step 3: Plot T(n) vs n
# -----------------------------

def plot_Tn_worst_case():
    sizes = [10, 50, 100, 500, 1000, 5000]
    algos = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "quick": quick_sort,
    }

    for name, fn in algos.items():
        results = []
        for n in sizes:
            arr = list(range(n, 0, -1))  # worst case: descending
            _, steps = fn(arr)
            results.append(steps)
        plt.plot(sizes, results, label=name)

    plt.title("T(n) vs n (Worst Case)")
    plt.xlabel("n")
    plt.ylabel("Steps")
    plt.legend()
    plt.show()


# -----------------------------
# Step 4: Plot Time vs n
# -----------------------------

def plot_time_worst_case():
    sizes = [10, 50, 100, 500, 1000, 5000]
    algos = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "quick": quick_sort,
    }

    for name, fn in algos.items():
        times = []
        for n in sizes:
            arr = list(range(n, 0, -1))
            start = time.time()
            fn(arr)
            end = time.time()
            times.append(end - start)
        plt.plot(sizes, times, label=name)

    plt.title("Time vs n (Worst Case)")
    plt.xlabel("n")
    plt.ylabel("Seconds")
    plt.legend()
    plt.show()


# -----------------------------
# Main
# -----------------------------

def main():
    print("== Step 1: sort a list of length 100 ==")
    arr = [random.randint(0, 100) for _ in range(100)]
    for fn in [bubble_sort, selection_sort, insertion_sort, quick_sort]:
        sorted_list, steps = fn(arr)
        print(f"{fn.__name__:25} sorted_ok={sorted_list == sorted(arr)} steps={steps}")
    sorted_list, steps = insertion_sort_subarray(arr[:], 0, len(arr) - 1)
    print(f"insertion_sort_subarray      sorted_ok={sorted_list == sorted(arr)} steps={steps}")

    print("\n== Step 2: T(n) best / worst / average (n=20) ==")
    cases = test_cases(20)
    for case_name, arr in cases.items():
        print(f"\nCase: {case_name}")
        for fn in [bubble_sort, selection_sort, insertion_sort, quick_sort]:
            _, steps = fn(arr)
            print(f"  {fn.__name__:20} T(n)={steps}")

    print("\n== Step 3: Plotting T(n) worst case ==")
    plot_Tn_worst_case()

    print("\n== Step 4: Plotting Time worst case ==")
    plot_time_worst_case()


if __name__ == "__main__":
    main()
