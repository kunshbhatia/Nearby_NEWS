import json

def writing_info():
    with open("txt_files/NEWS.txt","r",encoding="utf-8") as f:
        info = json.load(f)

    with open("txt_files/headings.txt","w",encoding="utf-8") as f:
        for i in info['articles']:
            f.write(i['title'].strip()+"\n")

    with open("txt_files/content.txt","w",encoding="utf-8") as f:
        for i in info['articles']:
            f.write(i['description'].strip()+"\n")

    with open("txt_files/urls.txt","w",encoding="utf-8") as f:
        for i in info['articles']:
            f.write(i['url'].strip()+"\n")

    with open("txt_files/images.txt","w",encoding="utf-8") as f:
        for i in info['articles']:
            f.write(i['image'].strip()+"\n")


    if len(info.get('articles', [])) == 0:
        raise Exception("No Info")