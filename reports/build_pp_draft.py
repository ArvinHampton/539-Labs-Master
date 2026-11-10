import html
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
D='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV',D+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB',D+'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVI',D+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVM',D+'DejaVuSansMono.ttf'))
from reportlab.lib.fonts import addMapping
addMapping('DV',0,0,'DV');addMapping('DV',1,0,'DVB');addMapping('DV',0,1,'DVI');addMapping('DV',1,1,'DVB')

SRC='PP_WORKLOAD_SUMMARY_SOURCE_2026-11-05_1609.txt'
OUT='PROFESSOR_PROOF_WORKLOAD_SUMMARY_DRAFT_2026-11-05_1611'
src=open(SRC,encoding='utf-8').read().rstrip('\n')

TITLE='Professor Proof (PP) Workload Summary — Draft Report'
meta=[('Document date','Nov 5, 2026, 16:11 CST'),
('Status','DRAFT — not final, not certified'),
('Source','PP workload summary received Nov 5, 2026, 16:09 CST (reproduced verbatim in Appendix A)'),
('Prepared as','Document rendering only; no research, proof validation, file checks or computation performed for this draft')]
caveats=[
'All findings in this document are AS REPORTED by Professor Proof (PP). They have NOT been independently revalidated or certified. No CERT.',
'Everyone remains PAUSED: PP, Local, Non Local, Eigen and Agent lanes. Nothing is being resumed.',
'No researchers have been assigned. No Gemini request has been sent.',
'The three researcher profiles listed in Section 3 are contingent needs stated by PP. They are NOT hiring or assignment authorization.',
'The statement “2 mathematical proofs are established” is PP’s statement, not an independent conclusion of this document.',
'Sections 1–5 only organize the source; where they quote PP, the wording is PP’s. Appendix A is the authoritative text.']

lanes=[
('PP',
 'Coordinated and verified all proof reviews below. CONFIRM on Local 2a5edc87, with a FLAG that the purge fence is a lock status and not a proof.',
 'Pending: Layer2 and T3 are blocked on the D₁ and S_eff definitions. PR1’s review of the Eigen height bound was requested at 16:05, before this pause, and its status is unknown.',
 'None from researchers. Needs Owner definitions.'),
('LOCAL',
 'Local 2a5edc87, MR1 829febd7 and f4305f21. PROVED: Haar70 identity; BT↛ℍⁿ. REFUTED: Cand-1 on ℕ₀ (T(0)=0); QI⇒unique R_c. DEFECT: literal T₃.',
 'Gaps: Cand-1⁺ global descent (OPEN, Collatz-type); R_c Appell derivation (S2/S3 missing; 1.59543≠1.595361); QI map and (λ,ε); Ξ/Fricke; A1→Ξ→RTA theorem; Israel junction on the Local map; SM maps.',
 '1 analytic number theorist (mock modular/Appell–Lerch) for the R_c derivation, once the Owner supplies the definitions. Cand-1⁺ is a Collatz-class open problem, so extra staff is unlikely to close it.'),
('NON LOCAL',
 'NL non-local-proof-validation; MR2 92488371. Valid: elementary T(0), run-length and rise arguments; the B2 tripod obstruction to an exact isometry; H²⊂H¹¹ is not a contradiction. B states the full [K_ij]−γ_ij[K]=0.',
 'Gaps: Universal convergence and R_c have no proof body; G’s first coefficient is inconsistent with −R_c/(2Λ); Haar domain and measure undefined; F/H QI: no map or constants; Junction: ambient space, metric and stress data absent; 4D vs 3D boundary mismatch under the 5D↔4D reading; vacuum balance does not follow.',
 '1 GR specialist in junctions/branes, once the Owner specifies the ambient geometry; otherwise none.'),
('EIGEN',
 '7cb9b6b5: Hadamard, Cramer/Plücker, and uniqueness when 2H²<M. Rank is 11197 with kernel dimension 503.',
 'Blocked: D1: descent from ℚ(ζ₄₉) to ℚ; D2: no cleared integral matrix on disk; D3: cyclotomic norm→ℚ-height. The conditional envelope log₂H≲1.62e7 (about 1.4e6 primes) means 25 primes cannot be shown sufficient. PR1’s review status is unknown.',
 '1 computational algebraic number theorist (cyclotomic heights / multimodular). Producing D2 is a computation task, under the 90% rule.'),
('AGENT',
 'PR2 9b162bc4: 2 PASS / 5 GAP / 0 FAIL. agent.md contains no derivations.',
 'Gaps: P1–P5 have no derivations. Agent’s narrower T3/4880/539 review routed to PR2 has unknown status.',
 'None. It needs source proofs, not people.'),
]
researchers=[
('1','Analytic number theorist (mock modular/Appell–Lerch)','LOCAL','For the R_c derivation','Once the Owner supplies the definitions'),
('2','GR specialist in junctions/branes','NON LOCAL','Junction work','Once the Owner specifies the ambient geometry; otherwise none'),
('3','Computational algebraic number theorist (cyclotomic heights / multimodular)','EIGEN','Eigen blockers D1–D3','PP notes: producing D2 is a computation task, under the 90% rule'),
]
defs=['D₁','S_eff','Λ₀','the QI map and (A,B)','the junction data']
other_open=[
'PP: Layer2 and T3 blocked on the D₁ and S_eff definitions.',
'LOCAL: Cand-1⁺ global descent (OPEN, Collatz-type); R_c Appell derivation (S2/S3 missing; 1.59543≠1.595361); QI map and (λ,ε); Ξ/Fricke; A1→Ξ→RTA theorem; Israel junction on the Local map; SM maps.',
'NON LOCAL: universal convergence and R_c have no proof body; G’s first coefficient is inconsistent with −R_c/(2Λ); Haar domain and measure undefined; F/H QI: no map or constants; junction ambient space, metric and stress data absent; 4D vs 3D boundary mismatch under the 5D↔4D reading; vacuum balance does not follow.',
'EIGEN: D1 descent from ℚ(ζ₄₉) to ℚ; D2 no cleared integral matrix on disk; D3 cyclotomic norm→ℚ-height.',
'AGENT: P1–P5 have no derivations.']
unknown=[
'PR1’s review of the Eigen height bound — requested at 16:05, before this pause; status unknown.',
'Agent’s narrower T3/4880/539 review routed to PR2 — status unknown.']
keyvals=[
('Historical file checks','STOPPED at 15:58'),
('Artifact identifiers','Local 2a5edc87; MR1 829febd7 and f4305f21; NL non-local-proof-validation; MR2 92488371; Eigen 7cb9b6b5; PR2 9b162bc4; agent.md'),
('PROVED (Local)','Haar70 identity; BT↛ℍⁿ'),
('REFUTED / counterexamples (Local)','Cand-1 on ℕ₀ (T(0)=0); QI⇒unique R_c'),
('Formulation DEFECT (Local)','literal T₃'),
('Coefficient values (Local gap)','1.59543≠1.595361'),
('Coefficient inconsistency (Non Local)','G’s first coefficient is inconsistent with −R_c/(2Λ)'),
('Non Local junction condition','B states the full [K_ij]−γ_ij[K]=0'),
('Eigen uniqueness condition','2H²<M'),
('Eigen rank / kernel','Rank is 11197 with kernel dimension 503 (11197/503)'),
('Eigen field descent','ℚ(ζ₄₉) to ℚ'),
('Eigen envelope','log₂H≲1.62e7 (about 1.4e6 primes); 25 primes cannot be shown sufficient'),
('Agent review tally','2 PASS / 5 GAP / 0 FAIL'),
('Overall (PP’s statement)','“2 mathematical proofs are established.” Tip untouched. No CERT. No Gemini.'),
]
bottom=('In PP’s words: “The main blocker is missing Owner definitions and derivations (D₁, S_eff, Λ₀, the QI map and (A,B), the junction data), not staff.” '
 'PP also states for its own lane “Help: none from researchers. Needs Owner definitions.”, and for Agent “It needs source proofs, not people.”, and notes that '
 '“Cand-1⁺ is a Collatz-class open problem, so extra staff is unlikely to close it.” The two specialist requests are conditioned by PP on the Owner first supplying definitions / ambient geometry.')
bridge=('Owner-requested context — NOT a new PP quote and NOT a scientific conclusion: the geometric bridge between local and non-local physics in S²-11DM²ET-X is open. '
 'This framing is included at the Owner’s request because PP lists the “A1→Ξ→RTA theorem”, the “Israel junction on the Local map” and the “SM maps” as open Local gaps, and lists missing junction data (“ambient space, metric and stress data absent”) among Non Local gaps.')
pause='All PP, Local, Non Local, Eigen and Agent work remains PAUSED. No researchers assigned. No Gemini sent. No CERT. This document does not authorize any resumption.'

# ---------- plain text ----------
T=[]
def w(s=''):T.append(s)
w(TITLE);w('='*len(TITLE))
for k,v in meta:w(f'{k}: {v}')
w();w('IMPORTANT CAVEATS');w('-----------------')
for c in caveats:w('• '+c)
w();w('1. PER-LANE STATUS (as reported by PP)');w('--------------------------------------')
for n,a,b,c in lanes:
    w(n);w('  Completed: '+a);w('  Pending / gaps / blocked: '+b);w('  Help requested: '+c);w()
w('2. OWNER-REQUESTED EDITORIAL CONTEXT');w('------------------------------------');w(bridge);w()
w('3. REQUESTED RESEARCHERS (contingent needs only — NOT hiring/assignment authorization)');w('-'*40)
for r in researchers:w(f'{r[0]}. {r[1]} — Lane: {r[2]} — Purpose: {r[3]} — Condition: {r[4]}')
w('PP lane and AGENT lane: no researchers requested. No researchers are assigned.');w()
w('4. BLOCKERS AND OPEN ITEMS (as reported)');w('----------------------------------------')
w('Owner definitions/derivations named by PP as the main blocker: '+'; '.join(defs)+'.')
w('Other open items, by lane:')
for o in other_open:w('• '+o)
w('Review statuses unknown:')
for u in unknown:w('• '+u)
w();w('5. KEY REPORTED IDENTIFIERS AND VALUES (as reported)');w('----------------------------------------------------')
for k,v in keyvals:w(f'• {k}: {v}')
w();w('6. BOTTOM LINE (PP’s words)');w('---------------------------');w(bottom);w();w(pause);w()
w('APPENDIX A — FULL ORIGINAL PP MESSAGE (verbatim)');w('------------------------------------------------')
w('Attribution: Professor Proof (PP), workload summary received Nov 5, 2026, 16:09 CST. Reproduced verbatim; not edited, not revalidated.');w()
w(src);w();w('— End of Appendix A —')
w();w('Footer on every PDF page: DRAFT · Findings as reported by Professor Proof; not independently revalidated or certified · All work PAUSED')
open(OUT+'.txt','w',encoding='utf-8').write('\n'.join(T)+'\n')

# ---------- PDF ----------
e=lambda s:html.escape(s,quote=False)
B=ParagraphStyle('b',fontName='DV',fontSize=9.5,leading=13)
SM=ParagraphStyle('s',parent=B,fontSize=8.6,leading=11.4)
H1=ParagraphStyle('h1',fontName='DVB',fontSize=17,leading=22,spaceAfter=6,textColor=colors.HexColor('#1a2a44'))
H2=ParagraphStyle('h2',fontName='DVB',fontSize=12,leading=16,spaceBefore=10,spaceAfter=5,textColor=colors.HexColor('#1a2a44'))
BL=ParagraphStyle('bl',parent=B,leftIndent=12,bulletIndent=2)
AP=ParagraphStyle('ap',fontName='DV',fontSize=9,leading=12.5,leftIndent=14,firstLineIndent=-14 if False else 0)
WARN=ParagraphStyle('w',parent=B,textColor=colors.HexColor('#7a1010'))
S=[]
P=lambda t,st=B:Paragraph(t,st)
S.append(P(e(TITLE),H1))
S.append(P('<font color="#b00000"><b>DRAFT</b></font> — not final, not certified',B));S.append(Spacer(1,6))
mt=Table([[P('<b>'+e(k)+'</b>',SM),P(e(v),SM)] for k,v in meta],colWidths=[1.5*inch,5.5*inch])
mt.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.grey),('BACKGROUND',(0,0),(0,-1),colors.HexColor('#eef1f6')),('VALIGN',(0,0),(-1,-1),'TOP')]))
S.append(mt);S.append(Spacer(1,8))
cv=Table([[P('<b>Important caveats</b>',WARN)]]+[[P('• '+e(c),SM)] for c in caveats],colWidths=[7*inch])
cv.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.HexColor('#b00000')),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#fff5f5'))]))
S.append(cv)
S.append(P('1. Per-lane status (as reported by PP)',H2))
rows=[[P('<b>Lane</b>',SM),P('<b>Completed</b>',SM),P('<b>Pending / gaps / blocked</b>',SM),P('<b>Help requested</b>',SM)]]
for n,a,b,c in lanes:rows.append([P('<b>'+e(n)+'</b>',SM),P(e(a),SM),P(e(b),SM),P(e(c),SM)])
lt=Table(rows,colWidths=[0.85*inch,2.05*inch,2.45*inch,1.65*inch],repeatRows=1)
lt.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dfe5ef')),('VALIGN',(0,0),(-1,-1),'TOP')]))
S.append(lt)
S.append(P('2. Owner-requested editorial context',H2))
bt=Table([[P(e(bridge),B)]],colWidths=[7*inch]);bt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.8,colors.HexColor('#8a6d00')),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#fffbea'))]))
S.append(bt)
S.append(P('3. Requested researchers — contingent needs only, NOT hiring/assignment authorization',H2))
rr=[[P('<b>'+h+'</b>',SM) for h in ['#','Profile','Lane','Purpose','Condition']]]+[[P(e(x),SM) for x in r] for r in researchers]
rt=Table(rr,colWidths=[0.3*inch,2.2*inch,0.9*inch,1.3*inch,2.3*inch])
rt.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dfe5ef')),('VALIGN',(0,0),(-1,-1),'TOP')]))
S.append(rt);S.append(Spacer(1,4))
S.append(P('PP lane and AGENT lane: no researchers requested. No researchers are assigned.',B))
S.append(P('4. Blockers and open items (as reported)',H2))
S.append(P('<b>Owner definitions/derivations named by PP as the main blocker:</b> '+e('; '.join(defs))+'.',B));S.append(Spacer(1,3))
S.append(P('<b>Other open items, by lane:</b>',B))
for o in other_open:S.append(Paragraph(e(o),BL,bulletText='•'))
S.append(P('<b>Review statuses unknown:</b>',B))
for u in unknown:S.append(Paragraph(e(u),BL,bulletText='•'))
S.append(P('5. Key reported identifiers and values (as reported)',H2))
kt=Table([[P('<b>'+e(k)+'</b>',SM),P(e(v),SM)] for k,v in keyvals],colWidths=[2.2*inch,4.8*inch])
kt.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.grey),('BACKGROUND',(0,0),(0,-1),colors.HexColor('#eef1f6')),('VALIGN',(0,0),(-1,-1),'TOP')]))
S.append(kt)
S.append(KeepTogether([P('6. Bottom line (PP’s words)',H2),P(e(bottom),B),Spacer(1,6),P('<b>'+e(pause)+'</b>',WARN)]))
S.append(PageBreak())
S.append(P('Appendix A — Full original PP message (verbatim)',H2))
S.append(P('<i>Attribution: Professor Proof (PP), workload summary received Nov 5, 2026, 16:09 CST. Reproduced verbatim; not edited, not revalidated.</i>',SM));S.append(Spacer(1,6))
for line in src.split('\n'):
    if not line.strip():S.append(Spacer(1,6));continue
    st=AP
    if line.startswith('- '):st=ParagraphStyle('apb',parent=AP,leftIndent=24,firstLineIndent=-10)
    elif line.startswith('('):st=ParagraphStyle('apn',parent=AP,leftIndent=26,firstLineIndent=-22)
    elif line.isupper() or line in('PP','LOCAL','NON LOCAL','EIGEN','AGENT'):st=ParagraphStyle('aph',parent=AP,fontName='DVB')
    S.append(P(e(line),st))
S.append(Spacer(1,8));S.append(P('— End of Appendix A —',SM))
def foot(c,d):
    c.saveState();c.setFont('DV',7.5);c.setFillColor(colors.HexColor('#555555'))
    c.drawString(0.75*inch,0.5*inch,'DRAFT · Findings as reported by Professor Proof; not independently revalidated or certified · All work PAUSED')
    c.drawRightString(letter[0]-0.75*inch,0.5*inch,f'Page {d.page}');c.restoreState()
doc=SimpleDocTemplate(OUT+'.pdf',pagesize=letter,leftMargin=0.75*inch,rightMargin=0.75*inch,topMargin=0.7*inch,bottomMargin=0.8*inch,
 title=TITLE,author='Draft rendering of Professor Proof workload summary',subject='DRAFT')
doc.build(S,onFirstPage=foot,onLaterPages=foot)
