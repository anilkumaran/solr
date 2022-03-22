#!/bin/bash

## DOWNLOAD & INSTALL SOLR
sudo apt install default-jdk
wget http://www.gtlib.gatech.edu/pub/apache/lucene/solr/8.11.1/solr-8.11.1.tgz
tar zxvf solr-8.11.1.tgz
sudo solr-8.11.1/bin/install_solr_service.sh solr-8.11.1.tgz
