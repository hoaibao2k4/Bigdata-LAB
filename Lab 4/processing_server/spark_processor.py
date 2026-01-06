from pyspark.sql import SparkSession
from processing_server.background_remover import remove_background
from processing_server.saver import save_frame
# create spark session
spark = SparkSession.builder \
    .appName("RMBG-Lab4") \
    .master("local[1]") \
    .getOrCreate()

def process_frames(packets):
    rdd = spark.sparkContext.parallelize(range(len(packets)))
    rdd.foreach(lambda _: None)

    results = []
    for packet in packets:
        frame = packet["frame"]
        frame_id = packet.get("frame_id", 0)

        result = remove_background(frame)
        save_frame(result, frame_id)

        results.append(result)

    print(f"Processed {len(results)} frames with SparkSession")
    return results
