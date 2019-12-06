from __future__ import annotations

input_file = open('input.txt', 'r')
orbits_raw = [s.split(")") for s in input_file.read().splitlines()]

santa: TreeNode
you: TreeNode

class TreeNode:
    parent: TreeNode
    left: TreeNode
    right: TreeNode
    name: str
    indirect_orbits_count: int    

    def __init__(self, name, indirect_orbits_count):
        self.name = name
        self.indirect_orbits_count = indirect_orbits_count


def populate_node(name, indirect_orbits_count, parent):    
    children = [orbit[1] for orbit in list(filter(lambda x: x[0] == name, orbits_raw))]    
    node = TreeNode(name, indirect_orbits_count)
    node.left = None if len(children) < 1 else populate_node(children[0], indirect_orbits_count + 1, node)
    node.right = None if len(children) < 2 else populate_node(children[1], indirect_orbits_count + 1, node)
    node.parent = parent

    if name == "SAN":
        global santa
        santa = node
    if name == "YOU":
        global you 
        you = node

    return node

def count_orbits(node: TreeNode):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.indirect_orbits_count
    return count_orbits(node.left) + count_orbits(node.right) + node.indirect_orbits_count

root = populate_node("COM", 0, None)

# Part 1
print (count_orbits(root))

# Part 2
nodes_from_santa_to_com = { "SAN": 0 }
nodes_from_you_to_com = { "YOU": 0 }
node = santa
distance_from_santa = 0

while node.name != "COM":
    nodes_from_santa_to_com[node.name] = distance_from_santa
    node = node.parent
    distance_from_santa += 1

node = you
distance_from_you = 0
while node.name != "COM":
    nodes_from_you_to_com[node.name] = distance_from_you
    node_distance_from_santa = nodes_from_santa_to_com.get(node.name)
    if node_distance_from_santa != None:
        print (node_distance_from_santa + distance_from_you - 2)
        break
    node = node.parent
    distance_from_you += 1