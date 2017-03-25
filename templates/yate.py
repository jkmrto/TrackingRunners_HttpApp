from string import Template


def start_response(resp="text/html"):
    return ('Content-type: ' + resp + '\n\n')


def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return (header.substitute(title=the_title))


def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return (footer.substitute(links=link_string))


def start_form(the_url, form_type="POST"):
    return ('<form action="' + the_url + '" method="' + form_type + '">')


def end_form(submit_msg="Submit"):
    return ('<p></p><input type=submit value="' + submit_msg + '"></form>')


def radio_button(rb_name, athlete_name, athlete_ID):
    """
    It selecte the athlete ID
    :param rb_name:
    :param athlete_name:
    :param athlete_ID:
    :return:
    """
    return ('<input type="radio" name="' + rb_name +
            '" value="' + str(athlete_ID) + '"> ' + str(athlete_ID) + ', ' + athlete_name + '<br />')


def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return (u_string)


def header(header_text, header_level=2):
    return ('<h' + str(header_level) + '>' + header_text +
            '</h' + str(header_level) + '>')

def para(para_text):
    return ('<p>' + para_text + '</p>')


def text_field(tf_name, tf_value, tf_size=30, tf_maxlength=30):
    return ('<input type="text" name="' + tf_name + '" value="' + tf_value +
            '" size="' + str(tf_size) + '" maxlength="' + str(tf_maxlength) + '" ><br>')


def hidden_input(tf_name, tf_value, tf_size=30, tf_maxlength=30):

    return ('<input type="hidden" name="' + tf_name + '" value="' + tf_value +
            '" size="' + str(tf_size) + '" maxlength="' + str(tf_maxlength) + '" >')


def simple_plot(path):
    return ('<img src="{}">'.format(path))

def simple_table(table):
    print("<table>")

    for row in table:
        print("<tr>")
        for cell in row:
            if isinstance(cell, float):
                string = "{0:.3f}".format(cell)
            else:
                string = str(cell)
            print("<td>" + string + "</td>")
        print("</tr>")

    print("</table>")

