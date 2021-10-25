from __future__ import annotations

from itertools import chain
from collections import Counter
from typing import Iterable


class CountVectorizer:

    def __init__(self):
        self.feature_names = []

    def fit_transform(self, raw_documents: Iterable[str]) -> list[list[int]]:
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

    def transform(self, raw_documents: Iterable[str]) -> list[list[int]]:
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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)