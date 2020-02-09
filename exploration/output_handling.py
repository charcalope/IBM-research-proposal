import re

exs = ['[ARG1: Cell cycle- and apoptosis - associated proteins] were [ARGM-MNR: semi] - [V: quantified] [ARG0: by Western Blotting] and breakdown of mitochondrial membrane potentials was detected by JC-1 staining .',
 'Cell cycle- and [ARG1: apoptosis] - [V: associated] [ARG1: proteins] were semi - quantified by Western Blotting and breakdown of mitochondrial membrane potentials was detected by JC-1 staining .',
 'Cell cycle- and apoptosis - associated proteins were semi - quantified by Western Blotting and [ARG1: breakdown of mitochondrial membrane potentials] was [V: detected] [ARG0: by JC-1 staining] .']

def parse_phrase(sentence):
    parse_list = []
    result = re.findall("([-\w]*): ([^\]]*)", sentence)
    for label, value in result:
       parse_list.append((label, value))
    if has_arg(parse_list):
        return parse_list

def join_parsed_phrase(parsed):
    p_list = []
    for (label, value) in parsed:
        p_list.append(value)
    phrase = ' '.join(p_list)
    return phrase

def has_arg(parsed_phrase):
    for (label, value) in parsed_phrase:
        if 'ARG' in label:
            return True

def no_overlap(all_parsed):
    phrases = [join_parsed_phrase(x) for x in all_parsed]
    phrases_helper = [(x, set(x.split())) for x in phrases]
    good_phrases = []

    for (phrase_on_trial, phrase_set) in phrases_helper:
        def mini_overlap():
            for (x, x_set) in phrases_helper:
                if (x is not phrase_on_trial) and (phrase_set.issubset(x_set)):
                    return False
            return True

        if mini_overlap():
            good_phrases.append(phrase_on_trial)

    return good_phrases

print(no_overlap([parse_phrase(x) for x in exs]))