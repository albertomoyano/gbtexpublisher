import re
import argparse
from pathlib import Path 

def read(path):
  print(f"{path}:")
  try:
    return path.read_text()
  except Exception:
    print(f"  Error al abrir")
    
def get_line(index, text):
  rx = re.compile(r'\n')
  lines = [l.span() for l in rx.finditer(text)]
  for i, ln in enumerate(lines, start=1):
    if index in range(*ln):
      return i

def check(text):
  rx = re.compile(r'\\(begin|end).*?\{(.+?)\}')
  matches = list(rx.finditer(text))
  pairs = [m.groups() for m in matches]
  for match in matches:
    tag1, env = match.groups()
    tag2 = "begin" if tag1 == "end" else "end"
    if (tag2, env) not in pairs:
      ini, fin = match.span()
      line = f"  Línea {get_line(fin, text)}:"
      mark = text[ini:fin]
      print(line, f"Falta '{tag2}' para {mark}")

cli = argparse.ArgumentParser()
cli.add_argument("paths", type=Path, nargs="+")
args = cli.parse_args()
texts = map(lambda p: read(p), args.paths)
[check(text) for text in texts if text]