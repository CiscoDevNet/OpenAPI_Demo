
```shell
# Example of a successful contract
> spectral lint --ruleset ruleset.yaml compliance-1.24.0-rev1.yaml -v Found 59 rules (10 enabled)

Linting /mnt/c/Users/stsfartz/repos/github.com/CiscoDevNet/API_Insights_Demo/rulesets/contract/compliance-1.24.0-rev1.yaml
No results with a severity of 'error' found!
```

```shell
# Example of a failing contract
> spectral lint --ruleset ruleset.yaml compliance-1.22.0-rev1.yaml -v 

Found 59 rules (10 enabled)
Linting /mnt/c/Users/stsfartz/repos/github.com/CiscoDevNet/API_Insights_Demo/rulesets/contract/compliance-1.22.0-rev1.yaml

/mnt/c/Users/stsfartz/repos/github.com/CiscoDevNet/API_Insights_Demo/rulesets/contract/compliance-1.22.0-rev1.yaml
  32:17  warning  error-status-code          There should be at least one error status code either 4xx or 5xx.; none of /^4\d{2}$/,/^5\d{2}$/,/^default$/ are matched              paths./organizations.get.responses
 114:17  warning  error-status-code          There should be at least one error status code either 4xx or 5xx.; none of /^4\d{2}$/,/^5\d{2}$/,/^default$/ are matched              paths./organizations.post.responses
 119:22    error  general-schema-definition  Some of the defined schema use object as a final field when describing their object structure.; properties missing for object schema  paths./organizations.post.responses[201].content.application/json.schema
 145:17  warning  error-status-code          There should be at least one error status code either 4xx or 5xx.; none of /^4\d{2}$/,/^5\d{2}$/,/^default$/ are matched              paths./organizations/{organizationId}.get.responses
 219:17  warning  error-status-code          There should be at least one error status code either 4xx or 5xx.; none of /^4\d{2}$/,/^5\d{2}$/,/^default$/ are matched              paths./organizations/{organizationId}.delete.responses

✖ 5 problems (1 error, 4 warnings, 0 infos, 0 hints)
```