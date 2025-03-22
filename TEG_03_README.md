# Introduction to Natural Language Processing (NLP) and Basic Retrival-Augumented Generation (RAG) Framework

## Overview
Today's class is an introduction to Natural Language Processing (NLP), a field of artificial intelligence that enables computers to understand, interpret, and generate human language. You will explore various methods and techniques used in NLP, including text tokenization, text embedding, and similarity measures.

Our objective will be to apply those learned techniques during building our own simple Retrieval-Augmented Generation (RAG) for processing and analyzing text data leveraging newly introduced [Langchain](https://python.langchain.com/) library.

## Objectives
### Your task for today is to build your own simple RAG using your own methods implementation or the Langchain library.

In order to do that you need to first go through provided Jupyter notebook and:
1. Understand fundamental concepts of NLP and text processing.
2. Learn different methods of text tokenization and chunking.
3. Experiment with text embeddings and similarity measures.
4. Explore advanced NLP techniques, including retrieval-augmented generation.

## Documentation
  - [NLTK Documentation](https://www.nltk.org/)
  - [Langchain Documentation](https://python.langchain.com/)
  - [RAG Research paper](https://arxiv.org/pdf/2312.10997)

## First steps
In order to run jupyter you need to create `.venv` and install all requirements.txt just like we did during all previous classes. 

## Topics covered during this class
### 1. Reading and Tokenizing Text
- Understanding the basics of text processing
- Different methods for splitting text into meaningful components
  - Word Splitting: Breaking text into individual words
  - Sentence Splitting: Identifying sentence boundaries
  - Fixed-Size Chunking: Splitting text into predefined word chunks
  - Semantic Splitting: Using sentence transformers for intelligent text segmentation

### 2. Text Embeddings: Comparing Models
Embeddings are vector representations of text that allow for comparisons and semantic understanding. 
We need them because computers can’t understand words — they understand numbers.
Embeddings let us capture meaning and **compute** similarity between pieces of text.

We will explore:
- TF-IDF Embeddings
- Bag of Words Embeddings
- Sentence Transformers Embeddings
- OpenAI-like Transformer Embeddings

### 3. Similarity Measures
To evaluate how similar two pieces of text are, we will use basic similarity metrics, such as:
- Cosine Similarity
- Euclidean Distance

### 4. Introduction to RAG (Retrieval-Augmented Generation)
- Understanding the principles of RAG
- Methods for reading and processing PDF data
- Enhancing and processing language using nltk
- Semantic splitting of text from PDFs using Sentence Transformers
- Leveraging Langchain library, designed for working with large textual data.