import Pandaz
def main():
    # TODO: Read data
    df = Pandaz.Dataframe.read_csv('/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/data/titanic.csv', '/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/data/titanic_dtype.csv')
    print(df)
    # TODO: Fill missing values
    # Numeric columns → mean
    # Categorical columns → mode
    df.fillna(num_strat=Pandaz.get_col_mean, cat_strat=Pandaz.get_col_mode)


    # TODO:Generate statistics file
    df.describe('/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/stats.csv')

    # TODO:Write cleaned data to CSV
    df.to_csv('/home/mahmoud-sayed/Desktop/ITI/Python/Mini Project/Project/output.csv')
    pass

if __name__ == "__main__":
    main()
