# my-first-app

## Setup
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

    ```sh
    # this is the ".env" file...

    ALPHAVANTAGE_API_KEY="_________"

    MAILGUN_API_KEY =  "to do"
    SENDER_ADDRESS = "sandbox9963f0dedce64ffc896e58aa1f62a4b3.mailgun.org"
    ```


Create an activate an anaconda environment python

    ```sh
    conda create -n my-first-env python=3.10
    conda activate my-first-env
    ```

Install Packages:
    ```sh
    pip install -r requirements.txt
    ```
can also use a requirements.txt file to install all the packages 

You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.


## Usage 
running the python script 
```sh
python app/my_script.py
```

run the unemployment report 
```sh
python -m app.unemployment

#passing in parameters through the terminal, rather than through .env file
ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py
```

Send an email
```sh
python app/email_service.py

```

## Testing

Run tests:

```sh
pytest
```





