## Environment:
- Spark Version: 3.0.1
- Python Version: 3.7

## Read-Only Files:
- `src/app.py`
- `src/tests/test_pipeline.py`
- `src/main/__init__.py`
- `src/main/base/__init__.py`
- `src/main/job/__init__.py`
- `install.sh`
- `data/*`

## Requirements:
There are large number of web page texts(for example, think of common crawl corpus) which can be used for various purposes like input to language prediction model, web page classification, web ranking etc. But in this challenge, we write a job that acts as a pre-processing step and find good and bad articles based on spell misspellings found. Here each article will have a single line in the input file: `article_id|article_text`. Sample files are given in `data`.

Data model of an `article`:
```python
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
``` 

- `articles.txt`
  - it contains `article_id` and text content `article_text`
  
- `dict.txt`
  - This is misspelled dictionary which has been use to detect misspelled word
  - Format: `<misspelled word><COMMA><correct word>`
  
There are 6 methods to be implemented in the file `main/job/pipeline.py`:

- `init_spark_context(self) -> SparkContext`:
  - create a spark context with master `local` and name `Spell Checker Job`

- `read_file(self, input_path: str) -> RDD`:
  - read the data from given text from `input_path`
  - assume that there is no header line and file format is `|` delimited.
  - you could use method `parse(line: str)` in `model.Article`
  - return an `RDD` of `Article`

- `keep_nonempty_articles(self, articles: RDD) -> RDD`:
  - remove the articles with empty content text
  - return an `RDD` of `Article`

- `find_good_articles(self, articles: RDD, dictionary: dict) -> RDD`:
  - filter out the bad articles and return only the good articles
  - an article is bad if it has more then 30% misspelled words otherwise article is good.
  - `dictionary` is a map of misspelled word to correct word which has been provided
  - you should use the provided `dictionary` to calculate the percentage of misspelled words over the text content of `Article`
  - return an `RDD` of good `Article`
  
- `find_bad_articles(self, articles: RDD, dictionary: dict) -> RDD`:
  - similar logic to `find_good_articles` except only return the bad articles instead
  - return an `RDD` of bad `Article`
  
- `save_as(self, rdd: RDD, output_path: str) -> None`: 
  - persist the given `RDD` of `Article` to disk at the given `output_path`.
  - the expected output is a folder containing part files with format: `<article_id><PIPE><article_text>`
    
Your task is to complete the implementation of that job so that the unit tests pass while running the tests. You can use the give tests check your progress while solving problem.

## Commands
- run: 
```bash
source venv/bin/activate; cd src; python3 app.py ../data/dict.txt ../data/articles.txt ../good_articles ../bad_articles
```
- install: 
```bash
bash install.sh; source venv/bin/activate; pip3 install -r requirements.txt
```
- test: 
```bash
source venv/bin/activate; cd src; py.test -p no:warnings
```