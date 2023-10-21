from pyspark.sql import SparkSession
from pyspark.ml.feature import StandardScaler, VectorAssembler, Imputer, StringIndexer
from pyspark.ml.regression import LinearRegression, RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
from pyspark.sql.functions import col
import pyspark.sql.functions as F

# Create Spark session
spark = SparkSession.builder.appName("housing").getOrCreate()

# Load dataset
housing_df = spark.read.csv("housing.csv", header=True, inferSchema=True).limit(1000)

# Convert Categorical values to numerical
map_expr = F.create_map([F.lit(x) for x in chain(*myMapCat.items())])
housing_df = housing_df.withColumn("ocean_proximity", map_expr[housing_df["ocean_proximity"]])

# Handle Missing Values
imputer = Imputer(strategy="median", inputCols=["total_bedrooms"], outputCols=["total_bedrooms"])  # Add other cols if needed
housing_df = imputer.fit(housing_df).transform(housing_df)

# Feature Scaling
features = [col_name for col_name in housing_df.columns if col_name != "median_house_value" and col_name != "ocean_proximity"]
assembler = VectorAssembler(inputCols=features, outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")

# Train-Test Split
train_data, test_data = housing_df.randomSplit([0.7, 0.3], seed=0)

# Linear Regression
lin_reg = LinearRegression(featuresCol="scaled_features", labelCol="median_house_value")
pipeline = Pipeline(stages=[assembler, scaler, lin_reg])
model = pipeline.fit(train_data)
predictions = model.transform(test_data)

evaluator = RegressionEvaluator(labelCol="median_house_value", predictionCol="prediction")
r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})
rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})

print("Linear Regression - R-squared:", r2)
print("Linear Regression - Root Mean Squared Error:", rmse)

# RandomForest
rf_reg = RandomForestRegressor(featuresCol="scaled_features", labelCol="median_house_value", numTrees=100)
pipeline = Pipeline(stages=[assembler, scaler, rf_reg])
model = pipeline.fit(train_data)
predictions = model.transform(test_data)

r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})
rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})

print("Random Forest - R-squared:", r2)
print("Random Forest - Root Mean Squared Error:", rmse)

# Note: KNN isn't natively supported in PySpark's MLlib, so it's omitted from this conversion.

# Close Spark session
spark.stop()
