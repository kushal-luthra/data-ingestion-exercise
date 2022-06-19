import sys
from main.job.pipeline import PySparkJob


dict_path = sys.argv[1]
article_path = sys.argv[2]
good_article_output = sys.argv[3]
bad_article_output = sys.argv[4]


def main():
    job = PySparkJob()

    # Load input data to DataFrame
    print("<<Reading>>")
    dictionary = job.load_dictionary(dict_path)
    articles = job.read_file(article_path)
    print(articles.count())

    # Keep non-empty articles
    print("<<Filtering Empty Articles>>")
    nonempty_articles = job.keep_nonempty_articles(articles).cache()
    print(nonempty_articles.count())

    # Extract good articles
    print("<<Good Articles>>")
    good_articles = job.find_good_articles(nonempty_articles, dictionary)
    print(good_articles.count())

    # Extract bad articles
    print("<<Bad Articles>>")
    bad_articles = job.find_bad_articles(nonempty_articles, dictionary)
    print(bad_articles.count())

    # Save articles to file
    print("<<Saving Articles>>")
    job.save_as(good_articles, good_article_output)
    job.save_as(bad_articles, bad_article_output)

    job.stop()


if __name__ == '__main__':
    main()
