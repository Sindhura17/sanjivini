import json
import requests


page_id="111955640361443"
page_access_token="EAAH5vh5dbawBAEYQBJZBiNCZAWY3lu0D4AmAhLpr2ge7SNlsqQpVa4MZBWuSxEOLbtHXLR2LMc8vm4JxtKoZCcBoBrVyy8PE1Cweun588zZBx4MZC84jnSb6FDn83TOmHndMrN1qZBCUDebuy6KyZAo2f3iHZCtz4sRtHRiQyyTNdsfaOrakY4dA0yY0uMeJnCtsZD"
def publish_photo_msg(message, image_url):
        # write your code here
        url="https://graph.facebook.com/v5.0/"+page_id +"/photos"
        params={"access_token":page_access_token,
        "url":image_url,
        "caption":message,
        }
        requests.post(url,params)
        return 

