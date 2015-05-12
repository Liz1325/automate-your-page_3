def generate_concept_HTML(concept_title, concept_description):
    html_text_1='''
<div class="concept">
    <div class="concept-title">
    '''+ concept_title
    html_text_2 ='''
</div>
<div class="concept-description">
'''+ concept_description
    html_text_3='''
</div>
</div>'''
    full_html_text=html_text_1+html_text_2+html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title=concept[0]
    concept_description=concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML=""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

example_list_of_concepts=[['How the Web Works','The Web is a system of interlinked hypterxt documents.'],
                  ['HTML','HTML stand for Hyptext Markup Language.'],
                  ['Tags and Elements','HTML documents are made up oof HTML elements.'],
                  ['Why Computers are Stupid','Computers are stupid because they interpet instructions iterally.'],
                  ['Inline vs. Block Elements','HTML elements are either inline or block.']]

print make_HTML_for_many_concepts (example_list_of_concepts)
