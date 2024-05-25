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