from itertools import combinations, chain



def get_powerset(s: set) -> list[set]:
    """
    Given set s this function returns list of all non-empty subsets of the set s
    """
    return [set(el) for el in list(chain.from_iterable(
        list(combinations(s, i + 1)) for i in range(1, len(s) + 1, 1)
    ))]

if __name__ == "__main__":

    S = {"a", "b", "c", "d", "e"}
    print(get_powerset(s=S))
    print(get_powerset(s={"a", 1, 3}))
