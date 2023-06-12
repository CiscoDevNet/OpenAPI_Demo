# yq

## conversion

```shell
# Convert to JSON
$ yq -o json openapi.yaml > openapi.json
$ cat openapi.yaml | yq -o json 

# Convert to YAML
$ cat openapi.json | yq -o yaml
```

## metrics

``` shell
# total number nb of paths
$ yq ".paths[] | key" compliance-1.24.yaml | wc -l
2

# total number of operations
$ yq ".paths[].* | key" compliance-1.24.yaml | wc -l
5
```




