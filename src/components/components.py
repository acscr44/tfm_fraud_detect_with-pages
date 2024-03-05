from static.styles.css_styles import *


def custom_header(title):
    return TITLE_STILE + f"""<div class="custom-header"><h1 class='title'>{title}</h1></div>"""


def custom_footer():
    html_content = (
    FOOTER_STYLE +
    "<div class=\"custom-footer\">" +
        "<p>Creadores:</p>" +
        "<a href=\"https://www.linkedin.com/in/pablo-oller-perez-7995721b2\" target=\"_blank\">Pablo Oller Pérez</a><br>" +
        "<a href=\"https://github.com/pabloquirce23\" target=\"_blank\">Pablo Santos Quirce</a><br>" +
        "<a href=\"https://github.com/acscr44\" target=\"_blank\">Alejandro Castillo Carmona</a>" +
    "</div>"
    )
    
    # Otra forma de hacerlo:
    # html_content_2 = f"""
    #     {FOOTER_STYLE}
    #     <div class="custom-footer">
    #         <p>Creadores:</p>
    #         <a href="https://www.linkedin.com/in/pablo-oller-perez-7995721b2" target="_blank">Pablo Oller Pérez</a><br>
    #         <a href="https://github.com/pabloquirce23" target="_blank">Pablo Santos Quirce</a><br>
    #         <a href="https://github.com/acscr44" target="_blank">Alejandro Castillo Carmona</a>
    #     </div>
    # """.strip().replace('\n', '')
    return html_content


def custom_title(title):
    return TITLE_STILE + f"""<div class="title"><h1 class='title'>{title}</h1></div><br>"""

def custom_width():
    return WIDTH_STILE