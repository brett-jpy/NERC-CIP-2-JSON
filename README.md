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
        "Language": "Each Responsible Entity shall implement a process...",
        "Applicability": "All BCS"
    },
    {
        "Standard": "CIP-002-5.1",
        "Requirement": "R1.1",
        "Language": "Identify each of the high impact...",
        "Applicability": "High BCS only"
    }
~~~

### Easy to Load Into MongoDB

Using PyMongo & Requests

```py
r = requests.get("https://raw.githubusercontent.com/brettjouwstra/NERC-CIP-2-JSON/master/All_Standards.json")

for item in r.json():
    data = {'Standard': item['Standard'], 'Requirement': item['Requirement'], 
            'Language': item["Language"], 'Applicability': item['Applicability'] 
    
    client.insert_one(data)
````

Set a text index on the Database [read here](https://docs.mongodb.com/manual/text-search/), allowing you to answer questions like, "Which standards have 'CIP Senior Manager' in them?" 

```py
# The Double Quotes wrapped by single quotes are to get exact phrase searching

for item in collection.find( { "$text": { "$search": '"CIP Senior Manager"' } } ): 
    print("Standard/Req:  {} - {} \n---Language: {}\n\n".format(item['Standard'], item['Requirement'], item['Language']  ))
```

The output then provides the standards that contain that exact phrase. I've removed all the text after "CIP Senior Manager" just for the example. 

```text
Standard/Req:  CIP-003-8 - R4
---Language: The Responsible Entity shall implement a documented process to delegate authority, unless no delegations are used. Where allowed by the CIP Standards, the CIP Senior Manager ...


Standard/Req:  CIP-003-8 - R3
---Language: Each Responsible Entity shall identify a CIP Senior Manager...


Standard/Req:  CIP-003-8 - R1
---Language: Each Responsible Entity shall review and obtain CIP Senior Manager...


Standard/Req:  CIP-013-1 - R3
---Language: Each Responsible Entity shall review and obtain CIP Senior Manager.... 


Standard/Req:  CIP-007-6 - R2.4
---Language: For each mitigation plan created or revised in Part 2.3, implement the plan within the timeframe specified in the plan, unless a revision to the plan or an extension to the timeframe specified in Part 2.3 is approved by the CIP Senior Manager...


Standard/Req:  CIP-002-5.1 - R2.2
---Language: Have its CIP Senior Manager...
```

