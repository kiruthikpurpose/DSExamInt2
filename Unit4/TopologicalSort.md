**Topological Sort:**

Topological sort is a linear ordering of vertices in a *Directed Acyclic Graph (DAG)* where, for every directed edge \( u \to v \), vertex \( u \) appears before \( v \). This is useful for scheduling tasks with dependencies, like course prerequisites or job scheduling. 

The process involves:
1. Selecting vertices with *no incoming edges* (in-degree zero) and adding them to the ordering.
2. Removing these vertices and their outgoing edges, updating in-degrees of connected vertices until all are sorted.

Topological sort is possible only in acyclic graphs.