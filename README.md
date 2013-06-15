conference
==========

A simple conference app showing off Plivo's capability. Provisions a number and a pin, which you can call into to get into the conference

This application shows off Plivo's ability as a platfporm.

__Installation___


Clone the repo:

```bash
    git clone git@github.com:abishekk92/conference.git
```

Install the Python dependencies:

```bash
    pip install -r requirements.txt
```
Note: 

  - You would need pip to be installed. Instructions on how to install pip for variety of operating systems can be found [here](http://www.pip-installer.org/en/latest/installing.html)

  - The app uses MongoDB as the datastore, you can install it following the instruction found [here](http://docs.mongodb.org/manual/installation/)
  
  - The app heavily uses Plivo's API, please make sure to get a [free developer account](http://plivo.com/)
  
  - Update the AUTH_ID and AUTH_TOKEN in the app.config as follows 
  
    ```python
        AUTH_ID="YOUR-AUTH-ID"
        AUTH_TOKEN="YOUR-AUTH-TOKEN"
        BASE_URL="APP-BASE-URL"
    ```
    
  - Update the MongoDB host in models.py with your values as follows
     
     ```python
        connect('conference',host="YOUR-MONGODB_HOST")
     ```
     
  - To run the app
    
    ```bash
        foreman start
    ```
  - Please follow the instructions here to [deploy on heroku]( https://devcenter.heroku.com/articles/python)

__Workflow__ : 
   
   - The apps allows one to create conference on a subject and invite people to the conference by adding their mobile numbers.

   !["Create Conference"](https://raw.github.com/abishekk92/conference/master/screenshots/Screenshot%20from%202013-06-15%2023:12:23.png)
 
   - Or people can choose to join one of the already existing conference by dialing into the Plivo Number along with the conference pin.
   
   !["Join a Conference"](https://raw.github.com/abishekk92/conference/master/screenshots/Screenshot%20from%202013-06-15%2023:15:13.png)
   

   
