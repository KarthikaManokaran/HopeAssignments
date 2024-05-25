class Univariate():
    def QuanQual(dataset):
        Quan = []
        Qual = []
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                Qual.append(columnName)
            else:
                Quan.append(columnName)
        return Quan,Qual

    
    def Univariate(dataset,Quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5_Rule",
                                        "Lesser_outlier","Greater_outlier","Min","Max","skewness","kurtosis","Var","std"],columns=Quan)
        for columnName in Quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5_Rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser_outlier"]=descriptive[columnName]["Q1:25%"]-1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Greater_outlier"]=descriptive[columnName]["Q3:75%"]+1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
            descriptive[columnName]["skewness"]=dataset[columnName].skew()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["Var"]=dataset[columnName].var()
            descriptive[columnName]["std"]=dataset[columnName].std()
    
        return descriptive


    def FreqTable(columnName,dataset):
        FreqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","Cumsum"])
        FreqTable["Unique_values"]=dataset[columnName].value_counts().index
        FreqTable["Frequency"]=dataset[columnName].value_counts().values
        FreqTable["Relative_Frequency"]=FreqTable["Frequency"]/103
        FreqTable["Cumsum"]=FreqTable["Relative_Frequency"].cumsum()
    
        return FreqTable

    def Find_outlier(dataset,Quan):
        lesser=[]
        greater=[]
        
        for columnName in Quan:
            if(descriptive[columnName]["Min"]<descriptive[columnName]["Lesser_outlier"]):
                lesser.append(columnName)
            if(descriptive[columnName]["Max"]> descriptive[columnName]["Greater_outlier"]):  
                 greater.append(columnName)
        return lesser,greater


    def Replace_outlier(dataset,lesser,greater):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser_outlier"]]=descriptive[columnName]["Lesser_outlier"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater_outlier"]]=descriptive[columnName]["Greater_outlier"]
    
        return lesser,greater


    def get_pdf_probability(dataset,startrange,endrange):
        from matplotlib import pyplot
        from scipy.stats import norm
        import seaborn as sns
        ax=sns.distplot(dataset,kde=True,kde_kws={'color':'blue'},color='Green')
        pyplot.axvline(startrange,color='Red')
        pyplot.axvline(endrange,color='Red')
    
        #generate a sample
        sample=dataset
    
        # calculate parameter
        sample_mean=sample.mean()
        sample_std=sample.std()
        print("Mean=%.3f,Standard Deviation=%.3f" % (sample_mean,sample_std))
    
        #define the distribution
        dist=norm(sample_mean,sample_std)
    
        #sample probabilities for a range of outcomes
        values=[ value for value in range(startrange,endrange)]
        Probabilities=[dist.pdf(value) for value in values]
        prob=sum(Probabilities)
        print("The area between range({},{}):{}".format(startrange,endrange,sum(Probabilities)))
    
        return prob
                

    def stdNDgraph(dataset):
        import seaborn as sns
        mean=dataset.mean()
        std=dataset.std()
        values=[i for i in dataset]
        z_score = [(( j-mean)/std) for j in values]
        sns.distplot(z_score,kde=True)
        sum(z_score)/len(z_score)
                    
                