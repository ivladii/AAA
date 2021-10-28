from __future__ import annotations

from itertools import chain
from collections import Counter
from typing import Iterable, List, Union
import math
from operator import mul


class CountVectorizer:

    def __init__(self):
        self.feature_names = []

    def fit_transform(self, raw_documents: Iterable[str]) -> List[List[int]]:
        """
        Составляет список терминов в необработанных документах
        и реобразует документы в терм-документную матрицу
        """
        return self.fit(raw_documents).transform(raw_documents)

    def fit(self, raw_documents: Iterable[str]) -> CountVectorizer:
        """Составляет список терминов в необработанных документах"""

        if not isinstance(raw_documents, list):
            raise ValueError('Iterable over raw text documents expected, string object received')

        words = chain.from_iterable(self.format_and_split_document(doc) for doc in raw_documents)
        for word in words:
            if word not in self.feature_names:
                self.feature_names.append(word)

        return self

    def transform(self, raw_documents: Iterable[str]) -> List[List[int]]:
        """Преобразует документы в терм-документную матрицу"""
        if not isinstance(raw_documents, list):
            raise ValueError('Iterable over raw text documents expected, string object received')

        if not self.feature_names:
            raise Exception('Fit method not initiated')

        count_matrix = []
        words_position = {word: pos for pos, word in enumerate(self.feature_names)}

        for doc in raw_documents:
            row = [0] * len(self.feature_names)
            counter = Counter(self.format_and_split_document(doc))
            for word, count in counter.items():
                row[words_position[word]] = count
            count_matrix.append(row)

        return count_matrix

    def get_feature_names(self) -> list:
        return self.feature_names

    def format_and_split_document(self, raw_document: str) -> list:
        return raw_document.lower().strip(' \t\r\n').split()


class TfidfTransformer:

    def __init__(self):
        pass

    def fit_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """
        tfidf-трансформация терм-матрицы
        """
        return self.fit().transform(count_matrix)

    def fit(self, *args, **kwargs):
        return self

    def transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """
        tfidf-трансформация терм-матрицы
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_martix = self.idf_transform(count_matrix)
        tfidf_matrix = [list(map(mul, tf_row, idf_martix)) for tf_row in tf_matrix]
        return tfidf_matrix

    def tf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Делает tf-трансформацию терм-матрицы
        """

        return [
            [word_qty / sum(row) for word_qty in row]
            for row in count_matrix
        ]

    def idf_transform(self, count_matrix: List[List[int]]) -> List[float]:
        """
        Делает idf-трансформацию терм-матрицы
        """

        def filter_zero(values: Iterable[int]) -> list:
            return [val for val in values if val != 0]

        def calc_idf(docs_qty: int, docs_qty_with_perm: int) -> float:
            return math.log((docs_qty + 1) / (docs_qty_with_perm + 1)) + 1

        term_occurrence = (
            len(filter_zero(term_qty_per_doc))
            for term_qty_per_doc in zip(*count_matrix)
        )

        idf_matrix = [
            calc_idf(len(count_matrix), docs_qty_with_perm)
            for docs_qty_with_perm in term_occurrence
        ]

        return idf_matrix


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, raw_documents: Iterable[str]) -> List[List[float]]:
        """
        Делает tf-idf трансформацию списка документов
        """

        count_matrix = super().fit_transform(raw_documents)
        return self.tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    tfids_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfids_vectorizer.fit_transform(corpus)

    print(tfidf_matrix)