import json
import networkx as nx
from pathlib import Path


class KnowledgeGraphLoader:

    def __init__(self, file_path="knowledge_graph.json"):
        self.file_path = Path(__file__).parent / file_path
        self.graph = nx.DiGraph()
        self.business_terms = {}

    def load(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        # Load entities as nodes
        for entity, details in data["entities"].items():
            self.graph.add_node(
                entity,
                table=details.get("table"),
                attributes=details.get("attributes", []),
                metrics=details.get("metrics", [])
            )

        # Load relationships as edges
        for relation in data["relationships"]:
            self.graph.add_edge(
                relation["from"],
                relation["to"],
                relation=relation["relation"]
            )

        # Load business definitions
        self.business_terms = data.get("business_terms", {})

        return self.graph

    def get_business_context(self, term):
        term = term.lower()

        for key, value in self.business_terms.items():
            if key.lower() in term:
                return {
                    "business_meaning": value
                }

        return {
            "business_meaning": "No specific business definition found"
        }


if __name__ == "__main__":

    kg = KnowledgeGraphLoader()

    graph = kg.load()

    print("Knowledge Graph Loaded")
    print("----------------------")

    print("Entities:")
    print(list(graph.nodes))

    print("\nRelationships:")
    print(list(graph.edges(data=True)))

    print("\nBusiness Context:")
    print(
        kg.get_business_context(
            "Who are my best customers?"
        )
    )