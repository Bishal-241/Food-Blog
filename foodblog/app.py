from flask import Flask,render_template,request
from mailjet_rest import Client
from key import Mail
import os
myMail = Mail()

mailjet = Client(auth=(myMail.apiKey, myMail.secreatKey), version='v3.1')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/subscription' , methods = ['POST'])
def subscription():
    mailaddr = request.form.get('email')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "noreply@FoodBlog.com",
            "Name": "Food-Blog Digest"
        },
        "To": [
            {
            "Email": mailaddr,
            # "Name": ""
            }
        ],
        "Subject": "Thanks for Subscribing!",
        "TextPart": "Thnks for subscribing , Stay in touch for weelky  recepie digest ",
        # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
        "CustomID": "AppGettingStartedTest"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    if result.status_code == 200:
        print(f'{mailaddr} just subscribed ')

    print(mailaddr)
    return render_template('thanksForSub.html')

