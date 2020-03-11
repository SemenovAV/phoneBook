def adv_print(*args, **kwargs):
    start = kwargs.get('start', '')
    max_line = int(kwargs.get('max_line', False))
    in_file = kwargs.get('in_file', False)
    strings = list(args)

    def get_lines(words):
        length = len(start)
        result = []
        for string in words:
            lines = []
            for item in str(string).split(' '):
                length += len(item)
                if max_line and length > max_line - 1:
                    length = 0
                    lines.append('\n')
                    lines.append(item)
                else:
                    lines.append(item)
            lines = ''.join(lines) if lines[0] == '\n' else ' '.join(lines)
            result.append(start + lines)
        return result

    print(*get_lines(strings), **kwargs)
    if in_file:
        with open(f'{in_file}', 'w', encoding='utf8') as f:
            print(*get_lines(strings), file=f)
