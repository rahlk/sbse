#!/bin/bash

Title="csc710sbse: hw2:Rahul Krishna"
a2ps --center-title="$Title" -qr2gC -o ~/tmp/listing.ps SA_Fonseca.py log_sa_fonseca.txt SA_Kursawe.py log_sa_kursawe.txt MaxWalkSat.py log_mwalksat.txt
ps2pdf ~/tmp/listing.ps listing.pdf

