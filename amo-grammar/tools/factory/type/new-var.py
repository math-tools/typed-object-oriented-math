from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

KIND = "fundation"


THIS_DIR = Path(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "amo-grammar"):
    SRC_DIR = SRC_DIR.parent

CFG_DIR = SRC_DIR / "grammar" / KIND

DOC_DIR = (
    SRC_DIR
    / "doc" / "fr" / "content" / "types" / "new-var" / KIND
)


DOC_TAG_FORMAT = "// -- SIMPLE TYPES - AUTO - {kind} -- //"
DOC_TAG_START  = DOC_TAG_FORMAT.format(kind = "START")
DOC_TAG_END    = DOC_TAG_FORMAT.format(kind = "END")


# --------------- #
# -- LET'S GO! -- #
# --------------- #

for cfgfile in CFG_DIR.glob("*/*.amo.cfg"):
    print(cfgfile.parent.name, '/', Path(cfgfile.stem).stem)

for docfile in DOC_DIR.glob("*.txt"):
    print(docfile.stem)
