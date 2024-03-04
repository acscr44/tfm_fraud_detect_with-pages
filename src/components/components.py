from static.styles import styles

def custom_header(title):
    return styles.HEADER_STILE + f"""<div class="custom-header"><h2>{title}</h2></div>"""
