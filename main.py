from ingestao.loader import carregar_documentos

docs = carregar_documentos()
print(f"Documentos carregados: {len(docs[0])}")