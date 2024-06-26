from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

# emb = embeddings.embed_query()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

# 1. when you call Chroma.from_documents() and pass in a list of 
# documents, you are telling Chroma thru OpenAI API that you 
# want to immediately calculate embeddings for all the documents
# 2. it will then create a SQLite db inside the "emb" directory
# 3. inconsitent between embedding vs. embeddings parameters
db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

results = db.similarity_search_with_score(
    "What is an interesting fact about the English language?",
    k=1 # number of result embedding chunks to return
    )

for result in results:
    print("\n")
    print("Similarity Score: " + str(result[1])) # similarity score
    print(result[0].page_content) # content