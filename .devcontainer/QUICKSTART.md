# xv6-riscv Learning Environment - Quick Start

## 1. Create GitHub Codespace

1. Go to: https://github.com/Ashishkosana/OS-Data-Structures-Learning
2. Click `<> Code` (green button, top right)
3. Click `Codespaces` tab
4. Click `Create codespace on main`
5. Wait 2-3 minutes for environment to load

## 2. Once Loaded, You'll Have:

✅ RISC-V cross-compiler  
✅ QEMU emulator  
✅ gdb debugger  
✅ xv6-riscv kernel source  
✅ Python environment  

---

## 3. Boot xv6-riscv Kernel (Live!)

### Terminal 1: Run QEMU
```bash
cd /workspace/xv6-riscv
make clean
make qemu
```

**You'll see:**
```
xv6 kernel starting
cpu0: starting 1 cpu
hart 1 starting
init: starting sh
$
```

**🎉 You're now inside the xv6 kernel!**

Try commands:
```bash
ls
echo hello
ps
```

---

### Terminal 2: Debug with gdb (in Codespace)

**While xv6 is running in Terminal 1, open a new terminal (Terminal 2):**

```bash
cd /workspace/xv6-riscv
riscv64-unknown-elf-gdb kernel/kernel
```

**In gdb prompt:**
```
(gdb) target remote :1234
(gdb) break scheduler
(gdb) continue
(gdb) step
(gdb) print proc
```

**You'll see:**
- Kernel code stepping line-by-line
- Variables and memory contents
- Process state
- Linked lists, page tables, etc.

---

## 4. What to Explore First

### View Kernel Source
```bash
cd /workspace/xv6-riscv
ls kernel/
```

**Key files for data structures:**
- `kernel/proc.c` — Process management (linked lists, scheduler)
- `kernel/kalloc.c` — Memory allocator (free list, buddy allocator)
- `kernel/fs.c` — File system (inode structures)
- `kernel/trap.c` — Interrupt handling

### Step Through Scheduler (Most Interesting)

**Terminal 1:** `make qemu`

**Terminal 2:**
```bash
cd /workspace/xv6-riscv
riscv64-unknown-elf-gdb kernel/kernel
(gdb) target remote :1234
(gdb) break scheduler   # Set breakpoint in scheduler
(gdb) continue          # Run until scheduler is called
(gdb) info locals       # See local variables
(gdb) print p->name     # Print process name
(gdb) step              # Step through one line
```

---

## 5. Run Python Labs (No Debugging Needed)

```bash
cd /workspace/labs/python/dynamic_array
python3 visualizer.py
```

Choose option 1 to see step-by-step append visualization.

---

## 6. Key Concepts to Learn

### Process Scheduling (Linked Lists)
- Open `kernel/proc.c` line 100+
- See `struct proc` and run queue
- Set gdb breakpoint at scheduler
- Watch processes being scheduled

### Memory Allocation (Free List / Buddy)
- Open `kernel/kalloc.c`
- See how kernel allocates pages
- Track `kmalloc()` / `kfree()` calls in gdb

### File System (Inode Trees)
- Open `kernel/fs.c`
- See hierarchical inode structures

---

## 7. Troubleshooting

### "QEMU not found"
```bash
apt-get install qemu-system-riscv64
```

### "RISC-V compiler not found"
```bash
export PATH=/opt/riscv/bin:$PATH
```

### "GDB connection refused"
Make sure QEMU is running in Terminal 1 before connecting in Terminal 2.

---

## 8. Next Steps

1. ✅ Boot xv6
2. ✅ Connect gdb
3. ✅ Set breakpoints in scheduler
4. ✅ Watch processes run
5. ✅ Inspect linked lists, memory
6. ✅ Answer check questions

---

**Enjoy learning OS data structures in action!** 🚀
