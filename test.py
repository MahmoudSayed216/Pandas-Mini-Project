import dataframe



df = dataframe.Dataframe.read_csv('/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/data/titanic.csv', '/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/data/titanic_dtype.csv')


print(df)

print(df.count_nulls())

df.describe('/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project')

# j = {}

# j[0]+=1

# print(j)


# x = 'ss'
# print(isinstance(x, int))

# f = [1, 2, 3, None, None]

# print(sum(f,))
# import stats
# def x(f):
#     print(f == stats.get_col_max)
# x(stats.get_col_max)
