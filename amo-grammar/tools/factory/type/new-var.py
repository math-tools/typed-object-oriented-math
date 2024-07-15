from collections import defaultdict
from yaml        import safe_load as yaml_load

from mistool.string_use import between
from mistool.os_use     import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR  = Path(__file__).parent
THIS_FILE_NAME = Path(__file__).stem

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "amo-grammar"):
    SRC_DIR = SRC_DIR.parent

CFG_DIR = SRC_DIR / "grammar" / "type"

DOC_DIR      = SRC_DIR / "doc" / "fr" / "content" / "typing"
DOC_FILE     = DOC_DIR / f"{THIS_FILE_NAME}.txt"
DOC_DIAUTO = DOC_DIR / THIS_FILE_NAME

DOC_TAG_FORMAT = "// -- TYPES - AUTO - {where} -- //"
DOC_TAG_START  = DOC_TAG_FORMAT.format(where = "START")
DOC_TAG_END    = DOC_TAG_FORMAT.format(where = "END")



# ----------- #
# -- TOOLS -- #
# ----------- #

def extract():
    ...


def build_auto_doc(all_cgfs, all_sorting):
    from pprint import pprint;pprint(all_cgfs);pprint(all_sorting)


# --------------- #
# -- LET'S GO! -- #
# --------------- #

all_cgfs    = dict()
all_sorting = dict()

for cfgfile in CFG_DIR.rglob("*.amo.cfg"):
    context  = cfgfile.parent.parent - CFG_DIR
    category = cfgfile.parent.name

    if not context in all_cgfs:
        all_cgfs[context] = defaultdict(list)

    all_cgfs[context][category].append(cfgfile.name)

for sortfile in CFG_DIR.rglob("sorting.yaml"):
    with sortfile.open(
        mode     = "r",
        encoding = "utf-8"
    ) as f:
        all_sorting[sortfile.parent - CFG_DIR] = yaml_load(f)

build_auto_doc(all_cgfs, all_sorting)
