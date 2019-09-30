# The API we used
https://cloud.google.com/natural-language/docs/sentiment-tutorial

    We use two functions of google api to develop our project:</br>
    
    (1)Analysis the sediment of the text.</br>
    (2)Analysis the entity in the text and anylysis the sediment of the words related to the entity.

    Here are the outputs of the google api, the inputs are the data grabbed from twitter api.

![Image text](https://github.com/YangHuNU/EC601_Mini_Project_GR15/blob/TJY/googleapi/output1.jpeg)
![Image text](https://github.com/YangHuNU/EC601_Mini_Project_GR15/blob/TJY/googleapi/output2.jpeg)
![Image text](https://github.com/YangHuNU/EC601_Mini_Project_GR15/blob/TJY/googleapi/output3.jpeg)


# System Design and how our esign addresses your user stories
      
      After attaining the data from twitter API, we use google api to pick up entities in the text and only output the entities with 'CONSUMER_GOOD' type, which will filter the unrelated entities. Then we analyze the sediment the words related to these entities and the whole sediment of the text.
