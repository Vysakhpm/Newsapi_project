# ML_ECS_pipeline
A ML containerisation project which makes use of ECS to deploy a streamlit app which can query data from postgres rds in aws which is populated using a automated labmbda function by making use of a NewsAPI

![Architecture](https://github.com/user-attachments/assets/fe0b968a-992d-4e1e-b5a9-5b11c2388dae)

In this project

* We are making use of a NewsAPI where we get the latest news articles with help of a API_Key obtained from the news api website
  after creating a developer account

* News articles are extracted with the help of a lambda function which is triggered every 1 hr using Event bridge.


* The raw data extrated are pushed to a S3 bucket and stored in json format
 
![S3 BUCKET](https://github.com/user-attachments/assets/7b9b51f4-dbd1-44ee-8de7-3d62329ce39b)

* News description are then analyzed using the using NLTK python library w.r.t the news article topic and based on the news sentiment a positive or negative score is assigned.


* Analyzed  news aritcle are pushed to a rds postgres AWS instance along with timestamp.
(https://github.com/user-attachments/assets/e3de3ce1-7b9d-4373-a9fd-a7085b82c635)
  
* Now a Dashboard is created using Streamlit to visualize the sentiment of the news in local system which is then converted to a docker image and pushed to ECR Registry in AWS.
  
![pg4admin_newstable](https://github.com/user-attachments/assets/7ad5b409-b403-4740-b114-2ba27700cde9)


* The uploaded image is run using a AWS Fargate cluster by create a task definition and using the publicIP and assigned port
  we can access the Streamlit Dashboard.
![Dashboard](https://github.com/user-attachments/assets/92b68ca7-472e-4db5-b90e-d5864b70a537)
