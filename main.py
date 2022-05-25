#from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext, SQLContext


class Spark_Start():
	def sparkinit(self):
		self.conf = SparkConf()
		self.sc = SparkContext(conf=self.conf)
		self.sqlContext=SQLContext(self.sc)
		#self.spark = SparkSession.builder.master("local").appName("kill_It").getOrCreate()
		#self.spark.sparkContext.setLogLevel("ERROR")
		return self.sqlContext
	
