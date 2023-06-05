# API Insights Preview Demo 

The OpenAPI documents in this repo are used to illustrate the collaboration between a technical lead and an engineering team working on the next release of their API.

## Quick steps

The [changelog](./compliance/CHANGELOG.md) details the multiple versions of OpenAPI documents handed over by the engineering team.

Open Chrome and import revision [1.22.0-rev1](./compliance/compliance-1.22.0-rev1.yaml) into [Swagger Editor](https://editor.swagger.io).

Explore the OpenAPI documents scores in API Insights [preview environment](https://developer.cisco.com/api-insights-preprod/timeline?service=demo--minidashboard_api).

Open a different web browser (Firefox) and load revision [1.24.0-rev1](./compliance/compliance-1.24.0-rev1.yaml) into [Swagger Editor](https://editor.swagger.io)


## User Story

An engineering group has an API in production for some time.
We are an SRE team (may also be an SRE organization CTO office or a group of technical leads responsible to review) and have asked for the OpenAPI definition of the API.
An OpenAPI document was provided back to us. 

Let’s look at it with SwaggerEditor, looks good? Shows revision number 1.22.0 

Now let’s loaded into API Insights with 1.22.0 as rev1.

API Insights shows gaps with completeness of Contract and Documentation but also Design Guidelines and Offensive Terms. We will be leaving REST guidelines out for the rest of this demonstration. 

We’re sending the findings report back to the engineering team and ask to fix for their next release. 

**A month later**, the engineering team has made progress with the new release and sends the updated OpenAPI document – v1.23.0. They provide a note saying they fixed the Offensive Terms and expanded the OpenAPI document. 

We load the new OAS document 1.23.0 - rev1 into API Insights  

API Insights shows progress: 100% inclusive language, but uncomplete for contract due to errors not being described. Also documentation is lacking examples.

We’re sending the findings reports to the engineering group and asking to fix before 1.23.0 GA release.

Team comes back with the new OpenAPI document **a week later** and once loaded in API Insights, it shows 100% complete for contract.

We mark revision 1.23.0-rev2 as 'release' in API Insights as the API goes into production.

**2 months later**, the engineering team comes back to us with a new minor release, with addition of an operation PUT and some other minor changes. They provide an OpenAPI document version 1.24.0.

We load it into API Insights, it shows revision 1.24.0 and now includes 5 operations.

First we check for the score, including 100% completeness of the API Contract.

> note that API Contracts must be 100% for valid findings - and once contract completeness is reached, API Insights can become the source of truth for changelogs and backward compatibility, but also to provide accurate documentation and confirm drifts and phantoms from live traffic observation).

Now let's look at backward compatibility: we see the operation added but also a breaking change introduced. We inform engineering so that they fix before release.  


### Going further

* integrating with engineering CI/CD pipeline, the gaps would be identified automatically 

* using the API Insights Visual Studio Code Extension, this flow would be simplified because engineering can spot gaps early on. 


### Wrap up

API Insights helped us identify offensive terms and fix for the next release. 

API Insights was instrumental to provide tips to get to 100% completeness for the API Contract and Documentation. 

Finally, API Insights prevented us from introducing a breaking change for the next release of the API. 

Note: API Insights can also help with Design Conventions using a spectral ruleset defined for your organizations. Also Panoptica can complement API Insights by providing security insights via both static analysis of contracts (is the API using your organization policies) but also via live traffic observations to ensure there are no drift related to security and zombies or shadow APIs 

