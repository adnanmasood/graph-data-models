from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .blank_nodes import blank_node_issue
from .datalog_runaway import runaway_guard
from .eav_join_complexity import join_complexity
from .lpg_supernodes import supernode_metrics
from .open_world_vs_shacl import open_world_vs_shacl
from .qualifier_loss import qualifier_loss
from .reification_verbosity import reification_counts
from .vector_not_facts import vector_limit


def demo() -> str:
    checks = [open_world_vs_shacl(), blank_node_issue(), reification_counts(), supernode_metrics(), qualifier_loss(), runaway_guard(), join_complexity(), vector_limit()]
    rows = [[f"lab-{index + 1}", str(check)] for index, check in enumerate(checks)]
    return simple_table(["gotcha lab", "observation"], rows)
