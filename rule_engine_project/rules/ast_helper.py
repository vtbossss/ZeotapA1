class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        """Convert the Node to a dictionary representation."""
        if self.node_type == 'operator':
            return {
                'node_type': self.node_type,
                'left': self.left.to_dict() if self.left else None,
                'right': self.right.to_dict() if self.right else None,
                'value': self.value,
            }
        elif self.node_type == 'operand':
            return {
                'node_type': self.node_type,
                'value': self.value,
            }
        return {}
