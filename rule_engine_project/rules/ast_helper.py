class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        """
        Initialize a Node instance.

        Parameters:
        - node_type: Type of the node ('operator' or 'operand').
        - left: Left child node (default is None).
        - right: Right child node (default is None).
        - value: Value of the node (used for operands and operators).
        """
        self.node_type = node_type  # Type of the node ('operator' or 'operand')
        self.left = left            # Left child node
        self.right = right          # Right child node
        self.value = value          # Value of the node

    def to_dict(self):
        """
        Convert the Node to a dictionary representation.

        Returns:
        A dictionary representation of the Node suitable for JSON serialization.
        """
        if self.node_type == 'operator':
            return {
                'node_type': self.node_type,                  # Type of the node
                'left': self.left.to_dict() if self.left else None,  # Convert left child to dict if it exists
                'right': self.right.to_dict() if self.right else None,  # Convert right child to dict if it exists
                'value': self.value,                          # Operator value
            }
        elif self.node_type == 'operand':
            return {
                'node_type': self.node_type,                  # Type of the node
                'value': self.value,                          # Operand value
            }
        
        return {}  # Return an empty dictionary for unsupported node types
