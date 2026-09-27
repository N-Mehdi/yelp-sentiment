from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    LongType,
    MapType,
    StringType,
    StructField,
    StructType,
)

REVIEW_SCHEMA = StructType(
    [
        StructField("review_id", StringType(), nullable=False),
        StructField("user_id", StringType(), nullable=False),
        StructField("business_id", StringType(), nullable=False),
        StructField("stars", DoubleType()),
        StructField("useful", LongType()),
        StructField("funny", LongType()),
        StructField("cool", LongType()),
        StructField("text", StringType()),
        StructField("date", StringType()),  # converti en timestamp après lecture
    ]
)

BUSINESS_SCHEMA = StructType(
    [
        StructField("business_id", StringType(), nullable=False),
        StructField("name", StringType()),
        StructField("address", StringType()),
        StructField("city", StringType()),
        StructField("state", StringType()),
        StructField("postal_code", StringType()),
        StructField("latitude", DoubleType()),
        StructField("longitude", DoubleType()),
        StructField("stars", DoubleType()),
        StructField("review_count", LongType()),
        StructField("is_open", IntegerType()),
        StructField("attributes", MapType(StringType(), StringType())),
        StructField("categories", StringType()),
        StructField("hours", MapType(StringType(), StringType())),
    ]
)

# friends et compliment_* volontairement absents : Spark ne les lit pas
USER_SCHEMA = StructType(
    [
        StructField("user_id", StringType(), nullable=False),
        StructField("name", StringType()),
        StructField("review_count", LongType()),
        StructField("yelping_since", StringType()),
        StructField("useful", LongType()),
        StructField("funny", LongType()),
        StructField("cool", LongType()),
        StructField("elite", StringType()),
        StructField("fans", LongType()),
        StructField("average_stars", DoubleType()),
    ]
)
