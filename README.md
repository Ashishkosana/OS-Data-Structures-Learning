# OS Data Structures Learning

Learn data structures by reading how they are actually used in a real operating system kernel. Annotated code examples, Python implementations, and experiments—not memorized abstractions.

## The Learning Loop (3 phases)

1. **Concept + Memory** → Read the theory; understand memory layout and invariants.
2. **Python Implementation** → Build the structure in Python; run demos and tests locally.
3. **Kernel Annotation** → Point to real xv6-riscv code where the same idea appears; see why the OS chose this layout.

Later: optional QEMU boots and kernel step-debugging with gdb.

## Repository Structure

```
.
├── README.md                    (this file)
├── docs/
│   ├── 00-overview.md           (map of DS → OS subsystems)
│   ├── memory-layout.md         (text/data/BSS/heap/stack; kernel vs user)
│   └── ds/
│       └── dynamic-array.md     (one doc per structure)
├── labs/
│   └── python/
│       └── dynamic_array/       (implementation, demo, tests)
├── annotations/
│   └── xv6/
│       └── dynamic-array.md     (file:line citations + short quotes)
├── diagrams/                    (mermaid, ASCII, or images)
└── cheatsheets/
    └── complexity.md            (ops + when OS picks this structure)
```

## Prerequisites

- Python 3.8+
- pytest (for running tests)
- Text editor or IDE
- Curiosity about how kernels actually work

## Curriculum Order

We follow this sequence, finishing each before moving to the next:

1. Memory layout (text/data/BSS/heap/stack; kernel vs user)
2. Dynamic arrays / buffers
3. Linked lists (singly, doubly, intrusive)
4. Stacks
5. Queues / ring buffers / wait-queue ideas
6. Hash tables
7. Trees / BST / heaps / priority queues (scheduler)
8. Graphs / Union-Find (if clearly useful)

Then: searching and sorting, tied back to which structures enable them.

**Out of scope:** SQL, databases, general algorithm theory divorced from OS usage.

## How to Study Each Structure

For every data structure:

1. **Read** `docs/ds/<name>.md` — concept, memory layout, invariant, complexity.
2. **Run** the Python lab in `labs/python/<name>/` — implement it, run demos, pass tests.
3. **Annotate** yourself by reading `annotations/xv6/<name>.md` — see the kernel code pointer.
4. **Answer** the check questions at the end of the doc.
5. **Wait** for review before advancing.

## References

- **xv6-riscv source:** https://github.com/mit-pdos/xv6-riscv (cited, not vendored)
- **Learning style:** Abdul-Bari clarity—plain, technical, no analogies or scavenger hunts.
- **You own the code:** scaffolds and partials provided; you type and run.

---

**Status:** Milestone 1 in progress (memory layout + dynamic arrays).
