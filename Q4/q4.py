import pandas as pd
def main():
    data = pd.read_csv("gender2.csv",encoding='cp949',index_col=0)

    columns = ["Total","Male","Female"]
    df=pd.DataFrame([data["2022년_계_총인구수"],data["2022년_남_총인구수"],data["2022년_여_총인구수"]],columns)
    df = df.transpose()
    
    print(df)
if __name__=='__main__':
    main()
