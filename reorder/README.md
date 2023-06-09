# Normalizng OpenAPI document

Using `openapi-format`: see 
and `yq`: see https://mikefarah.gitbook.io/yq/operators/sort-keys


## Installation

Run command: `npm install -g openapi-format`

Download and add to your path the latest yq release from: https://github.com/mikefarah/yq/releases


## Quick start

```shell
# Sort the different sections/subsections of the OpenAPI document
openapi-format --sortFile config_sort.json openapi.yaml --output openapi_sorted.yaml

# Reorder values by alphabetical for particular OpenAPI attributes
 yq 'sort_keys(.components.schemas)' openapi_sorted.yaml > openapi_sorted_components.yaml
```