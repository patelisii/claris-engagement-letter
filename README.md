# Claris Engagement Letter Generation API

## Tasks

1. Customer Database creation
    - create a sample database of fake customers
    - create a retriever tool (likely an OpenAI function) to query the database
2. Create retrieval pipeline
    - Set input variables
        - Customer name
        - Type of engagement (Tax compliance or Tax consulting)
        - List of Services (e.g. "Corporate tax strategy planning" "State and local tax compliance review")
        - Fee Structure
            - amount
            - schedule
        - Project Timeline
            - informationDeadline
            - completionDate
        - Signer Information (name and title)
    - Data we query
        - customer info using customer name
        - letter template using engagement type
        - TODO: MSA date using customer name



## Commands
To host the api, run the following command in your terminal: 
```
uvicorn main:app --reload
```



