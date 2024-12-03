def delete_html_tags(input_file='draft.html', output_file='cleaned.txt'):
    """
    Видалення html-тегів з прибиранням рядків, в яких немає інформації.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned_content = []
    inside_tag = False
    current_line = []

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            if char == '\n':
                if ''.join(current_line).strip():
                    cleaned_content.append(''.join(current_line))
                current_line = []
            else:
                current_line.append(char)

    if ''.join(current_line).strip():
        cleaned_content.append(''.join(current_line))

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_content))


delete_html_tags()
