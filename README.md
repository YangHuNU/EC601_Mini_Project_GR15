# EC601_Mini_Project_GR15
Mini Project by Group 15

## User's Instruction
Users can get sentimental feedbacks from a keyword search. By default, this product mainly focuses on smoking health sentiments. Therefore, keywords feeding such as "Juul" will be used. The product takes top 20 Twitter feeds and send to Google API for sentiment analysis. Results from analysis are provided to the users. Users can use the information they obtained from this product.
    
## Description on Minimum Value Product
The system consists of two segments of Python program. First, using Twitter API to obtain 20 Twitter feeds. These feeds will be sent to the second segment; Google API for sentiment analysis. Then, the feedbacks from sentiment analysis goes back to the users.

## Flaws 
Every time we run a program, 20 output files is generated. Due to the limitation of sentimental analysis input format. This is one solution we come up with to improve analysis accuracy. However, it is still quite problematic especially 20 files are generated each time. Eventually, the number of files is going to build up and all the files will take a lot of space. 

The results are not accurate enough. It is simply information processed and produced from two APIs. The information the product provided is not user-oriented. 

## Further Development (Potential Plans After MVP)
As shown in the output files, the results from twitter API are mannually forwared to Google for analysis. We will need to build a user interface that once a keyword is typed in, the program itself will provide the final results.

Keyword search from Twitter API can capture content that is more relevant to what user is looking for. Sentiment analysis from Google API can be more accurate. Precision improvement is important if we want to carry on this project after MVP.

The product need to be more user-oriented. As stated previously, this MVP only delivers results generated from API. It is like raw data with very little treatment. Information like raw data can be helpful but it is hard to read and manipulate. A projection for further development is that the results re customized, filtered and made just to satisfy users' needs.


# User story
## Consumer 
As a ***cigarette smoker***, I am able to learn more about people's acceptibility of Juuling, which will help me decide whether I should give up cigarette and change to Juuling.

As a ***family member of a smoker***, I can get information of smoking health, which allows me to take better care of a smoker family member and myself, who is constantly exposed to second-hand smoke.

As an ***owner*** of a bar, after knowing people's attitude to Juul, I can decide whether to sell Juul in my bar.

## Government
As a ***government employee***, I can learn about smoking health awareness and know people's attitude to banning Juul, which will affect policy making regarding Juuling.

## Researchers
As a ***researcher***, I will be able to get information of people's thoughts on Juuling, which can prove or disaprove a point of view in my research. 

## Juul Company
As a ***Juul company***, we can get the information of people’s attitude towards smoking, which can potentially be utilized to improve marketing plans of our products and make better profit out of the business. 

## Juul Salesman
As a ***Juul retailer***, I can develop sales strategies according to people's attitude towards smoking.

# Use case
 ![usecase](https://github.com/YangHuNU/EC601_Mini_Project_GR15/blob/master/use%20case.png)

