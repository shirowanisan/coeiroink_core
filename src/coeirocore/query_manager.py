from typing import List

from src.coeirocore.model import AudioQuery


def query2tokens_prosody(query: AudioQuery) -> List[str]:
    tokens = ['^']
    for i, accent_phrase in enumerate(query.accent_phrases):
        up_token_flag = False
        for j, mora in enumerate(accent_phrase.moras):
            if mora.consonant:
                tokens.append(mora.consonant.lower())
            if mora.vowel == 'N':
                tokens.append(mora.vowel)
            else:
                tokens.append(mora.vowel.lower())
            if accent_phrase.accent == j + 1 and j + 1 != len(accent_phrase.moras):
                tokens.append(']')
            if accent_phrase.accent - 1 >= j + 1 and up_token_flag is False:
                tokens.append('[')
                up_token_flag = True
        if i + 1 != len(query.accent_phrases):
            if accent_phrase.pause_mora:
                tokens.append('_')
            else:
                tokens.append('#')
    try:
        if query.accent_phrases[-1].is_interrogative:
            tokens.append('?')
        else:
            tokens.append('$')
    except IndexError:
        tokens.append('$')
    return tokens
