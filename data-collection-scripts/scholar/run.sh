#!/bin/bash

for year in {1991..2023}
do
	scrapy crawl --pdb scholarv1 -a start_year=$year -a end_year=$year -o result/${year}_denial_of_service.csv --logfile result/${year}.log
done
