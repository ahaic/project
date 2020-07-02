# TPB approved course list


import pandas as pd


url="https://www.tpb.gov.au/qas/search?page="


for i in range(418):
    
    page = url+str(i)
    
    tables = pd.read_html(page)
    print("table quantity:",len(tables))

    print(tables)

    tables[0].to_csv(r'1.csv', mode='a', encoding='utf-8', header=1, index=0)
    print('page:',i)


