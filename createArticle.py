import os
import datetime 
import shutil
from PIL import Image

PATH = os.path.dirname(os.path.abspath(__file__))

def createArticle(cat, title, author, text, filePath):
    with open(os.path.join(PATH, "html", "article.html")) as html:
        article = html.read()
        dates = datetime.date.today().strftime("%d-%m-%Y")
        times = str(datetime.datetime.now()).replace(":","").replace(".","")
        nText = ""
        for line in text.splitlines():
            nText += f"<p>{line}</p>"
        article = article.replace("==CAT==", cat)
        article = article.replace("==TITLE==", title)
        article = article.replace("==AUTHOR==", author)
        article = article.replace("==DATE==", dates)
        article = article.replace("==TEXT==", nText)
        title = title.replace(" ","-")
        path = f"{dates}-{times}.html".replace(" ","")

        spotHtml = '<div class="grid-item"><article class="article"><div class="card">==IMG==<div class="card-body text-center px-1"><a href="==HREF==" class="text-title display-1 text-dark">==TITLE==</a><p class="secondary-title text-secondary display-3"><span><i class="far fa-clock text-primary"></i>    ==DATE==</span></p></div></div></article></div>'
        spotHtml = spotHtml.replace("==TITLE==", title)
        spotHtml = spotHtml.replace("==HREF==", f"articles/{path}")
        spotHtml = spotHtml.replace("==DATE==", dates)
        ImageHeight = Image.open(newFilePathV).height
        spotHtml = spotHtml.replace("==PAD==", 100/(280/ImageHeight))
        
        try:
            ext = filePath.split(".")[1]
            newFilePath = os.path.join(PATH, "images", rf"{dates}-{times}.{ext}".replace(" ",""))
            newFilePathV = f"../images/{dates}-{times}.{ext}".replace(" ","")
            shutil.copy(filePath, newFilePath)
            article = article.replace("==IMG==", f'<div class="thumbnail mt-3"><img src="{newFilePathV}" class="thumbnail" alt=""></div>')
            spotHtml = spotHtml.replace("==IMG==", f'<div class="overflow-img"><a href="articles/{path}"><img src="{newFilePathV}" class="img-fluid" alt=""></a></div>')
        except:
            spotHtml = spotHtml.replace("==IMG==", "")
            article = article.replace("==IMG==", "")

        with open(os.path.join(PATH, "articles.txt"), "a") as spots:
            spots.write(spotHtml)

        newArticle = open(os.path.join(PATH, "articles", path), 'w')
        newArticle.write(article)
        newArticle.close()
        return True
