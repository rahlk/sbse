#!/bin/bash

Title="csc710sbse: hw2:Rahul Krishna"
a2ps --center-title="$Title" -qr2gC -o ~/tmp/listing.ps optimizer.py searcher.py models.py 
ps2pdf ~/tmp/listing.ps listing.pdf

