from wikipedia_app import app

from flask import render_template, request
from wikipedia_app import wiki

from wikipedia_app.wiki import get_random_wikipedia_article
from datetime import date

@app.route('/', methods=["GET", "POST"])
def index() -> render_template:
    wiki_result = None
    success = None
    show_text_div = False

    if  request.method == "POST":
        search_query = request.form['query']
        sentences = request.form['sentences']
        language = request.form['language']

        wiki_result = get_random_wikipedia_article(search_query, language, int(sentences))

        print(wiki_result)

        if (wiki_result[-1] == True):
            success = True
        elif (wiki_result[-1] == False):
            success = False
        elif (wiki_result[-1] == 'not_found'):
            success = 'not_found'
    

        show_text_div = True
        wiki_result = wiki_result[0]



    return render_template('index.html',
                            date=date.today().year,
                            wiki_result=wiki_result,
                            success=success,
                            show_text_div=show_text_div)
