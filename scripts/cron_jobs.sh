#!/bin/bash

BASE_DIR=/home/ubuntu/Football-Mercato-Application
PYTHON=/usr/bin/python3
LOG_DIR=$BASE_DIR/logs

mkdir -p $LOG_DIR


run_tuttomercato() {

LOG=$LOG_DIR/tuttomercato.log

echo "===== START tuttomeracto =====" >> $LOG
date >> $LOG

$PYTHON $BASE_DIR/web_scraping/transfermarkt/tuttomercato/main.py >> $LOG 2>&1

echo "===== END =====" >> $LOG
date >> $LOG

}



run_latest_transfers() {

LOG=$LOG_DIR/latest_transfers.log

echo "===== START latest transfers =====" >> $LOG
date >> $LOG

for file in $BASE_DIR/web_scraping/transfermarkt/latest_transfers/*.py
do
    $PYTHON "$file" >> $LOG 2>&1
done

echo "===== END =====" >> $LOG
date >> $LOG

}



run_rumours() {

LOG=$LOG_DIR/rumours.log

echo "===== START rumours =====" >> $LOG
date >> $LOG

for file in $BASE_DIR/web_scraping/transfermarkt/get_rumours/*.py
do
    $PYTHON "$file" >> $LOG 2>&1
done

echo "===== END =====" >> $LOG
date >> $LOG

}


SOURCES=(
"Fabrizio Romano"
"Florian Plettenberg"
"Christian Falk"
"Gianluca Di Marzio"
"David Ornstein"
"Paul Joyce"
"Matt Law"
"Gerard Romero"
"Matteo Moretto"
"Julien Laurens"
"Nicolo Schira"
"CaughtOffside"
"TEAMtalk"
"Transfermarkt"
"Football365"
)

run_news_api() {

LOG=$LOG_DIR/news_api.log

echo "===== START news =====" >> $LOG
date >> $LOG

for item in "${SOURCES[@]}"
do

echo "Running for $item" >> $LOG

$PYTHON \
$BASE_DIR/web_scraping/transfermarkt/news_api/main.py \
"$item" >> $LOG 2>&1

done

echo "===== END =====" >> $LOG
date >> $LOG

}



case "$1" in

tuttomercato)
run_tuttomercato
;;

latest)
run_latest_transfers
;;

rumours)
run_rumours
;;

news)
run_news_api
;;

*)
echo "Usage: cron_jobs.sh {tuttomercato|latest|rumours|news}"
;;

esac