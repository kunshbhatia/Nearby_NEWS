from flask import Flask,render_template,request
from getting_NEWS import basic_format
from reading_NEWS import writing_info

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home_page():
    try:
        if request.method == "POST":
            name = request.form['name']
            country = request.form['country']
            language = request.form['language']

            basic_format(language,country)
            writing_info()

            with (
                open("txt_files/headings.txt","r",encoding="utf-8") as h,
                open("txt_files/content.txt","r",encoding="utf-8") as c,
                open("txt_files/urls.txt","r",encoding="utf-8") as u,
                open("txt_files/images.txt","r",encoding="utf-8") as i
            ):
                headlines=h.readlines()
                contents =c.readlines()
                urls=u.readlines()
                image=i.readlines()

            news_list = []
            for head, con, ur,img in zip(headlines, contents, urls,image):
                news_list.append({
                    "title": head.strip(),
                    "content": con.strip(),
                    "url": ur.strip(),
                    "image":img.strip()
                })

            return render_template("Welcome_Page.html",name=name,country=country,language=language,news=news_list)
    except:
        return render_template("Error.html")
    return render_template("Asking_Name.html")


if __name__ == "__main__":
    app.run(debug=True)