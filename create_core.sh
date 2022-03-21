#!/bin/bash
# Usage: ./create_core.sh <core_name>

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
