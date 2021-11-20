import re


pattP = re.compile(r"(.)([A-Z][a-z]+)")
pattF = re.compile("([a-z0-9])([A-Z])")


def get_tokens(text):
    """
    Obtener tokens de un string
    """
    regex = re.compile(r"%\w+%")
    result = regex.findall(text)
    if len(result) > 0:
        result = list(set(result))
        tokens = [w.replace("%", "") for w in result]
        return tokens
    else:
        return []


def to_pascal(text):
    """
    comvierte camel case en notacion pascal
    """
    return pattF.sub(r"\1_\2", pattP.sub(r"\1_\2", text)).lower()


def pascal_case(text):
    return "".join(x for x in text.title() if not x.isspace())


def blank_file(file_path):
    """
    Crea un archivo en blanco
    """
    open(file_path, "a").close()


class View:
    """
    View parse class
    """

    def __init__(self, template_path):
        # self.template_name = template_name
        self.template = open(template_path, "r").readlines()

    def build(self, data):
        result = []
        for line in self.template:
            tokens = get_tokens(line)
            if len(tokens) > 0:
                for token in tokens:
                    value = data.get(token, None)
                    if value != None:
                        token = "%" + token + "%"
                    try:
                        line = line.replace(token, value)
                    except TypeError:
                        print(
                            "Error al reemplazar:",
                            "\n\t",
                            line.strip(),
                            f"\n\t{token} -> {value}",
                        )
            result.append(line)
        return result

    def build_and_save(self, data, output_name):
        result = self.build(data)
        output = open(output_name, "w")
        for line in result:
            output.write(line)
        output.close()
