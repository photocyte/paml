"""
The ObjectNode class defines the functions corresponding to the dynamically generated labop class ObjectNode
"""

from typing import Dict, List

from . import inner
from .activity_node import ActivityNode
from .literal_specification import LiteralSpecification


class ObjectNode(inner.ObjectNode, ActivityNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dot_attrs(
        self,
        incoming_edges: Dict["InputPin", List["ActivityEdge"]] = None,
    ):
        raise ValueError(f"Do not know what GraphViz label to use for {self}")

    def enabled(
        self,
        edge_values: Dict["ActivityEdge", List[LiteralSpecification]],
        engine: "ExecutionEngine",
    ):
        """Check whether all incoming edges have values defined by a token in tokens and that all value pin values are
        defined.

        Parameters
        ----------
        self: node to be executed
        edge_values: current list of pending edge flows

        Returns
        -------
        bool if self is enabled
        """
        return all([len(edge_values[e]) > 0 for e in edge_values]) or engine.permissive
