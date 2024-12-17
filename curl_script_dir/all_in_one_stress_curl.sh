#!/bin/bash

read -p 'Do you want a cpu stress test?(y/n): ' cpu_stress

if [ "$cpu_stress" == "y" ]; then
    cpu_run="True"

    read -p 'Please enter the arguments(cpu_num): ' cpu_num
    
    read -p 'Please enter the arguments(percentage): ' percentage
else
    cpu_run="False"
fi

read -p 'Do you want a gpu stress test?(y/n): ' gpu_stress

if [ "$gpu_stress" == "y" ]; then
    gpu_run="True"
else
    gpu_run="False"
fi

read -p 'Do you want a memory stress test?(y/n): ' memory_stress

if [ "$memory_stress" == "y" ]; then
    memory_run="True"
    read -p 'Please enter the arguments(mem_amount): ' mem_amount
else
    memory_run="False"
fi

read -p 'Do you want a disk stress test?(y/n): ' disk_stress

if [ "$disk_stress" == "y" ]; then
    disk_run="True"
    read -p 'Please enter the arguments(size_mb): ' size_mb
else
    disk_run="False"
fi

read -p 'Do you want a network stress test?(y/n): ' network_stress

if [ "$network_stress" == "y" ]; then
    network_run="True"

    read -p 'Please enter the arguments(mode): ' mode

    read -p 'Please enter the arguments(net_url): ' net_url

    read -p 'Please enter the arguments(net_port): ' net_port

    read -p 'Please enter the arguments(network_mode): ' network_mode
else
    network_run="False"
fi

read -p 'Please enter the arguments(duration): ' duration

curl "http://10.0.2.193:5000/aio?cpu_stress=$cpu_run&gpu_stress=$gpu_run&memory_stress=$memory_run&disk_stress=$disk_run&network_stress=$network_run&duration=$duration&mode=$mode&net_url=$net_url&net_port=$net_port&network_mode=$network_mode&cpu_num=$cpu_num&percentage=$percentage&mem_amount=$mem_amount&size_mb=$size_mb" &