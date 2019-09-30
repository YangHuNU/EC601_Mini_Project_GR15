# The API we used
https://cloud.google.com/natural-language/docs/sentiment-tutorial

   We use two functions of google api to develop our project:</br>
    
   (1)Analysis the sediment of the text.</br>
   
   (2)Analysis the entity in the text and anylysis the sediment of the words related to the entity.

   The inputs are the data grabbed from twitter api and the outputs are in test.md


# System Design and how our esign addresses your user stories
      
   After attaining the data from twitter API, we use google api to pick up entities in the text and only output the entities with 'CONSUMER_GOOD' type, which will filter the unrelated entities. Then we analyze the sediment the words related to these entities and the whole sediment of the text.
   The results reflected whether the public are positive or negative to Juul, by which users can get the information about people's attitude to smoking, Juul and smoking health. 
