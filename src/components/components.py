from static.styles import styles

def custom_header(title):
    return styles.HEADER_STILE + f"""<div class="custom-header"><h2>{title}</h2></div>"""


def custom_footer():
    return styles.FOOTER_STILE + f"""<div class="custom-footer"><p>© 2024 - TFM IABD</p></div>"""


def custom_title():
    return styles.TITLE_STILE + f"""<div class="centered"><h1>{title}</h1></div>"""

def custom_width():
    return styles.WIDTH_STILE