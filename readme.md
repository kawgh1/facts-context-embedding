### This is a project based on a course by Stephen Grider at [here](https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass)

- Please see the file `requirements.txt` before running locally

### Adding Context with Embedding Techniques

- In this project we will explore using an existing document -- it could be a .txt file, a PDF, a CSV file, a financial report, anything -- and enabling ChatGPT to draw data from this file to return information about the file to the user.
- This example is a short 10 lines of random facts in a .txt file, but the same principle would apply to any business report, a book in a PDF form, etc.
- ![Overview](https://raw.githubusercontent.com/kawgh1/facts-context-embedding/main/images/Context%20with%20Embedding%20Techniques.png)

### LangChain File Loader Classes

- LangChain provides Classes to help load data from different types of files. These Classes are called 'Loaders'.
- ![Loaders]()

- Additionally, LangChain also has Classes called 'Loaders' that are designed for specific Cloud Storage options like AWS S3 or Azure Blob, etc.
- These Cloud Loader classes like `S3FileLoader` for AWS can read many kinds of files, not just one. So this is important to remember.
  ![CloudLoaders]()

- Additionally, some `LangChain` Loader Classes, such as the `PyPDFLoader` require additional packages to be installed for them to work correctly (i.e., to read the files correctly)

![additional-packages-required]()
