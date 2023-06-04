# Spectral example

This example uses the tutorial of spectral

```shell
# Success example
> spectral lint --ruleset ruleset.yaml test-success.yaml  -v

Found 1 rules (1 enabled)
Linting /mnt/c/Users/stsfartz/repos/github.com/CiscoDevNet/API_Insights_Demo/rulesets/greeting/test-success.yaml
No results with a severity of 'error' found!
```

```shell
# Failing example
> spectral lint --ruleset ruleset.yaml test-fail.yaml  -v

Found 1 rules (1 enabled)
Linting /mnt/c/Users/stsfartz/repos/github.com/CiscoDevNet/API_Insights_Demo/rulesets/greeting/test-fail.yaml

/mnt/c/Users/stsfartz/repos/github.com/CiscoDevNet/API_Insights_Demo/rulesets/greeting/test-fail.yaml
 2:12  warning  my-rule  Value must equal "hello".  greeting.message

✖ 1 problem (0 errors, 1 warning, 0 infos, 0 hints)
```

