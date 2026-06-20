from pylatexenc.latexencode import unicode_to_latex
import re

OK_CHARS = r"[0-9a-zA-Z\[\]{}\.\,\?!'\-_\*\(\)\\/:;\s\n@=%$#+&]"
def main():
    out = ""
    with open("references.bib", 'r', encoding="utf-8") as file:
        for c in file.read():
            if re.match(OK_CHARS, c):
                out += c
            else:
                out += f"{{{unicode_to_latex(c)}}}"

    with open("references.bib", 'w', encoding="utf-8") as file:
        file.write(out)

if __name__ == "__main__":
    main()