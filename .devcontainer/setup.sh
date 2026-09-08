#!/bin/bash
# Setup script for xv6-riscv development environment

set -e

echo "=== Installing dependencies ==="
apt-get update
apt-get install -y \
    build-essential \
    git \
    qemu-system-riscv64 \
    gdb-multiarch \
    python3 \
    python3-pip \
    libfdt-dev \
    wget

echo "=== Installing RISC-V cross-compiler ==="
wget -q https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2023.02.15/riscv64-glibc-ubuntu-22.04-gcc-nightly-2023.02.15-nightly.tar.gz
tar -xzf riscv64-glibc-ubuntu-22.04-gcc-nightly-2023.02.15-nightly.tar.gz -C /opt/
rm riscv64-glibc-ubuntu-22.04-gcc-nightly-2023.02.15-nightly.tar.gz

echo "=== Adding RISC-V toolchain to PATH ==="
echo 'export PATH=/opt/riscv/bin:$PATH' >> /root/.bashrc
export PATH=/opt/riscv/bin:$PATH

echo "=== Cloning xv6-riscv ==="
cd /workspace
if [ ! -d "xv6-riscv" ]; then
    git clone https://github.com/mit-pdos/xv6-riscv.git
fi

echo "=== Installing Python dependencies ==="
pip3 install pytest

echo "\n=== Setup Complete ==="
echo "To start learning:"
echo "  1. cd xv6-riscv && make qemu"
echo "  2. In another terminal: riscv64-unknown-elf-gdb kernel/kernel"
echo "     (gdb) target remote :1234"
echo "     (gdb) break main"
echo "     (gdb) continue"
echo ""
echo "Or run Python labs:"
echo "  cd labs/python/dynamic_array"
echo "  python3 visualizer.py"
