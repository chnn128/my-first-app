# my-first-app

## Setup

Create an activate an anaconda environment python:

    ```sh
    conda create -n my-first-env python=3.10
    conda activate my-first-env
    ```

Install Packages: 
    using a requirements.txt file to install all the packages 

    ```sh
    pip install -r requirements.txt
    ```

Obtain API Keys:
    Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).
    You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

Create a ".env" file and paste in the following contents:

    ```sh

    ALPHAVANTAGE_API_KEY = "_________" #paste in your AlphaVantage API Key

    MAILGUN_API_KEY =  "__________" #place in your Mailgun API Key
    SENDER_ADDRESS = "__________" #replace with the domain corresponding to your API Key 

    ```

## Usage 
Running the my_script.py example python script:

    ```sh
    python app/my_script.py
    ```


Running the unemployment report:

    ```sh
    python -m app.unemployment
    ```



    Example code of passing in parameters through the terminal, rather than through .env file   

    ```sh
    ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py
    ```


Send an email:

    ```sh
    python app/email_service.py
    python -m app.email_service
    ```

Run Weather App:

    ```sh
    python -m app.weather_app

    ```

Run Flask App:

    ```sh 
    
    FLASK_APP=web_app flask run

    ```

Run the stocks report

```sh 
python -m app.stocks
```
## Testing

Run tests:
    from the terminal, enter the following command: 

    ```sh
    pytest
    ```






