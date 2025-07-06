# Overview

Builds on https://github.com/minimaxir/mtg-embeddings which used gte-modernbert-base to generate embeddings based on magic card json data from MTGJSON. The mtg-embeddings project supported similarity search via cosine similarity of the embedding vectors to card-to-card similarity. A card name could be used to find the embedding vector for the card and then most similar cards to that card could be retreived. Similarity accuracy is limited because the model has no magic the gathering specific knowledge, just general language concepts. 

This project expands on mtg-embeddings by fine tuning gte-modernbert-base with magic the gathering specific relationships. In addition to card-to-card relationships, query-to-card relationships will also be modeled. This will allow natural language searches to be performed in addition to searches by card name.

# Training Set

A triplet loss training set is used to fine tune the model relationships between magic the gathering cards and from queries to cards. These are types of symmetric and asymmetric relationships which gte-modernbert-base had in training data and therefore gte-modernbert-base is still a good base model to use.

`(anchor, positive, negative)`

Scryfall has a user curated tagging system that can be used to expedite training example creation. 

`https://api.scryfall.com/cards/search?q=oracletag:counterspell-free`

