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

Using PyMongo & Requests

```py
r = requests.get("https://raw.githubusercontent.com/brettjouwstra/NERC-CIP-2-JSON/master/All_Standards.json")

for item in r.json():
    data = {'Standard': item['Standard'], 'Requirement': item['Requirement'], 'Language': item["Language"], 'Applicability': item['Applicability'] 
    
    client.insert_one(data)
````

Set a text index on the Database [read here](https://docs.mongodb.com/manual/text-search/), allowing to answer questions like, "Which standards have 'CIP Senior Manager' in them?" 

```py
for item in collection.find( { "$text": { "$search": '"CIP Senior Manager"' } } ): # The Double Quotes wrapped by single quotes are to get exact phrase searching
    print("Standard/Req:  {} - {} \n---Language: {}\n\n".format(item['Standard'], item['Requirement'], item['Language']  ))
```

The output then provides the standards that contain that exact phrase. *Disclaimer* They're not in order 

```py
Standard/Req:  CIP-003-8 - R4
---Language: The Responsible Entity shall implement a documented process to delegate authority, unless no delegations are used. Where allowed by the CIP Standards, the CIP Senior Manager may delegate authority for specific actions to a delegate or delegates. These delegations shall be documented, including the name or title of the delegate, the specific actions delegated, and the date of the delegation; approved by the CIP Senior Manager; and updated within 30 days of any change to the delegation. Delegation changes do not need to be reinstated with a change to the delegator.


Standard/Req:  CIP-003-8 - R3
---Language: Each Responsible Entity shall identify a CIP Senior Manager by name and document any change within 30 calendar days of the change.


Standard/Req:  CIP-003-8 - R1
---Language: Each Responsible Entity shall review and obtain CIP Senior Manager approval at least once every 15 calendar months for one or more documented cyber security policies that collectively address the following topics:


Standard/Req:  CIP-013-1 - R3
---Language: Each Responsible Entity shall review and obtain CIP Senior Manager or delegate approval of its supply chain cyber security risk management plan(s) specified in Requirement R1 at least once every 15 calendar months. 


Standard/Req:  CIP-007-6 - R2.4
---Language: For each mitigation plan created or revised in Part 2.3, implement the plan within the timeframe specified in the plan, unless a revision to the plan or an extension to the timeframe specified in Part 2.3 is approved by the CIP Senior Manager or delegate.


Standard/Req:  CIP-002-5.1 - R2.2
---Language: Have its CIP Senior Manager or delegate approve the identifications required by Requirement R1 at least once every 15 calendar months, even if it has no identified items in Requirement R1.
```

