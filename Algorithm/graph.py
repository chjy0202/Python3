graph = dict()

graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

def bfs(graph, start_node):
	visited = []
	need_visit = []

	need_visit.append(start_node)

	while need_visit:
		node = need_visit.pop(0) 
		# pop(0)이라고 하면 need_visit queue에서 앞에부터 빼온다
		if node not in visited:
			visited.append(node)
			need_visit.extend(graph[node]) # 인접노드들을 넣어주는 과정

	return visited

print(bfs(graph,'A'))

# 시간복잡도 O(V노드수 + E간선수)

