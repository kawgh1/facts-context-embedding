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
