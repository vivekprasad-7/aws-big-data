'''
from spark_start import Spark_Start
s = Spark_Start()
first_users = s.gett("/home/vivek/Documents/Interview_prep/pr/data_users.csv")
s.filter_highest(first_users).show()
'''
from main import Spark_Start
s = Spark_Start()
sqlContext = s.sparkinit()

'''
path = "/home/vivek/Documents/Interview_prep/pr/data_users.csv"
df = spark.read.csv(path, inferSchema=True, multiLine=True, header=True)
df.show()
'''
data = [('1','James',40,'US'),
                 ('2','Ben',39,'UK'),
                 ('3','Jack',57,'IN'),
                 ('4','Tom',72,'CA'),
                 ('5','Tim',22,'US'),
                 ('6','',27,'UK')]
masterDf = sqlContext.createDataFrame(data,['prsn_code','name','age','country'])
masterDf.show()
