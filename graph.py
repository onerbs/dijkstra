class Vertex:
	def __init__(self, vid: str):
		self.vid = vid
		self.nodes = {}
		self.parent = None
		self.distance = -1

	def link(self, vertex, weight=0):
		self.nodes[vertex] = weight


class Graph:
	def __init__(self, data: list = None):
		self.items = {}
		for item in data:
			self.link(*item)

	def plug(self, vid) -> Vertex:
		if vid in self.items:
			return self.items[vid]
		vertex = Vertex(vid)
		self.items[vid] = vertex
		return vertex

	def link(self, va, vb, weight=0):
		self.plug(va).link(self.plug(vb), weight)
		self.plug(vb).link(self.plug(va), weight)
