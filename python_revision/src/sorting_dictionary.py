import functools
from functools import lru_cache, singledispatch
from collections import OrderedDict, defaultdict
from operator import itemgetter

composers = {"Johann": 65, "Ludwig": 56, "Frederic": 39, "Wolfgang": 35}
sorted_composers = dict(sorted(composers.items(), key=lambda x: x[1], reverse=True))
print(sorted_composers)

x = OrderedDict({"a": 1, "b": -1, "j": 0, "f": 4})
print(list(x.items()))
print(dict(x.items()))
print(dict(sorted(x.items())))
z = defaultdict(list)
z[0].append(1)
z["a"].append("a")
print(list(z.items()))
print(list(reversed([1, 0, 2])))

data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}


def sorting_by_skills(item):
    to_sort = item[1]["skills"]
    return (
        to_sort.get("js", 0) + to_sort.get("python", 0) + to_sort.get("java", 0)
    )  # Sum of skills...


# for val in list(data.values()):
#     print(val.get("skills"))


def sorting_by_age(item):
    return item[1]["age"]


# print(sorting_by_skills(list(data.items())))
print(list(data.items()))
# print(sorted(data.items(),key=itemgetter(sorting_by_skills(data)),reverse=True))

a = [("a", 1), ("b", 2), ("a", 3), ("d", 4), ("z", 10), ("g", 11)]
print(dict(a))
print(dict(a).get("d", 0))
print(dict(sorted(data.items(), key=lambda x: x[1]["age"])))

codes_sorted_by_value = dict(
    sorted(
        {letter: number for letter, number in a if number <= 10}.items(),
        key=itemgetter(1),
    )
)
codes_sorted_by_country = dict(
    sorted(
        {letter: number for letter, number in a if number <= 10}.items(), reverse=True
    )
)
print(codes_sorted_by_value)
print(codes_sorted_by_country)
upper_letter_codes = dict(
    sorted(
        {
            code.upper(): number
            for code, number in codes_sorted_by_country.items()
            if number < 6
        }.items(),
        key=itemgetter(1),
    )
)
print(upper_letter_codes)
