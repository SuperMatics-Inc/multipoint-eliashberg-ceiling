"""Admit immutable source pins, replay an isolated copy and build its paper.
The source manifest is separately hashed by the caller. No outward action.
"""
from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import pymupdf

parser=ArgumentParser(description=__doc__)
parser.add_argument('--manifest-sha256',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parent.parent
manifest_bytes=(root/'SOURCE-PINS.json').read_bytes()
if sha256(manifest_bytes).hexdigest()!=args.manifest_sha256:
 raise SystemExit('REJECT: externally admitted source manifest')
manifest=json.loads(manifest_bytes)
print('ADMITTED source manifest',args.manifest_sha256,flush=True)
base=Path('D:/t/UNIV-GLUE')
base.mkdir(parents=True,exist_ok=True)

with tempfile.TemporaryDirectory(prefix='optimum2-clean-',dir=base) as temporary:
 clean=Path(temporary)
 for name,pin in manifest['members'].items():
  rel=Path(name)
  if rel.is_absolute() or '..' in rel.parts:
   raise SystemExit('REJECT: manifest member path')
  source=root/rel
  raw=source.read_bytes()
  if len(raw)!=pin['bytes'] or sha256(raw).hexdigest()!=pin['sha256']:
   raise SystemExit('REJECT: source member '+name)
  target=clean/rel
  target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(source,target)
  copied=target.read_bytes()
  if len(copied)!=pin['bytes'] or sha256(copied).hexdigest()!=pin['sha256']:
   raise SystemExit('REJECT: copied member '+name)
 shutil.copyfile(root/'SOURCE-PINS.json',clean/'SOURCE-PINS.json')
 print('PASS raw-byte member admission and isolated copies:',len(manifest['members']),flush=True)
 command=[sys.executable,'-I','-B','OPTIMUM2/verify.py']
 result=subprocess.run(command,cwd=clean)
 print('EXIT',result.returncode,'COMMAND',command,flush=True)
 if result.returncode!=0:
  raise SystemExit('REJECT: clean exact replay')

 with pymupdf.open(clean/'main.pdf') as admitted:
  expected_text=[page.get_text() for page in admitted]
 (clean/'main.pdf').rename(clean/'admitted-main.pdf')
 command=['D:/dev/tools/tectonic/tectonic.exe','--only-cached','main.tex']
 result=subprocess.run(command,cwd=clean)
 print('EXIT',result.returncode,'COMMAND',command,flush=True)
 if result.returncode!=0 or not (clean/'main.pdf').is_file():
  raise SystemExit('REJECT: fresh clean paper build')
 with pymupdf.open(clean/'main.pdf') as rebuilt:
  actual_text=[page.get_text() for page in rebuilt]
 if actual_text!=expected_text:
  raise SystemExit('REJECT: rebuilt page text differs from admitted paper')
 print('PASS fresh PDF page-text identity:',len(actual_text),'pages',flush=True)
print('PASS: clean-copy replay, fourteen guarded mutants, finite Lean, fresh paper; owned temporary directory removed',flush=True)
