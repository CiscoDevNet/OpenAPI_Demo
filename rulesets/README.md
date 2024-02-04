# Spectral example

This example uses the OpenAPI compliance rule of Spectral

```shell
# Example of a successful contract
> spectral lint compliance-1.22.0-rev1.yaml  -v

Found 51 rules (40 enabled)
Linting compliance-1.22.0-rev1.yaml
No results with a severity of 'error' found!
```

```shell
# Example of a failing contract
> spectral lint incremental-1.26.0-Rev.3.yaml  -v
Found 51 rules (40 enabled)
Linting incremental-1.26.0-Rev.3.yaml

 176:25  error  oas3-valid-media-example  "value" property type must be object  paths./organizations.post.responses[201].content.application/json.examples.MiniOffice.value
 266:25  error  oas3-valid-media-example  "value" property type must be object  paths./organizations/{organizationId}.get.responses[200].content.application/json.examples.MiniOffice2.value
 377:25  error  oas3-valid-media-example  "value" property type must be object  paths./organizations/{organizationId}.put.responses[200].content.application/json.examples.MiniOffice4.value

✖ 3 problems (3 errors, 0 warnings, 0 infos, 0 hints)
```