import pandas as pd
def main():
    data = {'unit price':[1000,280,900],
            'number':[25,120,30]}
    index = ["store1","store2","store3"]

    store1 = [1000,25]
    store2 = [280,120]
    store3 = [900,30]

    df = pd.DataFrame(data, index)
    print(df)

    total_price = [0,0,0]
    for i in range(0,3,1):
        total_price[i] = data.get('unit price')[i]*data.get('number')[i]

    df['total price'] = total_price
    print(df)

    df_sort = df.sort_values(by='total price' ,ascending=False)
    print(df_sort[0:2])

if __name__=='__main__':
    main()
