import requests
import pandas as pd
from datetime import datetime


def current_sales():
    DH_forsale = []
    for i in range(0, 8686, 50):
        url = "https://api.opensea.io/api/v1/assets?order_direction=asc&offset=" + str(i) + "&limit=50&collection" \
                                                                                            "=darkhorizon"
        response = requests.get(url)
        r = response.json()

        for j in range(len(r["assets"])):
            # print(len(r["assets"]))
            if r["assets"][j]["sell_orders"] is not None:
                price = float(r["assets"][j]["sell_orders"][0]["current_price"]) / 1000000000000000000
                print(r["assets"][j]["token_id"], price)
                DH_forsale.append({'ID': int(r["assets"][j]["token_id"]), 'Price': price})
    df = pd.DataFrame.from_dict(DH_forsale)
    # df.to_excel(fileName, index=False)
    return df


if __name__ == '__main__':
    now = datetime.now()
    print("now =", now)
    # dd_mm_YY_H_M
    dt_string = now.strftime("%d_%m_%Y_%H_%M")
    df = current_sales()
    # df = pd.read_excel('DH_prices15_10_2021_18_31.xlsx')
    df1 = pd.read_excel('DH_Rarity.xlsx')
    left_merged = df.merge(df1, how="left", on='ID')
    left_merged['rarity/eth'] = left_merged.apply(lambda row: row.Rarity /
                                                  row.Price, axis=1)
    left_merged = left_merged.sort_values(by='rarity/eth', ascending=False)
    left_merged.to_excel('DH_prices' + dt_string + '.xlsx', index=False)
