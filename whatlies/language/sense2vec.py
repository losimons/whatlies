from typing import Union

import spacy
from spacy.language import Language
import numpy as np
from typing import Union, List
from sklearn.metrics import pairwise_distances
from sense2vec import Sense2Vec, Sense2VecComponent


class Sense2VecLangauge:
    """
    This object is used to lazily fetch [Embedding][whatlies.embedding.Embedding]s or
    [EmbeddingSet][whatlies.embeddingset.EmbeddingSet]s from a sense2vec language
    backend. This object is meant for retreival, not plotting.

    Arguments:
        sense2vec_path: path to downloaded vectors

    **Usage**:

    ```python
    > lang = Sense2VecLanguage(sense2vec_path="/path/to/reddit_vectors-1.1.0")
    > lang['bank|NOUN']
    > lang['bank|VERB']
    ```

    Important:
        The reddit vectors are not given by this library.
        You can find the download link [here](https://github.com/explosion/sense2vec#pretrained-vectors).

    """

    def __init__(self, sense2vec_path):
        self.s2v = Sense2Vec().from_disk(sense2vec_path)

    def __getitem__(self, query):
        """
        Retreive a single embedding or a set of embeddings.

        Arguments:
            query: single string or list of strings

        **Usage**
        ```python
        > lang = SpacyLanguage("en_core_web_md")
        > lang['duck|NOUN']
        > lang[['duck|NOUN'], ['duck|VERB']]
        ```
        """
        if isinstance(query, str):
            vec = self.s2v[query]
            return Embedding(query, vec)
        return EmbeddingSet(*[self[tok] for tok in query])

    def embset_similar(self, query, n=10):
        """
        Retreive an [EmbeddingSet][whatlies.embeddingset.EmbeddingSet] that are the most simmilar to the passed query.

        Arguments:
            query: query to use
            n: the number of items you'd like to see returned

        Returns:
            An [EmbeddingSet][whatlies.embeddingset.EmbeddingSet] containing the similar embeddings.
        """
        return EmbeddingSet(
            *[self[tok] for tok, sim in self.s2v.most_similar(query, n=n)],
            name=f"Embset[s2v similar_{n}:{query}]",
        )

    def score_similar(self, query, n=10):
        """
        Retreive an EmbeddingSet that are the most simmilar to the passed query.

        Arguments:
            query: query to use
            n: the number of items you'd like to see returned

        Returns:
            An list of ([Embedding][whatlies.embedding.Embedding], score) tuples.
        """
        return [(self[tok], sim) for tok, sim in self.s2v.most_similar(query, n=n)]
