class Univariate():
    def QuanQual(df):
        Quan= [feature for feature in df.columns if df[feature].dtype != 'O']
        Qual= [feature for feature in df.columns if df[feature].dtype == 'O']
        return Quan,Qual

    def descriptive(df,Quan):
        #Quan, _ = Univariate.QuanQual(df)  
        import pandas as pd
        import numpy as np
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5_Rule",
                                        "Lesser_outlier","Greater_outlier","Min","Max","skewness","kurtosis","Var","std"], columns=Quan)
        for columnName in Quan:
            # Measure of central tendency(Mean,median,mode)
            descriptive[columnName]["Mean"]=df[columnName].mean()
            descriptive[columnName]["Median"]=df[columnName].median()
            descriptive[columnName]["Mode"]=df[columnName].mode()[0]
            
            # Percentile
            descriptive[columnName]["Q1:25%"]=df.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=df.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=df.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(df[columnName],99)
            descriptive[columnName]["Q4:100%"]=df.describe()[columnName]["max"]
            
            # InterQuantile percentile
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5_Rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser_outlier"]=descriptive[columnName]["Q1:25%"]-1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Greater_outlier"]=descriptive[columnName]["Q3:75%"]+1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Min"]=df[columnName].min()
            descriptive[columnName]["Max"]=df[columnName].max()
            
            # skewness and kurtosis
            descriptive[columnName]["skewness"]=df[columnName].skew()
            descriptive[columnName]["kurtosis"]=df[columnName].kurtosis()

            # Variance and Standard Deviation
            descriptive[columnName]["Var"]=df[columnName].var()
            descriptive[columnName]["std"]=df[columnName].std()
        
        return descriptive

    def FreqTable(columnName,df):
        import pandas as pd
        # "Unique_values","Frequency","Relative_Frequency","Cumsum"
        FreqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","Cumsum"])
        FreqTable["Unique_values"]=df[columnName].value_counts().index
        FreqTable["Frequency"]=df[columnName].value_counts().values
        FreqTable["Relative_Frequency"]=FreqTable["Frequency"]/103
        FreqTable["Cumsum"]=FreqTable["Relative_Frequency"].cumsum()
    
        return FreqTable

    def Find_outlier(df,Quan):
        lesser=[]
        greater=[]
        
        for columnName in Quan:
            if(descriptive[columnName]["Min"]<descriptive[columnName]["Lesser_outlier"]):
                lesser.append(columnName)
            if(descriptive[columnName]["Max"]> descriptive[columnName]["Greater_outlier"]):  
                greater.append(columnName)
            
        return lesser,greater


    def Replace_outlier(df,lesser,greater):
        for columnName in lesser:
            df[columnName][df[columnName]<descriptive[columnName]["Lesser_outlier"]]=descriptive[columnName]["Lesser_outlier"]
        for columnName in greater:
            df[columnName][df[columnName]>descriptive[columnName]["Greater_outlier"]]=descriptive[columnName]["Greater_outlier"]
    
        return lesser,greater

    