from static.styles import styles

def custom_header(title):
    return styles.HEADER_STILE + f"""<div class="custom-header"><h2>{title}</h2></div>"""


def custom_footer():
    html_content = """
            class="custom-footer">
            <p>Creadores:</p>
            <a href="https://www.linkedin.com/in/pablo-oller-perez-7995721b2" target="_blank">Pablo Oller Pérez</a><br>
            <a href="https://www.linkedin.com/in/pablo-oller-perez-7995721b3" target="_blank">Pablo Santos Quirce</a><br>
            <a href="https://www.linkedin.com/in/pablo-oller-perez-7995721b2" target="_blank">Alejandro Castillo Carmona</a>
        </div>
        """
    return styles.FOOTER_STILE + html_content


def custom_title():
    return styles.TITLE_STILE

def custom_width():
    return styles.WIDTH_STILE