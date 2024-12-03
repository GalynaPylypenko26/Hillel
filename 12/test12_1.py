def delete_html_tags(input_file='draft.html', output_file='cleaned.txt'):
    """
    Видалення html-тегів без прибирання рядків, в яких немає інформації.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned_content = []
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_content.append(char)

    cleaned_content = ''.join(cleaned_content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)


delete_html_tags()
