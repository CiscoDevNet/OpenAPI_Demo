# API Insights Preview Demo 

These OAS documents illustrate the engineering story for the API Insights Preview at Cisco Live Amsterdam

## Quick steps

The [OAS changelog](./CHANGELOG.md) details the mutiple versions of OpenAPI documents handed over by the Dashboard API engineering team.

Open Chrome and import revision [1.22.0-rev1](oas/1.22.0-rev1.yaml) into [Swagger Editor](https://editor.swagger.io)

Explore the OpenAPI documents scores in API Insights [preview environment](https://testing-developer.cisco.com/api-insights-cisco/timeline?service=minidashboard_api)

Open a different web browser (Firefox) and load revision [1.24.0-rev1](oas/1.24.0-rev1.yaml) into [Swagger Editor](https://editor.swagger.io)

note: for further details, check the [demo playbook](https://cisco.sharepoint.com/:w:/r/sites/DevRelTeam/_layouts/15/doc2.aspx?sourcedoc=%7BFD1D65C8-4190-41A9-8FC0-7550ACA996BA%7D&file=API%20Insights%20Demo%20talk%20and%20flow.docx&action=default&mobileredirect=true&cid=6ae18af4-2f9e-4f78-b43a-a97fb0e7a835)

## User Story

Development teams have an API in production for some time, SRE teams (may also be organization CTO office or a technical lead responsible to review) have asked for the OpenAPI definition of the API. An OpenAPI document was provided to us. 

Let’s look at it with SwaggerEditor, looks good? Shows revision number 1.12.0 

Now let’s loaded into API Insights with 1.12.0 as rev1.

API Insights shows gaps with completeness of Contract and Documentation but also Design Guidelines and Offensive Terms. We will be leaving REST guidelines out for the rest of this  demonstration. 

We’re sending the findings report back to the engineering team and ask to fix for their next release. 

A month later, the engineering team has made progress with the new release and sends the updated OpenAPI document – v1.13.0. They provide a note saying they fixed the Offensive Terms and expanded the OpenAPI document. 

We load the new OAS document 1.13.0 - rev1 into API Insights  

API Insights shows progress: 100% inclusive language, but uncomplete for contract due to errors not being described. Also documentation is lacking examples.

We’re sending the findings reports to the engineering group and asking to fix before 1.23.0 GA release.

Team comes back with the new OpenAPI document and once loaded in API Insights, it shows 100% complete for contract.

We mark revision 1.23.0-rev2 as 'release' in API Insights as the API goes into production.

**2 months later**, the engineering team comes back to us with a new minor release, with addition of an operation PUT and some other minor changes. They provided a OpenAPI document versio 1.24.0.


The team comes back a few months later with a new release which is backward compatible and provides new features  has more features , and they provide a version 1.14.0 of the OpenAPI document, with a release note (X operations or paths). 

We load it into API Insights, it shows revision 1.14.0 and now includes 5 operations.

First we check for the score, including 100% completeness of the API Contract.

> note that API Contracts must be 100% for valid findings - and once contract completeness is reached, API Insights can become the source of truth for changelogs and backward compatibility, but also to provide accurate documentation and confirm drifts and phantoms from live traffic observation).

Now let's look at backward compatibility: we see the operation added but also a breaking change introduced. We inform engineering so that they fix before release.  








