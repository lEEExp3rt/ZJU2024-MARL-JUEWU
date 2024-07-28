#!/usr/bin/bash
cd /home/lqy/ZJU/ZJU2024-MARL-JUEWU/labs/pymarl
for i in $(seq 1 5)
do
    python3 src/main.py --config=qmix --env-config=sc2 with env_args.map_name=5m_vs_6m
done