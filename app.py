from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# Email templates directory
templates_dir = 'templates'

# Email details
email_details = {
    'welcome': {
        'name': 'User'
    },
    'update': {
        'update_info': 'You have initialised a request to update yout data. We will send you a link in 6 hours on your registered email.'
    },
    'newsletter': {
        'content': 'This is a sample newsletter, especially for you.'
    },
    'promotion': {
        'offer': '10% OFF ONLY FOR YOU.'
    },
    'spotlight_monthly': {
        'videos': [
            {'video_title': 'How to Get Your Brain to Focus | Chris Bailey | TEDxManchester', 'video_thumb': 'https://masterclass.ted.com/static/4ec0a4b5c98da46bb6843cca8d33b744/ee604/TEDSpeakeronstage.png', 'video_category': 'Ted_Talk', 'video_excerpt': 'The latest research is clear: the state of our attention determines the state of our lives. So how do we harness our attention to focus deeper, get distracted less, and even become more creative? Chris Bailey, author of the recent book Hyperfocus, talks about how our ability to focus is the key to productivity, creativity, and living a meaningful life.', 'video_link': 'https://youtu.be/Hu4Yvq-g7_Y?si=AkGkICg-5yDD9PwV'},
            {'video_title': 'How to speak so that people want to listen | Julian Treasure | TED', 'video_thumb': 'https://talkstar-photos.s3.amazonaws.com/uploads/7adc2250-de27-4116-b4ea-6fb4637ca98a/LeraBoroditsky_2017W-embed.jpg', 'video_category': 'Ted_Talk', 'video_excerpt': "Have you ever felt like youre talking, but nobody is listening? Here's Julian Treasure to help you fix that. As the sound expert demonstrates some useful vocal exercises and shares tips on how to speak with empathy, he offers his vision for a sonorous world of listening and understanding.", 'video_link': 'https://youtu.be/eIho2S0ZahI?si=mJz-69oQWdam5B5e'},
        ],
        'articles': [
            {'article_title': 'Strategies of Effective Interviewing', 'article_thumb': 'https://hbr.org/resources/images/article_assets/1964/01/Apr22_22_1146568863.jpg', 'article_category': 'Interview Strategy', 'article_excerpt': 'We all think we know how to carry on our side of a two-way business conversation, but we can get much fuller and more-accurate information if we pay careful attention to strategies of effective interviewing.', 'article_link': 'https://hbr.org/1964/01/strategies-of-effective-interviewing'},
            {'article_title': 'What is a Hard Fork and How it Works in Blockchain?', 'article_thumb': 'https://www.chainalysis.com/wp-content/uploads/2022/02/bloggraphic-blockchains-01-1-2048x1117.png', 'article_category': 'Blockchain', 'article_excerpt': 'A hard fork is a term you might come across often when reading about Blockchain technology. ', 'article_link': 'https://www.blockchain-council.org/blockchain/hard-fork/'}
        ]
    }
}


def generate_email(email_key, email_details):
    env = Environment(loader=FileSystemLoader(templates_dir))
    try:
        template = env.get_template(f'{email_key}.html')
        return template.render(email_details=email_details)
    except:
        return "Template not found"
    

# Email sending function
def send_email(email_key, email_content):
    # print(email_content)
    msg = MIMEMultipart('alternative')
    if email_key == "welcome":
        msg['Subject'] = "Welcome Onboard!"
    elif email_key == "spotlight_monthly":
        msg['Subject'] = "Spotlight Monthly"
    else:
        msg['Subject'] = "New Email from BigStartups."
        
    msg['From'] = "Priyanshi Saxena"
    msg['To'] = "priyanshi.21scse1010358@galgotiasuniversity.edu.in"

    part1 = MIMEText(email_content, 'html')
    msg.attach(part1)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('priyanshi16saxena@gmail.com', 'ppba hril axxf gxon')
        smtp.send_message(msg)

# API endpoints
@app.route('/email', methods=['GET'])
def get_email():
    email_key = request.args.get('email_key')
    if email_key and email_key in email_details:
        email_content = generate_email(email_key, email_details[email_key])
        send_email(email_key, email_content)
        return 'Email sent successfully!'
    else:
        return 'Invalid email key', 400

@app.route('/email', methods=['POST'])
def post_email():
    email_key = request.form['email_key']
    email_details = request.get_json()
    if email_key and email_details:
        email_content = generate_email(email_key, email_details)
        send_email(email_content)
        return 'Email sent successfully!'
    else:
        return 'Invalid email key or details', 400

if __name__ == '__main__':
    app.run(debug=True)