"""Dynamic Array (Growable Buffer) Implementation.

A dynamic array stores elements in a contiguous block of memory.
When full, it reallocates with a larger capacity (typically doubling).

Invariant:
  0 <= size <= capacity at all times
  If capacity > 0, data points to a valid buffer of capacity elements
  Elements [0, size) are initialized; [size, capacity) may be uninitialized
"""


class DynamicArray:
    """A growable array backed by a Python list (heap-allocated).
    
    Attributes:
        data: The underlying buffer (Python list).
        size: Number of elements currently stored.
        capacity: Total slots in the buffer.
    """
    
    def __init__(self, initial_capacity=1):
        """Initialize an empty dynamic array.
        
        Args:
            initial_capacity: Starting capacity (default 1).
        """
        self.size = 0
        self.capacity = initial_capacity
        self.data = [None] * initial_capacity
    
    def append(self, elem):
        """Add an element to the end of the array.
        
        If size == capacity, reallocate with doubled capacity.
        Amortized O(1).
        
        Args:
            elem: Element to add.
        """
        # Check if we need to reallocate
        if self.size == self.capacity:
            new_capacity = max(1, self.capacity * 2)
            new_data = [None] * new_capacity
            
            # Copy old elements to new buffer
            for i in range(self.size):
                new_data[i] = self.data[i]
            
            self.data = new_data
            self.capacity = new_capacity
        
        # Add element at the end
        self.data[self.size] = elem
        self.size += 1
    
    def pop(self):
        """Remove and return the last element.
        
        O(1).
        
        Returns:
            The last element.
            
        Raises:
            IndexError if the array is empty.
        """
        if self.size == 0:
            raise IndexError("pop from empty array")
        
        self.size -= 1
        return self.data[self.size]
    
    def __getitem__(self, index):
        """Get element at index.
        
        O(1).
        
        Args:
            index: Index (0-based).
            
        Returns:
            Element at index.
            
        Raises:
            IndexError if index out of range [0, size).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]
    
    def __setitem__(self, index, elem):
        """Set element at index.
        
        O(1).
        
        Args:
            index: Index (0-based).
            elem: New value.
            
        Raises:
            IndexError if index out of range [0, size).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = elem
    
    def __len__(self):
        """Return the current size.
        
        O(1).
        """
        return self.size
    
    def is_empty(self):
        """Check if array is empty.
        
        O(1).
        """
        return self.size == 0
    
    def reserve(self, new_capacity):
        """Reallocate to a specific capacity.
        
        If new_capacity > current capacity, allocate and copy.
        If new_capacity < current capacity, shrink (truncates if needed).
        
        Args:
            new_capacity: Desired capacity.
        """
        if new_capacity == self.capacity:
            return
        
        new_data = [None] * new_capacity
        
        # Copy elements (up to the minimum of old size and new capacity)
        copy_size = min(self.size, new_capacity)
        for i in range(copy_size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self.capacity = new_capacity
        self.size = min(self.size, new_capacity)
    
    def __repr__(self):
        """String representation for debugging."""
        elements = self.data[:self.size] if self.size > 0 else []
        return f"DynamicArray(size={self.size}, capacity={self.capacity}, elements={elements})"
