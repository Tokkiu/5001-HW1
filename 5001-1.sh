#!/bin/bash
for i in $(seq 1 1)
do
   mkdir DDM${i}
   echo 'nanoseconds since 1970-01-01 00:00:00 UTC:' >> DDM${i}/time_till_now.txt
   date +%s%N  >> DDM${i}/time_till_now.txt
done
