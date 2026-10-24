import markdown,subprocess,os,re
for name in ('LEDGER','INDEX'):
    md=open(name+'.md').read()
    if name=='LEDGER': md=re.sub(r'^(\d+)\. \*\*',lambda m:'- **%s.** **'%m.group(1),md,flags=re.M)
    parts=md.split('`')
    for i in range(0,len(parts),2): parts[i]=parts[i].replace('_','\\_')
    md='`'.join(parts)
    css='body{font-family:DejaVu Sans,Arial;font-size:9.5pt;max-width:900px;margin:auto}table{border-collapse:collapse;font-size:7.5pt;margin:6px 0}td,th{border:1px solid #999;padding:2px 4px}code{font-size:8pt}ul{list-style:none;padding-left:0}ul ul{list-style:disc;padding-left:1.6em}li{margin-bottom:6px}'
    open('/tmp/%s_v8.html'%name,'w').write('<html><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+markdown.markdown(md,extensions=['tables'])+'</body></html>')
    subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--print-to-pdf='+os.getcwd()+'/'+name+'.pdf','--no-pdf-header-footer','file:///tmp/%s_v8.html'%name],stderr=subprocess.DEVNULL)
