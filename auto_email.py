import datetime
import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of environment variables to check
env_vars = ['TO_EMAIL_A', 'EMAIL_A_NAME', 'TO_EMAIL_B', 'EMAIL_B_NAME', 'TO_EMAIL_C']

# Check and print each environment variable
for var in env_vars:
    value = os.getenv(var)
    if value is None:
        logging.error(f"Environment variable {var} not found.")

def send_email(recipient_email, recipient_name):
    # Check if today is a weekday
    if datetime.datetime.now().weekday() >= 5:
        logging.info("Today is a weekend. Not sending the email.")
        return
    
    logging.info("Sending email...")

    from_email = os.getenv('FROM_EMAIL')
    from_email_password = os.getenv('FROM_EMAIL_PASSWORD')
    from_email_smtp = os.getenv('FROM_EMAIL_SMTP')
    from_email_smtp_port = os.getenv('FROM_EMAIL_SMTP_PORT')
    bcc_email = os.getenv('BCC_EMAIL')
    subject = "The Gnarly Griffin seeking exciting partnership with Nintendo"
    
    body = f"""
<div name="messageBodySection">
  <div dir="auto">Hello {recipient_name}.<br>
    <br>
    This is Ryan from the Gnarly Griffin.<br>
    <br>
    The Gnarly Griffin is a new online retailer based in South Africa. Our aim is to turn online shopping into a
    memorable experience for our audience.<br>
    <br>
    My business partner, Juan, and I are avid gamers, comic book enthusiasts and lovers of all things sci-fi and
    fantasy. Our dream is to have a store that can offer all the games, merchandise and collectibles we know and
    love.<br>
    <br>
    We are fairly new to the scene, however we are currently working with various suppliers to provide a wide variety of
    products on our online shop ranging from gaming PC components to statues and collectible figurines like Funko Pops
    to comic books and hopefully soon, console electronics like Nintendo Switch. We have recently onboarded suppliers
    for Xbox and PlayStation hardware that we are so excited about!<br>
    <br>
    You can visit our store at:<br>
    <a href="https://thegnarlygriffin.com" target="_blank">https://thegnarlygriffin.com</a><br>
    <br>
    We would love to have Nintendo on board to extend our offerings and make more customers happy.<br>
    <br>
    Our passion for nerd culture and gaming is what drives us to provide the best experience possible and it's what will
    set us apart to be the 1-stop-shop in South Africa for all things nerdy.<br>
    <br>
    I hope this provides some insight into our mission. Thank you for taking the time to read this message.<br>
    <br>
    I do hope that The Gnarly Griffin and Nintendo will be able to work together very soon.<br>
    <br>
    Take care! And geek out.
  </div>
</div>
<div name="messageSignatureSection"><br>
  <div dir="auto">Kind regards,<br>
    Ryan from the Gnarly Griffin<br>
    <a href="https://thegnarlygriffin.com/" target="_blank">thegnarlygriffin.com</a><br>
    <img alt="gnarly griffin logo"
      style="max-width:100%;height:auto"
      src="https://cdn.shopify.com/s/files/1/0707/2320/7485/files/GG-Email-Signature.svg?v=1719501523">
  </div>
</div>
"""

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(from_email_smtp, from_email_smtp_port)
        server.starttls()
        server.login(from_email, from_email_password)
        text = msg.as_string()
        recipients = [recipient_email] + [bcc_email] if isinstance(bcc_email, str) else bcc_email
        server.sendmail(from_email, recipients, text)
        server.quit()
        logging.info("Email sent successfully")
    except smtplib.SMTPConnectError:
        logging.error("Failed to connect to the SMTP server. Please check the server address and port.")
    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to log in to the SMTP server. Please check your username and password.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {str(e)}")

to_email_a = os.getenv('TO_EMAIL_A')
email_a_name = os.getenv('EMAIL_A_NAME')
to_email_b = os.getenv('TO_EMAIL_B')
email_b_name = os.getenv('EMAIL_B_NAME')
to_email_c = os.getenv('TO_EMAIL_C')
email_c_name = os.getenv('EMAIL_C_NAME')

send_email(to_email_a, email_a_name)
send_email(to_email_b, email_b_name)
send_email(to_email_c, email_c_name)