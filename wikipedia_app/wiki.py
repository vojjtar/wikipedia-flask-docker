import wikipedia

def get_random_wikipedia_article(search_query: str, language: str, sentences: int) -> str:
    wikipedia.set_lang(language)
    try:
        return wikipedia.summary(search_query, sentences=sentences, auto_suggest=True), True
    except wikipedia.exceptions.DisambiguationError as e:
        return e.args, False
    except wikipedia.exceptions.PageError as e:
        return e.args, 'not_found'

