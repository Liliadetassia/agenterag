from langchain_comunity.document_loaders import DirectoryLoader

PASTA_BASE = "base"

def carregar_documentos():
    loader = DirectoryLoader(PASTA_BASE, glob="**/*.pdf")
    documentos = loader.load()
    return documentos