import chromadb
from chromadb.config import Settings


client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
persist_directory="db/"
))

collection = client.create_collection(name="HistoriasCristianas")