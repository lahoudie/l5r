"""Runs locally after images have public HTTPS URLs. python GENERER_CSS_ROLL20.py"""
from pathlib import Path
import json,re
base=Path(__file__).parent
mapping=json.loads((base/'ASSETS_A_HEBERGER.json').read_text(encoding='utf8'))
for key,value in mapping.items():
 if not value.startswith('https://') or not re.match(r'^https://\S+\.(png|jpg|jpeg|webp)(?:\?\S*)?$',value,re.I):
  raise SystemExit(f'Missing/invalid HTTPS image URL: {key}. Fill all entries in ASSETS_A_HEBERGER.json.')
layer=(base/'ART_LAYER_TEMPLATE.css').read_text(encoding='utf8')
for k,v in mapping.items(): layer=layer.replace('__ASSET_'+k.upper().replace('-','_')+'__',v)
assert '__ASSET_' not in layer
basecss=(base/'L5R4e_V2_3_BASE.css').read_text(encoding='utf8')
p=base/'L5R4e_V2_3_ROLL20_COMPLET.css';p.write_text(basecss+'\n\n'+layer,encoding='utf8')
print('Fichier créé:',p)
