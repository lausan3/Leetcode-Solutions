import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['population'] >= 25_000_000) | (world['area'] >= 3_000_000)]

    countries = df[['name','population','area']]

    return countries