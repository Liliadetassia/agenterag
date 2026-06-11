from langchain.text_splitter import RecursiveCharacterTextSplitter

def dividir_chunks(documentos):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documentos)

    return chunks