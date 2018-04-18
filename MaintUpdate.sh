#!/bin/bash

cd Watergate45

echo 'Deleting Wgatetimeline' >> log.txt

rm -rf wgatetimeline.csv

echo 'Getting wgatetimeline' >> log.txt

wget https://www.dropbox.com/s/ye6duakbjkqfmzs/wgatetimeline.csv?dl=1 -O wgatetimeline.csv

echo 'Starting Friend List analysis' >> log.txt

python WatergateMaintenance.py

echo 'done' >> log.txt


