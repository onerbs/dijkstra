from copy import deepcopy


def dijkstra(graph, src, dest):
	gg = deepcopy(graph)
	gg.items[src].distance = 0
	unseen = list(gg.items.values())

	while unseen:
		try:
			actor = min(
				[vex for vex in unseen if vex.distance >= 0],
				key=lambda vex: vex.distance
			)
		except ValueError:
			break

		for mate in actor.nodes:
			weight = actor.distance + actor.nodes[mate]
			if mate.distance == -1 or weight < mate.distance:
				mate.distance = weight
				mate.parent = actor

		unseen.remove(actor)

	path, root = [], gg.items[dest]
	while root.parent is not None:
		path.append(root.vid)
		root = root.parent
	path.append(root.vid if path else src)
	return path[::-1]
