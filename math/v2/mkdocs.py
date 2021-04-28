from importlib import import_module as imp
from os import listdir
from os.path import isfile, join
import md_toc

ignores = ["mkdocs.py", "util.py", "template.py"]

path = "."
files = [f for f in listdir(path) if isfile(join(path, f))]

docs = []

docfiles = {}

for file in files:
    if file in ignores: continue

    module = imp(file.replace(".py", ""))

    docs += [module.doc]
    docfiles[file] = module.doc

# Full Docs:
docs = "\n---\n\n".join(docs)
docs = "# Math Docs\n___\n\n" + "<TOC>\n\n___\n\n" + docs
with open("./docs/index.md", "w+") as file:
    file.write(docs)
docs = docs.replace("<TOC>", md_toc.build_toc('./docs/index.md'))
with open("./docs/index.md", "w+") as file:
    file.write(docs)

# File Docs:
for file, filedoc in docfiles.items():
    filename = file.replace(".py", "") + ".md"
    with open(f"./docs/{filename}", "w+") as f:
        f.write(filedoc)
    filedocs = filedoc.replace("<TOC>", md_toc.build_toc(f"./docs/{filename}"))
    with open(f"./docs/{filename}", "w+") as f:
        f.write(filedocs)
