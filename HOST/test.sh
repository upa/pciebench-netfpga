#!/bin/bash

function run_bench() {

	out=$1
	dir=$2
	len=$3
	mem=$4

	echo $len bytes, $mem memory

	sudo sh ./restart.sh
	cmd="sudo ./bin/benchmark \
		-d $dir -t bw -p FIX 0 -n $len -l 100 -c discard \
	       	-P $mem" > $out
	echo $cmd
	$cmd > $out
}


for len in  8 16 32 64 128 256 512; do

	out=output/pciebench_mem-dram_ptr-fix_len-${len}.txt
	run_bench $out RW $len hugepage

	out=output/pciebench_mem-p2pmem_ptr-fix_len-${len}.txt
	run_bench $out W $len 65:00.0

done

