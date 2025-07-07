# Overview

Builds on https://github.com/minimaxir/mtg-embeddings which used gte-modernbert-base to generate embeddings based on magic card json data from MTGJSON. The mtg-embeddings project supported similarity search via cosine similarity of the embedding vectors to card-to-card similarity. A card name could be used to find the embedding vector for the card and then most similar cards to that card could be retreived. Similarity accuracy is limited because the model has no magic the gathering specific knowledge, just general language concepts. 

This project expands on mtg-embeddings by fine tuning gte-modernbert-base with magic the gathering specific relationships. In addition to card-to-card relationships, query-to-card relationships will also be modeled. This will allow natural language searches to be performed in addition to searches by card name.

# Magic The Gathering Domain Specific Embedding Model

Use a two stage approach to create a Magic The Gathering Domain specific embedding model. 

## Stage 1: Self-Supervised Domain Adaptation

Use Masked Language Modeling self-supervised learning on Magic The Gathering json card corpus. The model will learn Magic The Gathering domain specific vocabulary. Use validation loss / perplexity, odd one out (card-to-card symmetric relationships) and recall@10 (query-to-card asymetric relationships) to evaluate MLM finetuned model performance against base model. 

## Stage 2: Supervised Fine-Tuning

### Training Set

A triplet loss training set is used to fine tune the model relationships between magic the gathering cards and from queries to cards. These are types of symmetric and asymmetric relationships which gte-modernbert-base had in training data and therefore gte-modernbert-base is still a good base model to use.

`(anchor, positive, negative)`

#### Query-to-card Asymmetric Examples

Try to cover common strategies and player slang as well as finetune nuance of relationships.

##### Strategies
- Reanimate
- Ramp
- Bounce
- Flicker
- etc.

#### Player Slang
- Mana dorks
- Mana rock
- Tutors
- Board wipes
- Removal
- Cantrips
- Stax
- etc.

#### Triplet Examples
```
(synergy with Abuelo's Awakening, Omniscience, Wrath of God)
(cards that work well with Abuelo's Awakening, Omniscience, Counterspell)
(targets for Abuelo's Awakening, Omniscience, Crucible of Worlds)
(cards to reanimate omniscience, Abuelo's Awakening, Zombify)
(cards that reanimate enchantments, Abuelo's Awakening, Argivian Restoration)
```

Scryfall has a user curated tagging system that can be used to expedite training example creation. 

`https://api.scryfall.com/cards/search?q=oracletag:counterspell-free`

