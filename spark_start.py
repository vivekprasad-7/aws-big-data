from pyspark.sql import SparkSession
class Spark_Start():
	def __init__(self):
		self.spark = SparkSession.builder.master("local").appName("kill_It").getOrCreate()
		self.spark.sparkContext.setLogLevel("ERROR")
	def gett(self,path):
		df = self.spark.read.csv(path, inferSchema=True, multiLine=True, header=True)
		return df
	def filter_highest(self,df):
		df = df.filter(df.salary>5000).select('name')
		return df	
