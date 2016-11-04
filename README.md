# Group3TeamProject  WordPickingGame
## API reference       
**45.55.248.135**
### Endpoint /getWord:      
#### Request Format:
* __/getWord?long=FLOAT&lat=FLOAT&radius=FLOAT&ids=INT__  
	* long and lat parameters are the geological location of current user. Both of them are floats and should be limited in Urbana/Champaign Area. Otherwise there will be no words.  
	* radius is the range of words the user want to display, the API do strict circular calculation and return all the words within the range
	* ids are the words the user already have in there view. **There could be multiple ids, the API take it as an array**  
	

#### Return **JSON STRING** Format :
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
	 
### Endpoint /postWord:      
#### Request Format:
* __/postWord?long=FLOAT&lat=FLOAT&word=STRING&definition=STRING__  
	* long and lat parameters are the geological location of the word. Both of them are floats.
	* if the backend successfully posts the word into the database, it will return success as a string
	
