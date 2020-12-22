# NERC-CIP Standards as JSON

Current Progress:

[x] CIP-002 
[x] CIP-003 
[x] CIP-004 
[x] CIP-005 
[x] CIP-006 
[x] CIP-007 
[x] CIP-008 
[x] CIP-009 
[x] CIP-010 
[x] CIP-011 
[x] CIP-013 


### Example of Structure

~~~json
    {
        "Standard": "CIP-002-5.1",
        "Requirement": "R1",
        "Language": "Each Responsible Entity shall implement a process that considers each of the following assets for purposes of parts 1.1 through 1.3: i. Control Centers and backup Control Centers; ii. Transmission stations and substations; iii. Generation resources; iv. Systems and facilities critical to system restoration, including Blackstart Resources and Cranking Paths and initial switching requirements; v. Special Protection Systems that support the reliable operation of the Bulk Electric System; and vi. For Distribution Providers, Protection Systems specified in Applicability section 4.2.1 above.",
        "Applicability": "All BCS"
    },
    {
        "Standard": "CIP-002-5.1",
        "Requirement": "R1.1",
        "Language": "Identify each of the high impact BES Cyber Systems according to Attachment 1, Section 1, if any, at each asset;",
        "Applicability": "High BCS only"
    }
~~~

Notice that all the subparts are included as part of the main language. 


### Easy to Load Into MongoDB

Using PyMongo

```py
with open('cip.json', 'r') as f:
    data = json.load(f)

    for value in data:
        client.insert_one(value)
````

