from knowledge_graph.kg_loader import KnowledgeGraphLoader


kg_loader = KnowledgeGraphLoader()
kg_loader.load()


def search_business_context(user_query: str) -> dict:
    """
    Use this tool whenever the user asks business questions.

    This tool provides business definitions,
    relationships between entities,
    and analytical meaning from the knowledge graph.
    """

    print("====================")
    print("KG TOOL CALLED")
    print("Query:", user_query)
    print("====================")

    result = kg_loader.get_business_context(user_query)

    print("KG RESULT:")
    print(result)

    return result