#!/bin/bash
#Author: kamau andrew

DATE=$(date +'%a-%d-%b-%Y-%H:%m:%S')
/usr/bin/python2.7 $APPS_HOME/twitter-biz-ke/app/run.py >> $APPS_HOME/twitter-biz-ke/app/logs/twitter.log

echo "Done."
