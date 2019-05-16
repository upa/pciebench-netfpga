#!/usr/bin/env python3


import argparse
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
from papersetup import ratio, fontsize, markersize, linewidth, lfontsize
from myplotlib import get_marker, get_color, change_aspect_ratio

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

lines = { "linewidth" : linewidth,
          "markersize" : markersize * 0.8,
          "markeredgewidth" : linewidth, }
markers = { "fillstyle" : "none", }
plt.rc("lines", **lines)
plt.rc("markers", **markers)


def parse(filename):

    bpses = []

    with open(filename, "r") as f:
        for line in f:
            bpses.append(float(line.strip().split(",")[3]))
            
    # avg
    s = 0.0
    for bps in bpses:
        s += bps
    return s / len(bpses)


def main():

    fig, ax = plt.subplots()
    
    bytelens = [ 8, 16, 32, 64, 128, 256, 512 ]
    #xaxis = list(range(len(bytelens)))
    xaxis = bytelens

    # Dram, DMA Write DMA Read
    dram = []
    p2pm = []
    for bl in bytelens:
        f = ("../output/pciebench_mem-dram_ptr-fix_len-{}.txt".format(bl))
        dram.append(parse(f))
        f = ("../output/pciebench_mem-p2pmem_ptr-fix_len-{}.txt".format(bl))
        p2pm.append(parse(f))

    print(xaxis)
    print(dram)
    print(p2pm)

    ax.plot(xaxis, dram, marker = get_marker(), color = get_color(),
            label = "DRAM PCIe Read/Write")
    ax.plot(xaxis, p2pm, marker = get_marker(), color = get_color(),
            label = "p2pmem PCIe Read")

    plt.xticks(xaxis, bytelens)
    ax.tick_params(labelsize = fontsize)
    ax.set_ylabel("throughput (Gbps)", fontsize = fontsize)
    ax.set_xlabel("transfer size (byte)", fontsize = fontsize)

    ax.grid(True, linestyle = "--", linewidth = 0.5)
    ax.legend(fontsize = lfontsize)

    ax.set_xticks([8, 64, 128, 256, 512])

    change_aspect_ratio(ax, 1)

    plt.savefig("graph_pciebench.pdf",
                bbox_inches = "tight", pad_inches = 0.05)

if __name__ == "__main__":
    main()
