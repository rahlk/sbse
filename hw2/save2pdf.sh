#!/bin/bash

Title="csc710sbse: hw1:Rahul Krishna"
a2ps --center-title="$Title" -qr2gC -o ~/tmp/listing.ps hw1_1.py output.log
ps2pdf ~/tmp/listing.ps listing.pdf

