class Univariate():
    def QuanQual(df):
        Quan= [feature for feature in df.columns if df[feature].dtype != 'O']
        Qual= [feature for feature in df.columns if df[feature].dtype == 'O']
        return Quan,Qual

    def descriptive(df):
        import pandas as pd
        Quan, _ = Univariate.QuanQual(df)  
        descriptive=pd.DataFrame(index=["Mean","Median","Mode"],columns=Quan)
        for columnName in Quan:
            descriptive[columnName]["Mean"]=df[columnName].mean()
            descriptive[columnName]["Median"]=df[columnName].median()
            descriptive[columnName]["Mode"]=df[columnName].mode()[0]

        return descriptive