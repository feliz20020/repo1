import yagmail
import os
from dotenv import load_dotenv


load_dotenv()



sender = "sreyasrajithlt@gmail.com"
receiver = "steqatxyh@emlpro.com"
subject = 'Test mail using python'
contents = '''
This is the content side for sending mail
'''

yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Send")




receiver = "steqatxyh@emlpro.com"