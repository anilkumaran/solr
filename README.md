# solr
## Delete a core
curl http://localhost:8983/solr/admin/cores?action=UNLOAD&core=mycore1&deleteIndex=true&deleteDataDir=true&deleteInstanceDir=true -H "Content-Type: text/xml"

## Refresh index of core
curl http://127.0.0.1:8983/solr/mycore/update?commit=true -H "Content-Type: text/xml" --data-binary "<delete><query>*:*</query></delete>"
