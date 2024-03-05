import static.styles.css_styles as css
# from static.styles.styles import FOOTER_STYLE

def custom_header(title):
    return css.HEADER_STILE + f"""<div class="custom-header"><h2>{title}</h2></div>"""


def custom_footer():
    html_content = css.FOOTER_STYLE + f"""
        <div class="custom-footer">
            <p>Creadores:</p>
            <a href="https://www.linkedin.com/in/pablo-oller-perez-7995721b2" target="_blank">Pablo Oller Pérez</a><br>
            <a href="https://github.com/pabloquirce23" target="_blank">Pablo Santos Quirce</a><br>
            <a href="https://github.com/acscr44" target="_blank">Alejandro Castillo Carmona</a>
        </div>
        """
    return html_content


def custom_title():
    return css.TITLE_STILE

def custom_width():
    return css.WIDTH_STILE