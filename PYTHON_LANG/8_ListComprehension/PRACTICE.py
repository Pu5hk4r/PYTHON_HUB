
sc = SparkContext.getOrCreate()
arr = [[1,2],[3,4],[5,6]]
rdd = sc.parallelize(arr).flatMap(lambda x: x)
        .map(lambda x:0 if x % 2 == 0 else 1 )
print(rdd.collect())