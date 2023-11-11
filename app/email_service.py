import requests #for Mailgun functionality
import os

from dotenv import load_dotenv
#Sendgrid Packages are omitted

#Environment Variables and Constants 
load_dotenv() #go look in .env for env variables 

MAILGUN_API_KEY = str(os.getenv("MAILGUN_API_KEY"))
SENDER_ADDRESS = str(os.getenv("SENDER_ADDRESS"))
MAILGUN_DOMAIN = str(os.getenv("MAILGUN_DOMAIN"))



def send_email(recipient_address=SENDER_ADDRESS, subject="[Shopping Cart App] Testing 123", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    try:
        request_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
        message_data = {
            'from': SENDER_ADDRESS,
            'to': recipient_address,
            'subject': subject,
            'html': html_content,
        }
        response = requests.post(request_url,
            auth=('api', MAILGUN_API_KEY),
            data=message_data
        )
        print("RESULT:", response.status_code)
        response.raise_for_status()
        print("Email sent successfully!")

        return response.status_code
    
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {str(e)}")

        return None


if __name__ == "__main__":
    # only want to run this if running from command line, not if importing a function from this file
    my_content = """

        <img
            src="https://img.freepik.com/free-vector/flat-ice-cream-collection_23-2148982427.jpg"
            alt="image of an ice cream"
            height=100
        >

        <h1>Ice Cream Shop Menu</h1>

        <p>Most popular flavors:</p>

        <ul>
            <li>Vanilla Bean </li>
            <li>Choc </li>
            <li>Strawberry</li>
        </ul>
    """

    user_address = input("Please enter your email address: ")
    send_email(html_content=my_content, recipient_address=user_address)