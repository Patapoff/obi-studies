queue.put(0)
visited[0 = true
distance[0] = 0

while not queue.vazia:
    u = fila.get()
    for v in vizinhos[u]:
        if visited[v] == false:
            visited[v] = true
            distance[v] = distance[u]+1
            fila.put(V)