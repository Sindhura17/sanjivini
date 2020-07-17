import facebook

def publish_photo_msg(message, image_url):
    page_access_token="EAAH5vh5dbawBAB9HV2t4uIyMgl1catwaEZAh9TFr2wWs03HtRgmMiDC0NzB58bagcgwRh33TX7rlLmB1LPiJbbxGQ5FD3qcDwFh5rzNVK8KQgaVVgbifDLovofgW3b150srF0mOpuoyuNEDyRT5L607EbfhjUetJHpqj6nUWwzZCfgi3Ezn7vLyWwcPWQZD"
    graph = facebook.GraphAPI(page_access_token)
    photo = open(r"C:\Users\Spoorthi S\Desktop\img.png", "rb")
    graph.put_photo(photo,message="This is a message")
    #graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
    photo.close()