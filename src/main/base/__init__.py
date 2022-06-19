import abc

from pyspark import RDD, SparkContext


class PySparkJobInterface(abc.ABC):

    def __init__(self):
        self.sc = self.init_spark_context()

    @abc.abstractmethod
    def init_spark_context(self) -> SparkContext:
        """Create spark context"""
        raise NotImplementedError

    @abc.abstractmethod
    def read_file(self, input_path: str) -> RDD:
        raise NotImplementedError

    @abc.abstractmethod
    def keep_nonempty_articles(self, articles: RDD) -> RDD:
        raise NotImplementedError

    @abc.abstractmethod
    def find_good_articles(self, articles: RDD, dictionary: dict) -> RDD:
        raise NotImplementedError

    @abc.abstractmethod
    def find_bad_articles(self, vaccines: RDD, dictionary: dict) -> RDD:
        raise NotImplementedError

    @abc.abstractmethod
    def save_as(self, rdd: RDD, output_path: str) -> None:
        raise NotImplementedError

    @staticmethod
    def load_dictionary(dict_path) -> dict:
        with open(dict_path) as r:
            return dict( [tuple(line.replace("\n", "").lower().split("|") ) for line in r])

    def stop(self) -> None:
        self.sc.stop()
