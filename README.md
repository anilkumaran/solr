# solr

## Install solr
Download source files and install dependencies 
```
sudo apt install default-jdk
wget http://www.gtlib.gatech.edu/pub/apache/lucene/solr/8.11.1/solr-8.11.1.tgz
tar zxvf solr-8.11.1.tgz
sudo solr-8.11.1/bin/install_solr_service.sh solr-8.11.1.tgz
```
Apache Solr should now be installed and started as a service automatically. It can be controlled by systemd through a systemctl command.
```
$ sudo systemctl start solr # start Solr
$ sudo systemctl stop solr # stop Solr
$ systemctl status solr # check the status of Solr
$ sudo systemctl enable solr # make Solr start automatically upon reboot
```

## Create a core
```
./create_core.sh <core-name-here>
Ex: ./create_core.sh mycore
```

## Delete a core
```
$ curl http://localhost:8983/solr/admin/cores?action=UNLOAD&core=mycore1&deleteIndex=true&deleteDataDir=true&deleteInstanceDir=true -H "Content-Type: text/xml"
```

## Refresh index of core
```
$ curl http://127.0.0.1:8983/solr/mycore/update?commit=true -H "Content-Type: text/xml" --data-binary "<delete><query>*:*</query></delete>"
```
