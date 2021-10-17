import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


def rarityTools(fileName, collection_url):
    CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path="D:\Arron\Downloads\chromedriver_win32\chromedriver.exe",
                              chrome_options=chrome_options)
    n = 0
    df = pd.DataFrame()
    while True:
        DH_rarity = []
        if os.path.exists(fileName):
            df = pd.read_excel(fileName)
            n = df["ID"].iloc[-1]
        for j in range(1 + n, n + 20):
            url_1 = collection_url + str(j)
            driver.implicitly_wait(60)
            driver.get(url_1)
            score = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div[2]")
            # token_id = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div[2]/div/div[1]/div/div[3]/div[2]")
            rarity_score = score.text
            DH_rarity.append({'ID': j, 'Rarity': float(rarity_score)})
            print(j)
        table = pd.DataFrame(data=DH_rarity)
        if not df.empty:
            df = df.append(table, ignore_index=True)
            print(df)
            df.to_excel(fileName, index=False)
        else:
            table.to_excel(fileName, index=False)


if __name__ == '__main__':
    rarityTools('DH_rarityt.xlsx', "https://rarity.tools/darkhorizon/view/")
