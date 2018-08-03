# Redash Project


This repository contains the  code for my  Project.

In this project I implemented a service which will send latest result of scheduled query in Redash to all recipient at scheduled time by user. In Redash we scheduled a query and query will be exceuted at scheduled time after that user can connect to this webapp by using http://localhost:5001/home link. On this webpage user can enter recipient email id on which he want result of query and schedule this emailing task by entering the time in this webpage.Query result will be sent to corresponding email id.
This webpage will always send latest scheduled query result in .csv format.


### Quick Setup For Redash
1. First install docker on local 

2. For Redash Repository and clone it on a local folder.

3.Go to redash folder by using - /redash

 4. Run following commonds one after other in oreder 
(a.)   docker-compose -f docker-compose.production.yml run --rm server create_db
(b.)  docker-compose -f docker-compose.production.yml up
 
5. After that type localhost:80 in your browser it will open the login page of Redash fill the details
 
 <img width="1440" alt="login" src="https://user-images.githubusercontent.com/40884871/43533853-7aa05fe6-95d3-11e8-84a2-aafe7c91a21c.png">
 
 
 
 
 
 
 
 
 
 

 6. Create data Source by clicking on new data source.
 
 <img width="1440" alt="new data source" src="https://user-images.githubusercontent.com/40884871/43534094-1afb61c0-95d4-11e8-8640-4a099202c45d.png">
 
 
 
 
 I used Postgres database. To use postgres database click on postgres and and fill details as following-

<img width="1440" alt="fill details for postgres" src="https://user-images.githubusercontent.com/40884871/43534775-cf0e7728-95d5-11e8-817b-ce2505975b3e.png">
  Name - Anything you want to type
  
  Host- (For it run you have to run these commonds in oreder)
  a. docker ps 
  b. docker inspect 82b956c22038 | grep “PAddress”
     here 82b956c22038 container id of postgres databse replace it accordingly 
  c.Now you will get host address paste it into host field.
   
  d. User- postgres
   
  e.database - postgres
   now click add and test if you see green symbol it means you have successfully connected with postgres databse
 
 7. Now click on create in redash webpage and click on query
 
 8. Create table .Table will look like this
  <img width="1440" alt="screen shot 2018-08-02 at 7 47 46 pm" src="https://user-images.githubusercontent.com/40884871/43589841-321019b4-968d-11e8-9a8b-391066fb74cc.png">

 
 9. Schedule a query by typing query and save it and you will see refresh Schedule option in lift side in the bottom.You can    schedule your query.Query will be auto exceuted by redash at scheduled time .
  <img width="1440" alt="schedule query" src="https://user-images.githubusercontent.com/40884871/43534986-628abf52-95d6-11e8-8794-81c8cb1dd9d7.png">
  <img width="1440" alt="scheduled successfully" src="https://user-images.githubusercontent.com/40884871/43535020-7baf736a-95d6-11e8-8e42-e6b8e546310a.png">

### Setup for Email Sending Service
 
10. After that make a seprate directory using  mkdir commond and clone this Email Sending Service app
 
 11. now go to inside folder and copy the query url from redash 
   For it you have to click on the button as shown in the image and and click on  show  API
   Key and copy the API key for csv format result.
   <img width="1440" alt="copy api key" src="https://user-images.githubusercontent.com/40884871/43535117-bf78c704-95d6-11e8-9be6-ea6686bc0d30.png">
   <img width="1440" alt="for csv format" src="https://user-images.githubusercontent.com/40884871/43535154-d35bfbce-95d6-11e8-8299-f04085e97e3f.png">

 12. Now paste it into inside the function name fun_email() of  Sender_Email.py file in the variable name query_url
     this query url will remain same even on changing query. By using this url you can always download latest result of running query.
 13. Now run app.py file from commond prompt by typing python app.py

 14.Now flask server will be running at port no. 5001 .Now go to your browser and type
  localhost:5001/home
  it will open a webpage now add email id where you want to get result of query running in Redash.
  
  <img width="1440" alt="screen shot 2018-08-01 at 10 07 09 pm" src="https://user-images.githubusercontent.com/40884871/43535395-7ff25e00-95d7-11e8-99d2-d147203713ec.png">
  
 15. Add schedule time by typing time in HH:MM AM/PM format in the text box given on webpage and click on schedule button .
  Now query results will be sent on corresponding email ids.




16. I created a thread which will run in background and it will do communication with flask app to get the values of email ids and and scheduled time.

<img width="1440" alt="screen shot 2018-08-02 at 8 07 33 pm" src="https://user-images.githubusercontent.com/40884871/43590992-f9e66bd0-968f-11e8-91de-5d29634df50a.png">

<img width="1440" alt="screen shot 2018-08-02 at 8 07 40 pm" src="https://user-images.githubusercontent.com/40884871/43591069-1b9fc168-9690-11e8-9a67-b3cacedd757d.png">



   
 
 




