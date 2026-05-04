import chromadb
client=chromadb.Client()
collection=client.get_or_create_collection(name='logs')

def save_log_embedding(log_text:str):
    collection.add(documents=[log_text],ids=[str(abs(hash(log_text)))])
