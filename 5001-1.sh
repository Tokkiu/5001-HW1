#!/bin/bash
for i in $(seq 1 100)
do
   mkdir DDM${i}
   date > DDM${i}/time_till_now.txt
done
