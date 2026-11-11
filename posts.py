F="node_modules/@fontsource/poppins/files"
ff="".join(f"@font-face{{font-family:Poppins;font-weight:{w};font-style:{s};src:url({F}/poppins-latin-{w}-{s}.woff2)}}" for w,s in [(300,'normal'),(400,'normal'),(500,'normal'),(800,'normal'),(300,'italic'),(800,'italic')])
css=ff+"""
:root{--lima:#E4F062;--ink:#1A1217;--soft:#F4F4F1;--grey:#8C8C8C}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#999;font-family:Poppins,sans-serif;color:var(--ink)}
.post{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;padding:90px;display:flex;flex-direction:column}
em{font-style:italic;font-weight:800;background:var(--lima);color:var(--ink);padding:0 .16em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.dark{background:var(--ink);color:#fff}.soft{background:var(--soft)}.limabg{background:var(--lima)}
.limabg em{background:var(--ink);color:var(--lima)}
h1{font-weight:500;font-size:104px;line-height:1.22;letter-spacing:-.02em}
h1 em{font-weight:800}
.foot{position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:500}
.logo{font-weight:800;font-size:34px;display:flex;align-items:center;gap:8px;letter-spacing:-.01em}
.logo i{font-style:italic;background:var(--lima);color:var(--ink);padding:2px 12px;border-radius:6px;font-weight:800;font-size:30px}
.dark .logo{color:#fff}.limabg .logo i{background:var(--ink);color:var(--lima)}
.sub{font-size:38px;font-weight:300;line-height:1.4;margin-top:36px}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.btn{display:inline-block;background:var(--ink);color:var(--lima);font-weight:500;font-size:34px;padding:26px 50px;border-radius:999px}
.limabtn{background:var(--lima);color:var(--ink)}
.c{justify-content:center;padding-bottom:190px}
/* p1 */
.p1 .card{position:absolute;left:70px;right:70px;bottom:150px;background:#fff;border-radius:34px;padding:56px}
.p1 h1{font-size:92px}.p1 .sub{font-size:34px;margin-top:20px;color:#444}
.p1 .foot{color:#fff}.p1 .logo{color:#fff}
/* p2 bars */
.bars{position:absolute;right:0;bottom:170px;display:flex;flex-direction:column;gap:20px;align-items:flex-end;width:100%}
.bar{height:92px;border-radius:46px 0 0 46px;background:var(--lima);display:flex;align-items:center;padding-left:44px;font-weight:800;font-style:italic;font-size:44px}
.bar.k{background:var(--ink);color:var(--lima)}.bar.s{background:var(--soft);border:2px solid #d0d0c8;border-right:0;font-weight:800}
/* p4 */
.rows{display:flex;flex-direction:column;gap:22px;margin-top:56px}
.row{background:#fff;border-radius:26px;padding:30px 38px;display:flex;gap:30px;align-items:center}
.row b{font-weight:800;font-style:italic;font-size:54px;color:var(--ink);background:var(--lima);min-width:96px;height:96px;border-radius:20px;display:flex;align-items:center;justify-content:center}
.row strong{font-size:38px;font-weight:600;display:block}.row span{font-size:28px;font-weight:300;color:#555;line-height:1.35;display:block;margin-top:4px}
h2{font-weight:500;font-size:88px;line-height:1.2;letter-spacing:-.02em}h2 em{font-weight:800}
/* p6 */
.p6:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,18,23,.92) 0%,rgba(26,18,23,.55) 38%,rgba(26,18,23,0) 62%);z-index:1}
.p6 h1{position:relative;z-index:2;color:#fff;font-size:96px}
.p6 .foot{z-index:2;color:#fff}
/* p7 */
.big{font-weight:800;font-style:italic;font-size:560px;line-height:.9;color:var(--lima);letter-spacing:-.04em;margin-top:30px}
/* p8 */
.steps{display:flex;flex-direction:column;gap:0;margin-top:60px}
.step{display:flex;gap:36px;align-items:flex-start;padding:30px 0;border-top:2px solid #e3e3dc}
.step:first-child{border-top:0}
.step b{font-weight:800;font-style:italic;font-size:46px;color:var(--ink);background:var(--lima);min-width:100px;height:84px;border-radius:16px;display:flex;align-items:center;justify-content:center}
.step strong{font-size:46px;font-weight:600;display:block;line-height:1.1}.step span{font-size:30px;font-weight:300;color:#555;display:block;margin-top:6px}
/* p9 */
.checks{margin-top:50px;display:flex;flex-direction:column;gap:20px}
.chk{background:#fff;border-radius:22px;padding:28px 36px;font-size:36px;font-weight:500;display:flex;gap:26px;align-items:center}
.chk:before{content:"×";font-weight:800;font-size:44px;width:64px;height:64px;border-radius:50%;background:var(--ink);color:var(--lima);display:flex;align-items:center;justify-content:center;flex:none;padding-bottom:6px}
.ans{margin-top:44px;font-size:42px;font-weight:300;line-height:1.35}.ans b{font-weight:800}
/* p10 */
.p10 h1{font-size:112px}
.p10 .ph{position:absolute;left:0;right:0;bottom:0;height:640px;overflow:hidden}
.p10 .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 38%}
.p10 .foot{display:none}
.p10 .btn{margin-top:46px}
"""
def foot(extra=""): return f'<div class="foot"><div class="logo">SOLÍS <i>MEDIA</i></div><div>{extra}</div></div>'
P=[]
P.append(f'''<div class="post p1"><img class="photo" src="foto-ignacio.jpg" style="object-position:50% 20%"><div class="card"><h1>Hola, soy <em>Ignacio</em></h1><p class="sub">Soy quien está detrás de Solís Media. Si nos escribes, hablas conmigo.</p></div>{foot()}</div>''')
P.append(f'''<div class="post p2"><h1 style="font-size:120px;margin-top:20px">Tu marca merece <em>ser conocida.</em></h1><div class="bars"><div class="bar" style="width:52%">Shopify</div><div class="bar k" style="width:70%">WordPress</div><div class="bar" style="width:88%">Marca personal</div><div class="bar s" style="width:76%">Tienda online</div><div class="bar" style="width:58%">Videos</div></div>{foot()}</div>''')
P.append(f'''<div class="post dark p3 c"><h1 style="margin-top:60px;font-size:98px">Puedes ser el mejor, pero si nadie te conoce, <em>gana la competencia.</em></h1><p class="sub" style="color:#cfcfcf;font-size:40px">Que te conozcan no es vanidad. Es parte de vender.</p>{foot("Guárdalo 📌")}</div>''')
rows=[("01","Sitios web y tiendas online","Un lugar propio donde mostrarte y vender."),("02","Administración de anuncios","Que las personas correctas conozcan tu marca."),("03","Edición de video y contenido","Tú grabas, nosotros lo dejamos listo."),("04","Optimización y automatización","Mejoramos tu web y respondemos más rápido.")]
r="".join(f'<div class="row"><b>{a}</b><div><strong>{b}</strong><span>{c}</span></div></div>' for a,b,c in rows)
P.append(f'''<div class="post soft p4"><h2>4 formas de ayudarte a <em>mostrarte</em></h2><div class="rows">{r}</div>{foot("Guárdalo 📌")}</div>''')
P.append(f'''<div class="post limabg p5 c"><h1 style="margin-top:80px;font-size:118px">Si no estás en digital, para muchos <em>no existes.</em></h1><p class="sub" style="font-size:42px;font-weight:500">Hoy los clientes te buscan en internet antes de escribirte.</p>{foot()}</div>''')
P.append(f'''<div class="post p6"><img class="photo" src="foto-ignacio.jpg" style="object-position:50% 70%"><h1>Lo que no se muestra, <em>no se conoce.</em></h1>{foot()}</div>''')
P.append(f'''<div class="post dark p7"><div class="big">+8</div><h2 style="font-size:72px;margin-top:20px">años en el mundo <em>digital</em></h2><p class="sub" style="color:#cfcfcf;font-size:36px;margin-top:28px;max-width:820px">Con negocios propios y con clientes. Experiencia real detrás de cada proyecto.</p>{foot()}</div>''')
st=[("01","Conversamos","Tu proyecto y lo que quieres lograr."),("02","Maqueta","Un diseño para que lo veas con calma."),("03","Ajustamos","Colores, textos y detalles."),("04","Lanzamos","Entrega y mejora continua.")]
s="".join(f'<div class="step"><b>{a}</b><div><strong>{b}</strong><span>{c}</span></div></div>' for a,b,c in st)
P.append(f'''<div class="post p8 c"><h2>Así hacemos tu <em>sitio web</em></h2><div class="steps">{s}</div>{foot("Guárdalo 📌")}</div>''')
c="".join(f'<div class="chk">{t}</div>' for t in ["Se demora en cargar","Nadie sabe qué hacer al entrar","Respondes lo mismo todo el día"])
P.append(f'''<div class="post soft p9 c"><h2>¿Tienes web pero <em>no vende?</em></h2><div class="checks">{c}</div><p class="ans">Optimizamos tu web y <b>automatizamos tu WhatsApp</b> para que no pierdas clientes.</p>{foot()}</div>''')
P.append(f'''<div class="post dark p10"><h1>¿Hablamos?</h1><p class="sub" style="color:#cfcfcf;margin-top:24px">Escríbeme por WhatsApp.<br>Te respondo yo, <b style="color:var(--lima);font-weight:600">Ignacio</b>.</p><div><span class="btn limabtn">Escríbeme por WhatsApp</span></div><div class="ph"><img src="foto-ignacio.jpg"></div></div>''')
open("posts.html","w",encoding="utf-8").write(f'<!doctype html><html lang="es"><meta charset="utf-8"><style>{css}</style><body>'+"".join(P)+'</body></html>')
