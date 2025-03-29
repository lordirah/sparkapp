from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, lower, regexp_extract, split

spark = SparkSession.builder.appName(
    "Myapp"
).getOrCreate()

df = spark.createDataFrame(
    [
        (1, "foo"),  # create your data here, be consistent in the types.
        (2, "bar"),
    ],
    ["id", "label"]  # add your column names here
)

df.printSchema()

df.show()
