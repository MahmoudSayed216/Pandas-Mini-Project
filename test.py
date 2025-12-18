import dataframe



df = dataframe.Dataframe.read_csv('/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/data/titanic.csv', '/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/data/titanic_dtype.csv')


print(df)

print(df.count_null())


# from functools import reduce



# lst = [1, 2, 3, None, 4, None, 6, None]


# f = lambda x, y: x + (1 if y is None else 0)


# x =reduce(f,lst, 0)
# print(x)
