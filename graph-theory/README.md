---
tags: python, graph theory
---

# Graph Theory and Social Network Analysis with python

- [演算法筆記 - Graph](http://www.csie.ntnu.edu.tw/~u91029/Graph.html)
- [An Introduction to Graph Theory and Network Analysis (with Python codes)](https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/)
- [Graph: Intro(簡介)](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)
- [Tree(樹): Intro](http://alrightchiu.github.io/SecondRound/treeshu-introjian-jie.html)
- [譜分群 (Spectral Clustering) ─ 運用圖論 (Graph Theory) 進行分群](https://taweihuang.hpd.io/2017/07/06/intro-spectral-clustering/)

## Terminology

1. The vertices (點) `u` and `v` are called the `end vertices` of the edge (邊) `(u,v)`
2. If two edges have the same `end vertices` they are `Parallel`
3. An edge of the form `(v,v)` is a `loop`
4. A Graph is `simple` if it has **no parallel edges and loops**
5. A Graph is said to be `Empty` if it has **no edges**. Meaning `E` is empty
6. A Graph is a `Null Graph` if it has **no vertices**. Meaning `V` and `E` is empty
7. A Graph with only **1 Vertex** is a `Trivial` graph
8. **Edges** are `Adjacent` if they have a common vertex. **Vertices** are `Adjacent` if they have a common edge
9. The **degree** of the vertex `v`, written as `d(v)`, is the number of **edges** with `v` as an end vertex. By convention, we count a loop twice and parallel edges contribute separately
10. **Isolated Vertices** are vertices with degree 1. `d(1)` vertices are isolated
11. A Graph is **Complete** if its edge set contains every possible edge between ALL of the vertices
12. A `Walk` in a Graph `G = (V,E)` is a finite, alternating sequence of the form ViEiViEi consisting of vertices and edges of the graph G
13. A Walk is `Open` if the initial and final vertices are different. A Walk is `Closed` if the initial and final vertices are the same
14. A Walk is a `Trail` if ANY edge is traversed atmost once
15. A Trail is a `Path` if ANY vertex is traversed atmost once (Except for a closed walk)
16. A Closed Path is a `Circuit` -- Analogous to electrical circuits
17. Directed Graph (Digraph): 有向圖
18. 點和邊可加上權重
19. 點和邊可取名字、代號

## Graph 資料結構

#### 1. Edge List

#### 2. Adjacency Matrix

#### 3. Adjacency Lists


## Graph Theory

### Graph Traversal

### Example

[Airline dataset](https://bitbucket.org/dipolemoment/analyticsvidhya/src)


