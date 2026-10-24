from pathlib import Path
import argparse, hashlib, json, re
p=argparse.ArgumentParser();p.add_argument("binary");p.add_argument("output");a=p.parse_args()
b=Path(a.binary).read_bytes();expected="ffb64331bc0ee1b69efb7c2c428bd3ab516bc31b75bf60886b356c97c1c25ffd"
assert hashlib.sha256(b).hexdigest()==expected,"Different binary; this report does not apply"
o=Path(a.output);o.mkdir(parents=True,exist_ok=False);rows=[]
for k,m in enumerate(re.finditer(rb"// @bun @bytecode\n",b)):
 s=m.start();e=b.find(b"\x00",s);v=b[s:e]
 try:v.decode("utf-8")
 except UnicodeDecodeError:continue
 name=f"module-{k:03d}.js";(o/name).write_bytes(v)
 rows.append(dict(file=name,binary_start=s,binary_end_exclusive=e,bytes=len(v),sha256=hashlib.sha256(v).hexdigest()))
(o/"manifest.json").write_text(json.dumps(rows,indent=2))
print("Extracted",len(rows),"candidates. module-000 is a runtime template, excluded by analysis.")
