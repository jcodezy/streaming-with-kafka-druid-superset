# Superset 

Superset can be installed on one of the nodes (query node preferrably) or run locally. 

Since the Superset installation is more straight forward than Kafka and Druid, 
you can see the Superset installation instructions [HERE](https://superset.apache.org/docs/installation/installing-superset-from-scratch)

## Starting Superset 

```
# After installation, go into the Superset directory and run:
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
```  

## Superset UI
If there's no error in terminal, you should be able to access the Superset UI.
Go into your browser and enter
```
# If you installed Superset on a VM
[VM_EXTERNAL_IP]:8088 

# If you installed Superset locally
localhost:8088
``` 

