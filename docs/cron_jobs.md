# Cron Jobs Configuration

User: ubuntu

Base path:

/home/ubuntu/Football-Mercato-Application


## Script

scripts/cron_jobs.sh

This script runs different scraping jobs depending on argument.


## Logs

logs/

tuttomercato.log
latest_transfers.log
rumours.log
news_api.log


## Cron jobs

Edit cron:

crontab -e


Tuttomercato

0 17 * * 1,5 /home/ubuntu/Football-Mercato-Application/scripts/cron_jobs.sh tuttomercato


Latest transfers

0 13 * 1,3,5,7,9,11,12 3 /home/ubuntu/Football-Mercato-Application/scripts/cron_jobs.sh latest


Rumours

0 8 * * 1,3,5,7 /home/ubuntu/Football-Mercato-Application/scripts/cron_jobs.sh rumours


News API

0 18 * * * /home/ubuntu/Football-Mercato-Application/scripts/cron_jobs.sh news


## Check logs

tail -f logs/tuttomercato.log

tail -f logs/latest_transfers.log

tail -f logs/rumours.log

tail -f logs/news_api.log