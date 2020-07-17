import json
import requests
def publish_photo_msg(message, image_url):
        page_id="111955640361443"
        page_access_token="EAAH5vh5dbawBAEYQBJZBiNCZAWY3lu0D4AmAhLpr2ge7SNlsqQpVa4MZBWuSxEOLbtHXLR2LMc8vm4JxtKoZCcBoBrVyy8PE1Cweun588zZBx4MZC84jnSb6FDn83TOmHndMrN1qZBCUDebuy6KyZAo2f3iHZCtz4sRtHRiQyyTNdsfaOrakY4dA0yY0uMeJnCtsZD"
        # write your code here
        url="https://graph.facebook.com/v5.0/"+page_id+"/photos"
        params={"access_token":page_access_token,
        "url":image_url,
        "caption":message,
        }
        j=requests.post(url,params)
        print(j)
        return 
        
        
publish_photo_msg("Second post","https://www.google.co.in/search?q=ice+cream+images&sxsrf=ALeKk02BFm85IdzFkVXnPsVU3xL3n0HRqw:1594981023440&tbm=isch&source=iu&ictx=1&fir=Izk9xz_wgvai-M%252C3tI7KB2eZT2cWM%252C_&vet=1&usg=AI4_-kRabCIj-HG2oOdiCQPM638rBt16lw&sa=X&ved=2ahUKEwiPic2qh9TqAhUVX30KHYdCAhwQ9QEwCHoECAkQQA#imgrc=Izk9xz_wgvai-M")

