#!/bin/bash
cd /home/rahul/Desktop/Test_qikpod
for i in {1..2}
do
	python3 -m pytest test_portal.py
done
