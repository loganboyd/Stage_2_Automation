
def generate_header_HTML(page_title, section_heading):
    html_head_1 = '''
 <!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="Style.css">
    <title>Logan Boyd</title>
  </head>
<body>
  <div class="intro">
 ''' + page_title
    html_head_2 = '''
  </div>
  <div class="heading">
        <h2>''' + section_heading
    html_head_3 = ''' </h2>
    </div>'''
    full_html_header = html_head_1 + html_head_2 + html_head_3
    return full_html_header


HEAD_TEXT = ['INTRO TO PROGRAMMING', 'Stage 2']

def make_header(header_one):
    page_title = HEAD_TEXT[0]
    section_head = HEAD_TEXT[1]
    return generate_header_HTML(page_title, section_head)



def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
  <div class="stage">
    <div class="topic">
        <h3>''' + concept_title
    html_text_2 = '''</h3>
    <p>
        ''' + concept_description
    html_text_3 = '''
    </p>
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

LOGANS_NOTES = [ ['Intro to Programming', 'Computers through use of programs is a universal machine and can do a lot of useful things. <br> A program tells the computer what to do. <br>  Interpreter is an application that allows you to run other applications. For example Python is an application and application can be written in the python language to make an application. <br> Python is a single programming language <br> Full notes, HTML and CSS foud at insert link'],
                 ['Variables and Strings', 'What is the difference in a variable and a String<br> Variables must be defined first using a variable name and an equals value <br> A String can be defined without a name <br>Indexing Strings Indexes start at zero <br> How to use <b>Find</b> Find is a procedure which is built into python.'],
                 ['Input > Function > Output', '<b>Functions</b> are used to take an input, preform and action, and return an output <br> to make a function start the line with def followed by the function name and parameters. <br> To use a function, we write the name of the function followed by the value(s) we want to give it in parentheses.'],
                 ['Decisions and Repetition: If and While', 'If statements are used to test a comparison <br> <b>While Loops</b> continue a set action as long as the statement is ture. '],
                 ['Structured Data: Lists and For Loops', '<b>Lists</b> are a way to capture data. <br> functions can be placed around the data to produce specific outputs as defined <br> Mutation means we can change the value of a list once created. <br><b> Aliasing</b> allows you to assign a new variable to an existing list that may already have a variable name. <b> For Loops</b> use the <b>for</b> command to loop though a set input and perform a function on the entire set.']]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_header(HEAD_TEXT)
print make_HTML_for_many_concepts(LOGANS_NOTES)
