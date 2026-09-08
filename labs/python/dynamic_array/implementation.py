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
        # TODO: Initialize self.size, self.capacity, and self.data
        # self.data should be a list of None with initial_capacity slots
        pass
    
    def append(self, elem):
        """Add an element to the end of the array.
        
        If size == capacity, reallocate with doubled capacity.
        Amortized O(1).
        
        Args:
            elem: Element to add.
        """
        # TODO: If self.size == self.capacity, double capacity and realloc
        # Then add elem at self.data[self.size]
        # Increment self.size
        pass
    
    def pop(self):
        """Remove and return the last element.
        
        O(1).
        
        Returns:
            The last element.
            
        Raises:
            IndexError if the array is empty.
        """
        # TODO: Check if size > 0, return self.data[size-1], decrement size
        pass
    
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
        # TODO: Check bounds, return self.data[index]
        pass
    
    def __setitem__(self, index, elem):
        """Set element at index.
        
        O(1).
        
        Args:
            index: Index (0-based).
            elem: New value.
            
        Raises:
            IndexError if index out of range [0, size).
        """
        # TODO: Check bounds, set self.data[index] = elem
        pass
    
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
        # TODO: If new_capacity != capacity, allocate new buffer,
        # copy elements, update self.data and self.capacity
        pass
    
    def __repr__(self):
        """String representation for debugging."""
        elements = self.data[:self.size] if self.size > 0 else []
        return f"DynamicArray(size={self.size}, capacity={self.capacity}, elements={elements})"
