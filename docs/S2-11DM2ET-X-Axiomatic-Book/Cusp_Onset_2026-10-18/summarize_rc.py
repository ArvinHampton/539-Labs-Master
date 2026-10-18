import json, sys
for fn in sys.argv[1:]:
    for r in json.load(open(fn)):
        print(r['s'], 'M=%d' % r['M'], r['cyc'], '|G|=%d' % r['G'], '|K_N|=%d' % r['K_N'], '|H|=%d' % r['H'], 'cnt_dev=%s' % r['count_check_maxdiff'], '->', r['uL_verdict'], 'nongenus pure chars (complete parts) =', r['uL_nongenus_pure_chars_complete'])
        for c in r['cparts']: print('    c=%s Nc=%d |T|=%d obs=%d complete=%s genus_pure=%s genus_mixed=%s ng_pure=%s orders=%s' % (c['c'], c['Nc'], c['n_classes'], c['observable_classes'], c['complete'], c.get('genus_pure'), c.get('genus_mixed'), c.get('nongenus_pure_chars'), c.get('nongenus_pure_char_orders')))
