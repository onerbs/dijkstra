from unittest import TestCase
from dijkstra import dijkstra
from graph import Graph


class TestDijkstra(TestCase):
	def test_graph_1(self):
		gg = Graph([
			('A', 'B', 3),
			('A', 'C', 4),
			('A', 'D', 7),
			('B', 'C', 1),
			('B', 'F', 5),
			('C', 'D', 2),
			('C', 'F', 6),
			('D', 'E', 3),
			('D', 'G', 6),
			('E', 'F', 1),
			('E', 'G', 3),
			('E', 'H', 4),
			('F', 'H', 8),
		])
		r"""
		. A---D---G
		. |\ / \ /|
		. | C   E |
		. |/ \ / \|
		. B---F---H
		"""

		self.assertEqual(
			['A', 'C', 'D', 'E', 'H'],
			dijkstra(gg, 'A', 'H'),
		)

		self.assertEqual(
			['B', 'C', 'D', 'G'],
			dijkstra(gg, 'B', 'G'),
		)

	def test_graph_2(self):
		gg = Graph([
			('A', 'B', 14),
			('A', 'G', 10),
			('A', 'H', 17),
			('B', 'C', 9),
			('B', 'F', 10),
			('B', 'G', 3),
			('C', 'F', 2),
			('F', 'I', 7),
			('G', 'H', 6),
			('G', 'I', 4),
			('H', 'I', 1),
		])
		r"""
		.   B---G
		.  /|\ /|\
		. C | A | \
		.  \|  \| |
		.   F   H |
		.    \   \|
		.     `---I
		"""

		self.assertEqual(
			['C', 'F', 'I', 'H'],
			dijkstra(gg, 'C', 'H')
		)

		self.assertEqual(
			['A', 'G', 'I', 'F'],
			dijkstra(gg, 'A', 'F')
		)

	def test_graph_3(self):
		# https://es.wikipedia.org/wiki/Anexo:Ejemplo_de_Algoritmo_de_Dijkstra
		gg = Graph([
			('A', 'B', 16),
			('A', 'C', 10),
			('A', 'D', 5),
			('B', 'C', 2),
			('B', 'F', 4),
			('B', 'G', 6),
			('C', 'D', 4),
			('C', 'E', 10),
			('C', 'F', 12),
			('D', 'E', 15),
			('E', 'F', 3),
			('E', 'Z', 5),
			('F', 'G', 8),
		])
		r"""
		.   B---,---G
		.  / \   \ / \
		. A---C---F---Z
		.  \ / \ /   /
		.   D---E---
		"""

		self.assertEqual(
			['A', 'D', 'C', 'B', 'F', 'E', 'Z'],
			dijkstra(gg, 'A', 'Z')
		)

	def test_graph_4(self):
		gg = Graph([
			('A', 'B', 5),
			('A', 'C', 2),
			('B', 'D', 7),
			('C', 'D', 1),
		])
		gg.plug('Z')
		r"""
		. Z  B
		.   / \
		.  A   D
		.   \ /
		.    C
		"""

		self.assertEqual(
			['Z'], dijkstra(gg, 'Z', 'A')
		)
