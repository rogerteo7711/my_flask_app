class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, item):
        """Add an item to the buffer."""
        self.buffer.append(item)

    def get_all(self):
        """Retrieve all items from the buffer."""
        return self.buffer

    def clear(self):
        """Clear the buffer."""
        self.buffer = []

    def get_by_type(self, data_type):
        """Retrieve items of a specific type from the buffer."""
        return [item for item in self.buffer if isinstance(item, data_type)]