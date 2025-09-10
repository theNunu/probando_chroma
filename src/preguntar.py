# otro archivo
from main import collection

results = collection.query(
    query_texts=["que paso en 1535?"],
    n_results=10
)

results
print(results)