#!/bin/bash

Title="csc710sbse: hw4:Rahul Krishna"
a2ps --center-title="$Title" -qr2gC -f4 -o ~/listing.ps optimizer.py searcher.py models.py 
ps2pdf ~/listing.ps listing.pdf

