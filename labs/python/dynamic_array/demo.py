"""Demo: Observe dynamic array append costs and amortization.

Run this to see:
- Cost of each append (time / reallocation count)
- Amortized O(1) behavior
- Why doubling strategy works
"""

import time
from implementation import DynamicArray


def demo_append_costs():
    """Track the cost of each append: O(1) vs O(n) reallocations."""
    print("=" * 60)
    print("Demo 1: Append Costs and Reallocations")
    print("=" * 60)
    
    arr = DynamicArray(initial_capacity=1)
    realloc_indices = []  # Indices where reallocations happened
    
    n = 32  # Append 32 elements
    for i in range(n):
        old_capacity = arr.capacity
        arr.append(i)
        if arr.capacity > old_capacity:
            realloc_indices.append(i)
            print(f"  Reallocation at index {i}: capacity {old_capacity} -> {arr.capacity}")
    
    print(f"\nAfter appending {n} elements:")
    print(f"  Final size: {arr.size}")
    print(f"  Final capacity: {arr.capacity}")
    print(f"  Reallocations: {len(realloc_indices)} at indices {realloc_indices}")
    print(f"  Total work: O(n) = O({sum(arr.capacity // (2**i) for i in range(len(realloc_indices) + 1))})")
    print(f"  Amortized per append: O({n} / {n}) = O(1)")
    print()


def demo_memory_layout():
    """Show memory layout: size vs capacity."""
    print("=" * 60)
    print("Demo 2: Size vs Capacity")
    print("=" * 60)
    
    arr = DynamicArray(initial_capacity=2)
    print(f"Initial: {arr}")
    
    arr.append(10)
    print(f"After append(10): {arr}")
    
    arr.append(20)
    print(f"After append(20): {arr}")
    
    arr.append(30)  # Triggers reallocation
    print(f"After append(30): {arr}")
    
    arr.append(40)
    print(f"After append(40): {arr}")
    
    print(f"\nNote: capacity is 4, but we've only filled 4 slots.")
    print(f"The buffer has room for growth without reallocation.\n")


def demo_pop():
    """Show pop operation."""
    print("=" * 60)
    print("Demo 3: Pop Operation")
    print("=" * 60)
    
    arr = DynamicArray()
    for i in range(5):
        arr.append(i * 10)
    
    print(f"Before pop: {arr}")
    
    val = arr.pop()
    print(f"Popped: {val}")
    print(f"After pop: {arr}")
    print(f"Note: capacity stays {arr.capacity} (pop doesn't shrink capacity)\n")


def demo_random_access():
    """Show O(1) random access."""
    print("=" * 60)
    print("Demo 4: O(1) Random Access")
    print("=" * 60)
    
    arr = DynamicArray()
    for i in range(10):
        arr.append(i * i)  # 0, 1, 4, 9, 16, ..., 81
    
    print(f"Array: {arr}")
    print(f"\nRandom access (instant, no iteration):")
    for idx in [0, 3, 5, 9]:
        print(f"  arr[{idx}] = {arr[idx]}")
    print()


def demo_timing():
    """Show that append is fast (even with reallocations)."""
    print("=" * 60)
    print("Demo 5: Timing Append (1000 elements)")
    print("=" * 60)
    
    arr = DynamicArray()
    
    start = time.time()
    for i in range(1000):
        arr.append(i)
    elapsed = time.time() - start
    
    print(f"Appended 1000 elements in {elapsed*1000:.2f} ms")
    print(f"Final size: {arr.size}, capacity: {arr.capacity}")
    print(f"Average per append: {elapsed*1000000/1000:.2f} microseconds")
    print()


if __name__ == "__main__":
    demo_append_costs()
    demo_memory_layout()
    demo_pop()
    demo_random_access()
    demo_timing()
    
    print("=" * 60)
    print("Demo complete. Run pytest test_dynamic_array.py for unit tests.")
    print("=" * 60)
