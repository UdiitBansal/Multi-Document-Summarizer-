



from sentence_transformers import SentenceTransformer
import chromadb

print("Loading Embedding Model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model Loaded Successfully")

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="research_documents"
)


def generate_embeddings(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings


def store_chunks(chunks, embeddings):

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print(f"{len(chunks)} chunks stored")


def search_chunks(query, top_k=5):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]