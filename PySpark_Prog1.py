import json
import pyspark
from pyspark.sql import functions
from pyspark.sql.functions import explode
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, StringType

class Solution:
    def fun(self, n:int)->int:
        if n%2==0:
            return n*n
        else:
            return n*2
o = Solution()

print(o.fun(10))