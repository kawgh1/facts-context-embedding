### This is a project based on a course by Stephen Grider at [here](https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass)

- Please see the file `requirements.txt` before running locally

### Adding Context with Embedding Techniques

- In this project we will explore using an existing document -- it could be a .txt file, a PDF, a CSV file, a financial report, anything -- and enabling ChatGPT to draw data from this file to return information about the file to the user.
- This example is a short 10 lines of random facts in a .txt file, but the same principle would apply to any business report, a book in a PDF form, etc.
- ![Overview](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Context%20with%20Embedding%20Techniques.png)

### LangChain File Loader Classes

- LangChain provides Classes to help load data from different types of files. These Classes are called 'Loaders'.
- ![Loaders](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/LangChain%20File%20Loader%20Classes.png)

- Additionally, LangChain also has Classes called 'Loaders' that are designed for specific Cloud Storage options like AWS S3 or Azure Blob, etc.

  - These Cloud Loader classes like `S3FileLoader` for AWS can read many kinds of files (.json, .md, .txt, etc.), not just one. So this is important to remember.

    - [CloudLoaders](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Cloud%20Storage%20Loaders.png)

  - Additionally, some `LangChain` Loader Classes, such as the `PyPDFLoader` require additional packages to be installed for them to work correctly (i.e., to read the files correctly)

    - [additional-packages-required](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/some%20loader%20classes%20require%20additional%20packages.png)

### LangChain TextLoader Class

- TextLoader is a LangChain class that read `.txt` files
  - ![textloader](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Text%20Loader%20.png)

### This Project

- So we know we want to use `facts.txt` and allow ChatGpt to read it and provide informational responses to the user about the file.

  - Considerations:

    - Including the entire `facts.txt` file in every user query is expensive, both in compute and money $$.
    - Takes longer to run.
    - It also makes it more difficult for the LLM to find relevant facts about the document, if it receives it new every query.

  - Better Option:
    - Put only the top 1-3 **relevant** facts into the request prompt.
    - Upside: shorter prompt! Less expensive, faster, more focused.
    - Downside: need to find the most relevant facts to each prompt before sending the request!

### Introducing Embeddings

- Alternative - Semantic Search

  - Understand the goal of the user's search
  - implement using **embeddings**

- Embeddings

  - An **embedding** is a list of numbers between -1 and 1 that represent a score of how much a piece of text is talking about some particular quality.
  - These **embeddings** only rate **2 qualities**, but production-level embeddings often have **700-1500+ dimensions** or qualities that they score on
  - ![embeddings-example](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Embeddings%20Example.png)

- ### Squared L2 and Cosine Similarity

  - We take those lists of numbers and turn them into multi-dimensional **vectors**.
    - We can then make comparisons between those vectors to estimate how similar or dissimilar two sentences are.
      <br>
      <br>
  - ![squared-L2-and-cosine-similarity](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Cosine%20Sim%20and%20L2.png)

- ### Vector Stores

  - We create embeddings for all 10 "facts" in our `facts.txt` file and store them as **vectors** in our **vector store**.
  - Then, when the user asks a question, we vectorize their question and compare it to the vectors in our **vector store** and grab the most similar (vectorized) facts.
    <br>
    <br>
  - ![vector-store-1](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Vector%20Store%201.png)
    <br>
    <br>
  - ![vector-store-2](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Vector%20Store%202.png)

- ### LangChain Class CharacterTextSplitter
  - used to take strings and split them --> also called **chunking**
  - Multiple variations of Text Splitters:
    - **SentenceTransformer**
      - _all-mpnet-base-v2_
        - runs on local machine, free, but takes local compute power
        - 768 dimensions
    - **OpenAI Embeddings**
      - runs on the OpenAI API, not free, but much faster
      - 1536 dimensions
      - etc.
      - etc.
    - **Note**: Different algorithms are not really comparable or compatible because how they vectorize and determine their embedding scores is totally different, even if they have the same number of dimensions.

```
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

...
...
...


embeddings = OpenAIEmbeddings()

emb = embeddings.embed_query()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

for doc in docs:
    print(doc.page_content)
    print("\n")

```

- **Output**:

```
1. "Dreamt" is the only English word that ends with the letters "mt."
2. An ostrich's eye is bigger than its brain.
3. Honey is the only natural food that is made without destroying any kind of life.


4. A snail can sleep for three years.
5. The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'
6. The elephant is the only mammal that can't jump.


7. The letter 'Q' is the only letter not appearing in any U.S. state name.
8. The heart of a shrimp is located in its head.
9. Australia is the only continent covered by a single country.


10. The Great Wall of China is approximately 13,171 miles long.
11. Bananas are berries, but strawberries aren't.
12. The Sphinx of Giza has the body of a lion and the head of a human.


13. The first computer bug was an actual bug trapped in a computer.
14. Neil Armstrong was the first man to walk on the moon.


15. The Eiffel Tower in Paris leans slightly in the sun due to thermal expansion.
16. Queen Elizabeth II is the longest-reigning current monarch.

...
...
...

```

# ChromaDB for Embeddings

- We can use ChromaDB to generate and manage our embeddings

  - `pip3 install chromadb`
  - `from langchain.vectorstores.chroma import Chroma`
  - LangChain allows us to do this through OpenAI API.

    - It is not free! But for our purposes may cost a few cents.
    - ```

      1. when you call Chroma.from_documents() and pass in a list of
         documents, you are telling Chroma thru OpenAI API that you
         want to immediately calculate embeddings for all the documents
      2. it will then create a SQLite db inside the "emb" directory
      3. inconsitent between embedding vs. embeddings parameters

      db = Chroma.from_documents(
      docs,
      embedding=embeddings,
      persist_directory="emb"
      )

      results = db.similarity_search_with_score(
      "What is an interesting fact about the English language?",
      k=1 # number of result embedding chunks to return
      )
      ```
