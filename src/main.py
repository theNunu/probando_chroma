import chromadb
from chromadb.config import Settings
from historias import reforma_info, evangelizacion_info, brujas_info

# client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
# persist_directory="db/"
# ))
# Initialize the Chroma client with persistent storage
client = chromadb.PersistentClient(path="db/")

collection = client.get_or_create_collection(name="HistoriasCristianas")
# source => fuente
collection.add(
    documents = [reforma_info, evangelizacion_info, brujas_info],
    metadatas = [{"source": "reforma protestante info"},
                 {"source": "america evangelio info"},
                 {'source':'brujas cazeria info'}],
    ids = ["id1", "id2", "id3"]
)


# heroes = []

