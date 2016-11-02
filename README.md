# Group3TeamProject  WordPickingGame
## API reference       
**45.55.248.135**
### Endpoint /getWord:      
#### Request Format:
* __/getWord?long=REAL&lat=REAL&radius=REAL&ids=INT__  
	* long and lat parameters are the geological location of current user. Both of them are floats and should be limited in Urbana/Champaign Area. Otherwise there will be no words.  
	* radius is the range of words the user want to display, the API do strict circular calculation and return all the words within the range
	* ids are the words the user already have in there view. **There could be multiple ids, the API take it as an array**
#### Return Format **JSON STRING**:
	* __{words[  
				{  
					"lat":*latitude of the word*  
					"long":*longitude of the word*  
					"name":*the word*  
					"definition":*definition of the word*  
					"id":*UUID of the word*  
				},  
				{  
					etc....  
				}  
			
			
			]}__  
	 
