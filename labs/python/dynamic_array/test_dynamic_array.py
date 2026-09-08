"""Unit tests for DynamicArray.

Run with: pytest test_dynamic_array.py -v
"""

import pytest
from implementation import DynamicArray


class TestDynamicArrayInit:
    """Test initialization."""
    
    def test_init_default(self):
        """Test default initialization."""
        arr = DynamicArray()
        assert arr.size == 0
        assert arr.capacity >= 1
        assert arr.is_empty()
    
    def test_init_with_capacity(self):
        """Test initialization with specific capacity."""
        arr = DynamicArray(initial_capacity=10)
        assert arr.size == 0
        assert arr.capacity == 10
    
    def test_len(self):
        """Test __len__ returns size."""
        arr = DynamicArray()
        assert len(arr) == 0


class TestAppendAndPop:
    """Test append and pop operations."""
    
    def test_append_single(self):
        """Test appending a single element."""
        arr = DynamicArray()
        arr.append(42)
        assert arr.size == 1
        assert arr[0] == 42
    
    def test_append_multiple(self):
        """Test appending multiple elements."""
        arr = DynamicArray()
        for i in range(5):
            arr.append(i)
        assert arr.size == 5
        for i in range(5):
            assert arr[i] == i
    
    def test_append_triggers_reallocation(self):
        """Test that append triggers reallocation when full."""
        arr = DynamicArray(initial_capacity=2)
        arr.append(1)
        arr.append(2)
        old_capacity = arr.capacity
        arr.append(3)  # Should reallocate
        assert arr.capacity > old_capacity
        assert arr.size == 3
    
    def test_pop_single(self):
        """Test popping from a single-element array."""
        arr = DynamicArray()
        arr.append(10)
        val = arr.pop()
        assert val == 10
        assert arr.size == 0
    
    def test_pop_multiple(self):
        """Test popping multiple times."""
        arr = DynamicArray()
        for i in range(5):
            arr.append(i)
        
        assert arr.pop() == 4
        assert arr.pop() == 3
        assert arr.size == 3
    
    def test_pop_empty_raises(self):
        """Test that pop on empty array raises IndexError."""
        arr = DynamicArray()
        with pytest.raises(IndexError):
            arr.pop()


class TestGetSet:
    """Test __getitem__ and __setitem__."""
    
    def test_getitem(self):
        """Test getting elements by index."""
        arr = DynamicArray()
        for i in range(5):
            arr.append(i * 10)
        
        assert arr[0] == 0
        assert arr[2] == 20
        assert arr[4] == 40
    
    def test_getitem_out_of_bounds(self):
        """Test that getitem raises on out-of-bounds index."""
        arr = DynamicArray()
        arr.append(1)
        
        with pytest.raises(IndexError):
            _ = arr[1]  # size is 1, so [1] is out of bounds
        
        with pytest.raises(IndexError):
            _ = arr[-1]  # negative indices not supported
    
    def test_setitem(self):
        """Test setting elements by index."""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        
        arr[0] = 100
        arr[1] = 200
        
        assert arr[0] == 100
        assert arr[1] == 200
    
    def test_setitem_out_of_bounds(self):
        """Test that setitem raises on out-of-bounds index."""
        arr = DynamicArray()
        arr.append(1)
        
        with pytest.raises(IndexError):
            arr[1] = 99  # size is 1, so [1] is out of bounds


class TestReserve:
    """Test reserve (manual reallocation)."""
    
    def test_reserve_grow(self):
        """Test reserving a larger capacity."""
        arr = DynamicArray(initial_capacity=2)
        arr.append(1)
        arr.append(2)
        
        arr.reserve(10)
        assert arr.capacity == 10
        assert arr.size == 2
        assert arr[0] == 1
        assert arr[1] == 2
    
    def test_reserve_shrink(self):
        """Test reserving a smaller capacity (truncates if needed)."""
        arr = DynamicArray(initial_capacity=10)
        arr.append(1)
        arr.append(2)
        arr.append(3)
        
        arr.reserve(2)  # Smaller than size
        assert arr.capacity == 2
        # Size may be truncated depending on implementation


class TestInvariants:
    """Test that invariants hold throughout operations."""
    
    def test_size_le_capacity(self):
        """Test that size <= capacity always."""
        arr = DynamicArray()
        for i in range(100):
            arr.append(i)
            assert arr.size <= arr.capacity
    
    def test_capacity_never_zero(self):
        """Test that capacity never drops to zero (if size > 0)."""
        arr = DynamicArray()
        arr.append(1)
        assert arr.capacity > 0
        arr.pop()
        # After pop, size is 0, capacity may be anything >= 0


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_append_none(self):
        """Test that we can store None as an element."""
        arr = DynamicArray()
        arr.append(None)
        assert arr[0] is None
    
    def test_append_mixed_types(self):
        """Test appending mixed types (Python allows this)."""
        arr = DynamicArray()
        arr.append(1)
        arr.append("hello")
        arr.append(3.14)
        assert arr.size == 3
        assert arr[0] == 1
        assert arr[1] == "hello"
        assert arr[2] == 3.14
    
    def test_large_append_sequence(self):
        """Test appending a large number of elements."""
        arr = DynamicArray()
        n = 10000
        for i in range(n):
            arr.append(i)
        
        assert arr.size == n
        assert arr[0] == 0
        assert arr[n - 1] == n - 1
