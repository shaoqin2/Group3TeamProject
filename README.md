# Group3TeamProject Documentation  

This is the documentation for the word picking game. The backend keep track of all the geological words and user information

# API reference  

45.55.248.135

## Endpoints  

### GET /getWord

Get information of all the words in a certain area  

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`long`| float | the geological longitude of the user(champaign urbana area)
`lat`| float | the geological latitude of the user(champaign urbana area)
`radius`| float | the radius of the circle that the words would be in
`ids`| integer list | the ids of the the words the user does not want. could have multiple ids parameter. API take it as a list  

**Return JSON format:**  

    {"words":[  
                {  
                    "lat" : latitude of the word  
                    "long" : longitude of the word  
                    "name" : the word  
                    "definition" : definition of the word  
                    "id" : UUID of the word  
                },  
                {  
                    etc....  
                },
                {
                    etc....
                },
                ]
    }  

### POST /postWord  
Post a word into the database with all related information  

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`long`| float | the geological longitude of the word(champaign urbana area)
`lat`| float | the geological latitude of the word(champaign urbana area)
`word`| string | the word
`definition`| string | definition of the word  

**Return format:**  

Value | information
--- | ---
success | the word is posted into database successfully
bad request | something went wrong with the post format
