
# A generator in Python is a special type of iterator that allows you to iterate over a potentially large
# sequence of data efficiently. It produces values on-the-fly and does not store the entire sequence in memory.
# Suited for scenarios with large datasets where loading everything into memory is not feasible.
def topten():
    yield 5
    yield 6
    yield 7
    yield 8


val = topten()
print(val.__next__())
print(next(val))
for i in val:
    print(i)


def prefect_sq():
    n = 1
    while n < 10:
        sq = n * n
        yield sq
        n += 1


sq = prefect_sq()
for i in sq:
    print(i)

# another way of writing the generator function
generator_exp = (i * 5 for i in range(5) if i%2==0)

for i in generator_exp:
    print(i)
