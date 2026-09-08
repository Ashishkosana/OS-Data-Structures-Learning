# Dynamic Array Lab

## What to Do

1. **Read** `docs/ds/dynamic-array.md` — understand the concept, memory layout, and complexity.
2. **Implement** `implementation.py` — fill in the TODO methods:
   - `__init__()` — initialize size, capacity, and data buffer
   - `append()` — add element, reallocate if full
   - `pop()` — remove and return last element
   - `__getitem__()` — get element at index
   - `__setitem__()` — set element at index
   - `reserve()` — manual reallocation
3. **Run** `demo.py` to see your implementation in action:
   ```bash
   python3 demo.py
   ```
4. **Test** with pytest:
   ```bash
   pytest test_dynamic_array.py -v
   ```
5. **Answer** the check questions in `docs/ds/dynamic-array.md`.

## Tips

- **Python lists are heap-allocated.** When you create `self.data = [None] * capacity`, Python allocates on the heap.
- **Doubling strategy:** When `size == capacity`, allocate a new buffer of size `2 * capacity`, copy elements, and free (or let Python GC) the old buffer.
- **Bounds checking:** `__getitem__` and `__setitem__` should only allow indices in `[0, size)`.
- **Reserve:** Resizing to a specific capacity; if shrinking below current size, you may truncate.

## Expected Test Output

When all tests pass:
```
================================ test session starts =================================
...
test_dynamic_array.py::TestDynamicArrayInit::test_init_default PASSED
...
================================ X passed in 0.XXs ==================================
```

## Once Complete

Answer the 4 check questions at the end of `docs/ds/dynamic-array.md`, then wait for review before moving to linked lists.
