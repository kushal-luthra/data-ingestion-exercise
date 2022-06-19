from pyspark import RDD, SparkContext, SparkConf
from pyspark.sql import SparkSession
from src.main.base import PySparkJobInterface

class Article:
    article_id: int
    article_text: str

    def parse(self, line):
        tokens = line.split("|")
        self.article_id = int(tokens[0])
        self.article_text = tokens[1]
        return self

    def __repr__(self):
        return f"{self.article_id}|{self.article_text}"


class PySparkJob(PySparkJobInterface):

    def init_spark_context(self) -> SparkContext:
        # TODO: put your code here
        name = 'Spell Checker Job'
        sparkconf =  SparkConf()
        sparkconf.setAppName(name)
        sparkconf.setMaster('local')

        spark =  SparkSession.builder \
                .config(conf=sparkconf) \
                .getOrCreate()

        return spark.sparkContext

    def read_file(self, input_path: str) -> RDD:
        # TODO: put your code here
        # sc = self.init_spark_context()
        input_path = 'file:///'+input_path

        return self.sc\
            .textFile(input_path) \
            .map( lambda x: x.split("|") )

    def keep_nonempty_articles(self, articles: RDD) -> RDD:
        # TODO: put your code here
        return articles.filter(lambda x: len(x[1])>0)

    def find_good_articles(self, articles: RDD, dictionary: dict) -> RDD:
        # TODO: put your code here

        # gives us format : (article_id, word). eg - (1, 'old'), (1, 'new'), .... so on.
        count_articles = articles.flatMapValues(lambda x: x.split(" "))
        new_count_article =  count_articles.map(lambda x: (x[1], (x[0], x[1])))
        # new_count_article.take(5)

        # now read dictionary into RDD
        dict_rdd = self.sc.parallelize(dictionary.items())
        # dict_rdd.take(5)

        # join with dict and set mispelled flag as True or False
        # joined_rdd = count_articles.join(dict_rdd)
        joined_rdd = new_count_article.leftOuterJoin(dict_rdd)
        joined_rdd.take(5)

        # evaluate flag
        evaluate_rdd = joined_rdd.map(lambda x: ( x[1][0][0], x[1][0][1].strip()==x[1][1].strip() ) )

        evaluate_rdd.filter(lambda x: x[1]).take(5)

        return evaluate_rdd

    def find_bad_articles(self, articles: RDD, dictionary: dict) -> RDD:
        # TODO: put your code here
        pass

    def save_as(self, rdd: RDD, output_path: str) -> None:
        # TODO: put your code here
        pass
