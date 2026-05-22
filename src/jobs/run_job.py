from src.transformations.clean import clean_data

def run():

    data = [1,2,None, 4]

    result = clean_data(data)
    print(result)