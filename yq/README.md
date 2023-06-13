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

## list status or error codes in a YAML document

```shell
# show all status codes
$ yq ".paths[].[].responses | map_values(.description)" compliance-1.22.yaml | sort -u
'200': Successful operation
'201': Successful operation
'204': Successful operation

# show all status codes
$ yq ".paths[].[].responses | map_values(.description)" compliance-1.24.yaml | sort -u
'200': Success
'201': Success
'204': Success
'400': Bad request
'401': Unauthorized
'403': Forbidden
'429': Too many requests
'500': Internal service error
'502': Bad gateway
'503': Service unavailable
'504': Gateway timeout
```

## extract all tags as an array to include at the top of the document

```shell
# show all tags as an array of name/description
yq ".paths[].*.tags" compliance-1.24.yaml | sort -u | yq '.[] as $item ireduce ([]; . + { "name" : $item, "description" : $item } )'

- name: configure
  description: configure
- name: read
  description: read
```
