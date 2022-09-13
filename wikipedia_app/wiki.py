import wikipedia

wikipedia.set_lang('cz')

def get_random_wikipedia_article() -> str:
    return wikipedia.summary('https://en.wikipedia.org/wiki/Special:Random', 4)
