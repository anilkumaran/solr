#!/bin/bash

## DOWNLOAD & INSTALL SOLR
sudo apt install default-jdk
wget http://www.gtlib.gatech.edu/pub/apache/lucene/solr/8.11.1/solr-8.11.1.tgz
tar zxvf solr-8.11.1.tgz
sudo solr-8.11.1/bin/install_solr_service.sh solr-8.11.1.tgz

## CREATE CORE
SOLR_SRC="/opt/solr"      # symlink to your solr-<version> directory
SOLR_ROOT="/var/solr"
SOLR_HOME="${SOLR_ROOT}/data"
CORE=$1

# Create core config set in SOLR_HOME
cd ${SOLR_HOME}/
mkdir -p ${CORE}/data
cp -R ${SOLR_SRC}/server/solr/configsets/_default/conf/ ./${CORE}/ # from default conf
#cp -R ${SOLR_SRC}/server/solr/${CORE}/conf/ ./${CORE}/

# Set ownership
chown -R solr:solr ${SOLR_HOME}

# Create core
${SOLR_SRC}/bin/solr create -c ${CORE} -force
