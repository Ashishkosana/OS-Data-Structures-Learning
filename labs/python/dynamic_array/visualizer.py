"""Interactive visualization of DynamicArray operations.

Run this to see LIVE how the array grows, reallocates, and changes.
Step through each operation and watch memory/size/capacity change in real-time.
"""

from implementation import DynamicArray
import time


def visualize_append_step_by_step():
    """Step through appends with DETAILED visualization."""
    print("\n" + "="*70)
    print("INTERACTIVE: Step-by-step Append Visualization")
    print("="*70)
    
    arr = DynamicArray(initial_capacity=2)
    elements_to_add = [10, 20, 30, 40, 50, 60, 70, 80]
    
    print(f"\n[INITIAL STATE]")
    print(f"  Size: {arr.size}")
    print(f"  Capacity: {arr.capacity}")
    print(f"  Buffer: {arr.data}")
    print(f"  Status: Empty array, room for 2 elements")
    
    for idx, elem in enumerate(elements_to_add, 1):
        print(f"\n--- STEP {idx}: Append {elem} ---")
        print(f"  BEFORE:")
        print(f"    Size: {arr.size}, Capacity: {arr.capacity}")
        print(f"    Is full? {arr.size == arr.capacity}")
        
        if arr.size == arr.capacity:
            print(f"    ⚠️  ARRAY IS FULL! Will reallocate...")
            print(f"    Old capacity: {arr.capacity}")
            print(f"    New capacity: {arr.capacity * 2}")
            print(f"    Action: Copy {arr.size} elements to new buffer")
        
        arr.append(elem)
        
        print(f"  AFTER:")
        print(f"    Size: {arr.size}, Capacity: {arr.capacity}")
        print(f"    Buffer: {arr.data}")
        print(f"    Filled slots: {arr.data[:arr.size]}")
        print(f"    Empty slots: {arr.data[arr.size:]}")
    
    print(f"\n[FINAL STATE]")
    print(f"  Total elements appended: {len(elements_to_add)}")
    print(f"  Final size: {arr.size}")
    print(f"  Final capacity: {arr.capacity}")
    print(f"  Memory utilization: {arr.size}/{arr.capacity} = {100*arr.size/arr.capacity:.1f}%")


def visualize_pop_step_by_step():
    """Step through pops with visualization."""
    print("\n" + "="*70)
    print("INTERACTIVE: Pop Visualization")
    print("="*70)
    
    arr = DynamicArray()
    for i in range(5):
        arr.append((i+1) * 10)
    
    print(f"\n[INITIAL STATE]")
    print(f"  Size: {arr.size}")
    print(f"  Capacity: {arr.capacity}")
    print(f"  Buffer: {arr.data}")
    
    for step in range(3):
        print(f"\n--- POP #{step+1} ---")
        print(f"  BEFORE: Size={arr.size}, Elements={arr.data[:arr.size]}")
        
        val = arr.pop()
        
        print(f"  Popped value: {val}")
        print(f"  AFTER: Size={arr.size}, Elements={arr.data[:arr.size]}")
        print(f"  Note: Capacity STAYS {arr.capacity} (no shrinking)")


def visualize_memory_layout():
    """Show memory layout with ASCII art."""
    print("\n" + "="*70)
    print("MEMORY LAYOUT: How Data is Stored in Memory")
    print("="*70)
    
    arr = DynamicArray(initial_capacity=4)
    
    print(f"\n[EMPTY ARRAY]")
    print(f"  arr.size = {arr.size}")
    print(f"  arr.capacity = {arr.capacity}")
    print(f"  arr.data = {arr.data}")
    print(f"\n  Memory layout:")
    print(f"    Logical size: [{arr.size}]")
    print(f"    Buffer:       [{' '.join(['_'] * arr.capacity)}]  (all empty)")
    
    # Add elements
    for elem in [100, 200, 300]:
        arr.append(elem)
    
    print(f"\n[AFTER APPENDING 3 ELEMENTS]")
    print(f"  arr.size = {arr.size}")
    print(f"  arr.capacity = {arr.capacity}")
    print(f"  arr.data = {arr.data}")
    print(f"\n  Memory layout:")
    filled = [str(arr.data[i]) for i in range(arr.size)]
    empty = ['_'] * (arr.capacity - arr.size)
    print(f"    Logical size: [{arr.size}]")
    print(f"    Filled:       [{' '.join(filled)}]")
    print(f"    Empty:        [{' '.join(empty)}]")
    print(f"    Buffer:       [{' '.join(filled + empty)}]")


def visualize_reallocation_cost():
    """Show COST of each append (when reallocation happens)."""
    print("\n" + "="*70)
    print("COST ANALYSIS: Why Append is O(1) Amortized")
    print("="*70)
    
    arr = DynamicArray(initial_capacity=1)
    total_work = 0
    
    print(f"\nAppending 16 elements with doubling strategy:")
    print(f"{'Append #':<10} {'Element':<10} {'Realloc?':<12} {'Work Done':<12} {'Total Work':<12}")
    print(f"-" * 60)
    
    for i in range(16):
        old_cap = arr.capacity
        arr.append(i)
        new_cap = arr.capacity
        
        if old_cap != new_cap:
            # Work = copying old elements
            work = arr.size - 1  # Number of elements copied
            total_work += work
            realloc = f"YES (copy {work})"
        else:
            work = 1  # Just one insertion
            total_work += work
            realloc = "NO"
        
        print(f"{i+1:<10} {i:<10} {realloc:<12} {work:<12} {total_work:<12}")
    
    print(f"\n  Total appends: 16")
    print(f"  Total work: {total_work}")
    print(f"  Average per append: {total_work/16:.2f} ≈ O(1) AMORTIZED")
    print(f"\n  Why? Doubling strategy spreads reallocation cost!")
    print(f"  - Most appends are cheap (O(1))")
    print(f"  - Rare reallocs are expensive (O(n))")
    print(f"  - But reallocs happen so rarely they don't affect average")


def run_interactive_menu():
    """Interactive menu to let user choose which visualization to run."""
    print("\n" + "#"*70)
    print("#  DYNAMIC ARRAY INTERACTIVE VISUALIZER")
    print("#  See how arrays grow, reallocate, and manage memory")
    print("#"*70)
    
    while True:
        print("\nChoose a visualization:")
        print("  1. Step-by-step Append (MOST IMPORTANT - start here!)")
        print("  2. Pop Operations")
        print("  3. Memory Layout Diagram")
        print("  4. Cost Analysis (Why O(1) amortized?)")
        print("  5. Run ALL")
        print("  6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == "1":
            visualize_append_step_by_step()
        elif choice == "2":
            visualize_pop_step_by_step()
        elif choice == "3":
            visualize_memory_layout()
        elif choice == "4":
            visualize_reallocation_cost()
        elif choice == "5":
            visualize_append_step_by_step()
            visualize_pop_step_by_step()
            visualize_memory_layout()
            visualize_reallocation_cost()
        elif choice == "6":
            print("\nGoodbye! You now understand DynamicArray. 🚀")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    run_interactive_menu()
