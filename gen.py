import json, re

WA = "https://wa.me/56900000000"   # reemplazar por el numero real
def attrs(d): return (" " + json.dumps(d, ensure_ascii=False, separators=(",",":"))) if d else ""

def grp(cls, inner, anchor=None, align=None):
    a = {"className": cls}
    if anchor: a["anchor"] = anchor
    if align: a["align"] = align
    idattr = f' id="{anchor}"' if anchor else ""
    al = f"{'alignfull ' if align=='full' else ''}"
    return f'<!-- wp:group{attrs(a)} -->\n<div{idattr} class="wp-block-group {al}{cls}">\n{inner}\n</div>\n<!-- /wp:group -->'

def p(text, cls=None):
    a = {"className": cls} if cls else {}
    c = f' class="{cls}"' if cls else ""
    return f'<!-- wp:paragraph{attrs(a)} -->\n<p{c}>{text}</p>\n<!-- /wp:paragraph -->'

def h(level, text, cls=None):
    a = {}
    if level != 2: a["level"] = level
    if cls: a["className"] = cls
    c = f' {cls}' if cls else ""
    return f'<!-- wp:heading{attrs(a)} -->\n<h{level} class="wp-block-heading{c}">{text}</h{level}>\n<!-- /wp:heading -->'

def btns(items, cls=None):
    out = []
    for text, href, outline in items:
        a = {"className": "is-style-outline"} if outline else {}
        c = " is-style-outline" if outline else ""
        out.append(f'<!-- wp:button{attrs(a)} -->\n<div class="wp-block-button{c}"><a class="wp-block-button__link wp-element-button" href="{href}">{text}</a></div>\n<!-- /wp:button -->')
    a = {"className": cls} if cls else {}
    c = f" {cls}" if cls else ""
    return f'<!-- wp:buttons{attrs(a)} -->\n<div class="wp-block-buttons{c}">\n' + "\n".join(out) + '\n</div>\n<!-- /wp:buttons -->'

def ul(items, cls=None):
    li = "\n".join(f'<!-- wp:list-item -->\n<li>{t}</li>\n<!-- /wp:list-item -->' for t in items)
    a = {"className": cls} if cls else {}
    c = f" {cls}" if cls else ""
    return f'<!-- wp:list{attrs(a)} -->\n<ul class="wp-block-list{c}">{li}</ul>\n<!-- /wp:list -->'

def details(summary, inner, cls=None, open_=False):
    a = {}
    if cls: a["className"] = cls
    if open_: a["showContent"] = True
    c = f" {cls}" if cls else ""
    o = " open" if open_ else ""
    return f'<!-- wp:details{attrs(a)} -->\n<details class="wp-block-details{c}"{o}><summary>{summary}</summary>\n{inner}\n</details>\n<!-- /wp:details -->'

def html(code): return f'<!-- wp:html -->\n{code}\n<!-- /wp:html -->'

def image(src, alt, cls):
    return f'<!-- wp:image {{"sizeSlug":"large","linkDestination":"none","className":"{cls}"}} -->\n<figure class="wp-block-image size-large {cls}"><img src="{src}" alt="{alt}"/></figure>\n<!-- /wp:image -->'

ICON = {
 "web": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#1A1217" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
 "ads": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#1A1217" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>',
 "auto": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#1A1217" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></svg>',
 "video": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#1A1217" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2" ry="2"/></svg>',
}
def icon(k): return html(f'<div class="sm-ico">{ICON[k]}</div>')

# ---------- secciones ----------
nav = grp("sm-navwrap", "\n".join([
    p('SOLÍS <em>MEDIA</em>', "sm-logo"),
    p('<a href="#servicios">Servicios</a><a href="#proceso">Proceso</a><a href="#nosotros">Nosotros</a><a href="#contacto">Contacto</a>', "sm-nav"),
    btns([("Hablemos", WA, False)], "sm-navbtn"),
]))

bars = grp("sm-bars", "\n".join([
    p("Shopify", "sm-bar sm-bar-a"), p("WordPress", "sm-bar sm-bar-b"), p("Marca personal", "sm-bar sm-bar-c"),
    p("Tienda online", "sm-bar sm-bar-d"), p("Videos", "sm-bar sm-bar-e"), p("Contenido", "sm-bar sm-bar-f"),
]))
hero = grp("sm-hero", "\n".join([
    grp("sm-herotext sm-col", "\n".join([
        p("Sitios web · Tiendas online · Anuncios · Video", "sm-eyebrow"),
        h(1, "Tu marca merece<br><em>ser conocida.</em>", "sm-h1"),
        p("Creamos tu web o tienda online, manejamos tus anuncios y editamos tus videos para que más gente te encuentre, conozca lo que haces y te elija.", "sm-lead"),
        btns([("Cotiza gratis", WA, False), ("Ver proyectos", "#proyectos", True)]),
    ])),
    bars,
]), anchor="inicio")

exp = grp("sm-sec sm-dark sm-exp", "\n".join([
    grp("sm-expbig", p("+8", "sm-big") + "\n" + p("años de<br>experiencia", "sm-bigcap")),
    grp("sm-col", "\n".join([
        h(2, "Te ayudamos a tener <em>presencia digital</em>"),
        p("Llevamos más de 8 años en el mundo digital, con negocios propios y acompañando a otros clientes. Sabemos lo que cuesta que una marca se vea, se conozca y venda.", "sm-soft"),
        ul(["Estar en digital", "Mostrar lo que haces", "Que te conozcan"], "sm-pills"),
    ])),
]))

def card(ic, title, desc, incluye, ideal, cta, open_=False):
    inner = "\n".join([
        p("INCLUYE", "sm-k"), ul(incluye), p("IDEAL PARA", "sm-k"), p(ideal), btns([(cta, WA, False)]),
    ])
    return grp("sm-card", "\n".join([icon(ic), h(3, title), p(desc), details("Ver más", inner, "sm-more", open_)]))

serv = grp("sm-sec", "\n".join([
    h(2, "Lo que hacemos <em>por tu marca</em>"),
    grp("sm-cards", "\n".join([
        card("web", "Sitios web y tiendas online", "Creamos tu sitio o tu tienda para que tu marca tenga un lugar propio donde mostrarse y vender.",
             ["Sitio web o tienda Shopify nueva", "Páginas de servicios y productos", "Versión para celular", "Formulario y botón de WhatsApp"],
             "Marcas que quieren vender online o mostrar su trabajo.", "Cotizar sitio web"),
        card("ads", "Administración de anuncios", "Planificamos, lanzamos y optimizamos tus campañas para que las personas correctas conozcan tu marca.",
             ["Estrategia y creatividades", "Campañas en Meta (Facebook e Instagram)", "Optimización semanal", "Reporte mensual claro"],
             "Marcas con web o tienda que quieren más visitas y ventas. Con el tiempo, también en Google.", "Cotizar anuncios"),
        card("video", "Edición de video y contenido", "Tú nos envías el material y lo convertimos en videos listos para publicar.",
             ["Montaje y ritmo", "Voz en off y música", "Formatos para redes y anuncios", "Revisión de cambios"],
             "Marcas que graban contenido pero no tienen tiempo de editarlo.", "Cotizar video"),
        card("auto", "Optimización y automatización", "Mejoramos la web que ya tienes y automatizamos tareas para que no pierdas clientes por responder tarde.",
             ["Mejora de velocidad, orden y textos de tu web o tienda", "Respuestas automáticas y flujos en WhatsApp", "Avisos automáticos de pedidos y carritos abandonados", "Formularios conectados a tu WhatsApp o correo"],
             "Marcas que ya tienen web pero no vende lo que podría, o que pierden tiempo respondiendo siempre lo mismo.", "Cotizar optimización"),
    ])),
]), anchor="servicios")

def prow(label, steps):
    st = "\n".join(grp("sm-pstep", p(f"{i+1:02d}", "sm-pn") + "\n" + p(f"<strong>{t}</strong><br>{d}")) for i, (t, d) in enumerate(steps))
    return grp("sm-prow", p(label, "sm-plabel") + "\n" + st)
proceso = grp("sm-sec sm-soft-bg", "\n".join([
    h(2, "Cómo trabajamos <em>según lo que necesites</em>"),
    prow("Sitio web o tienda online", [("Conversamos","Tu proyecto y objetivos."),("Maqueta","Un diseño para ver con calma."),("Ajustamos","Colores, textos y detalles."),("Lanzamos","Entrega y mejora continua.")]),
    prow("Administración de anuncios", [("Diagnóstico","Objetivos, cuenta y tienda."),("Creatividades","Configuración, imágenes y copys."),("Lanzamiento","Campaña activa y medición."),("Optimización","Ajustes semanales y reporte mensual.")]),
    prow("Optimización y automatización", [("Revisión","Vemos tu web y cómo respondes hoy."),("Plan","Qué mejorar y qué automatizar."),("Implementación","Cambios y automatizaciones activas."),("Seguimiento","Medimos y ajustamos.")]),
    prow("Edición de video", [("Brief","Idea, estilo y material."),("Edición","Montaje, voz en off y música."),("Revisión","Cambios sobre el primer corte."),("Entrega","Archivos listos para publicar.")]),
]), anchor="proceso")

def proj(i, cls, cap, kind):
    return grp("sm-projwrap", grp(f"sm-proj {cls}", p("Imagen del proyecto")) + "\n" + p(f"<strong>Marca {i:02d}</strong><br>{kind}", "sm-cap"))
proyectos = grp("sm-sec", "\n".join([
    h(2, "Mostramos <em>lo que hacemos</em>"),
    grp("sm-grid3", "\n".join([proj(1,"sm-proj-1","","Tienda Shopify"), proj(2,"sm-proj-2","","Campaña en Meta"), proj(3,"sm-proj-3","","Contenido y video")])),
]), anchor="proyectos")

def stat(n, t): return grp("sm-stat", p(n, "sm-num") + "\n" + p(t))
cifras = grp("sm-sec sm-lima-bg", grp("sm-grid4", "\n".join([stat("+8","Años de experiencia"), stat("+00","Proyectos entregados"), stat("+00","Marcas acompañadas"), stat("00%","Clientes que repiten")])))

def testi(t): return grp("sm-testi", p(t, "sm-quote") + "\n" + p("<strong>Nombre Apellido</strong><br>Marca, rubro", "sm-who"))
testimonios = grp("sm-sec", "\n".join([
    h(2, "Lo que dicen <em>nuestros clientes</em>"),
    grp("sm-grid2", testi("Aquí va el testimonio real de un cliente, en sus propias palabras.") + "\n" + testi("Aquí va otro testimonio, idealmente de un rubro distinto.")),
]))

about = grp("sm-about", "\n".join([
    image("foto-ignacio.jpg", "Ignacio, fundador de Solís Media", "sm-photo"),
    grp("sm-aboutcard sm-col", "\n".join([
        p("QUIÉN TE ATIENDE", "sm-k"),
        h(2, "Hola, soy <em>Ignacio</em>"),
        p("Cuando escribes a Solís Media, hablas conmigo. Te escucho, entiendo tu proyecto y me ocupo personalmente de que tu marca se muestre, se conozca y venda."),
        btns([("Escríbeme por WhatsApp", WA, False)]),
    ])),
]), anchor="nosotros")

def faq(q, a): return details(q, p(a), "sm-q")
faqs = grp("sm-sec sm-soft-bg sm-faq", "\n".join([
    h(2, "Preguntas <em>frecuentes</em>"),
    faq("¿Cuánto tarda en estar lista mi web o tienda?", "Depende del alcance. Después de conversar tu proyecto te enviamos un plan con los plazos claros."),
    faq("¿Puedo ver cómo quedaría antes de decidir?", "Sí. Te enviamos una maqueta en un link para que la revises con calma y nos digas qué cambiarías."),
    faq("¿Cuánto debo invertir en anuncios?", "Depende de tu objetivo y de tu rubro. Lo definimos juntos en el diagnóstico, y la inversión en anuncios la pagas directo a Meta."),
    faq("¿Puedo contratar solo un servicio?", "Sí. Puedes partir por la web, los anuncios, el video o la optimización, y sumar el resto cuando lo necesites."),
]))

contact = grp("sm-sec sm-dark sm-contact", "\n".join([
    grp("sm-col", "\n".join([
        h(2, "Hagamos que <em>te conozcan.</em>"),
        p("Cuéntanos de tu negocio y te respondemos con ideas, sin compromiso.", "sm-soft"),
        p(f'<a href="{WA}">WhatsApp</a><br><a href="mailto:hola@tudominio.cl">hola@tudominio.cl</a><br><a href="https://instagram.com/tu_usuario">Instagram</a>', "sm-links"),
    ])),
    grp("sm-form", p("Aquí va tu formulario de contacto (Contact Form 7, Fluent Forms o WPForms). Reemplaza este bloque por el shortcode del formulario.", "sm-formph")),
]), anchor="contacto")

footer = grp("sm-footer", "\n".join([p("SOLÍS <em>MEDIA</em>", "sm-logo"), p("Chile · Todos los derechos reservados"), p(f'<a href="{WA}">WhatsApp</a> · <a href="https://instagram.com/tu_usuario">Instagram</a>')]))

page = grp("sm-page", "\n".join([nav, hero, exp, serv, about, proyectos, proceso, cifras, testimonios, faqs, contact, footer]), align="full")
open("bloques-wordpress.html", "w", encoding="utf-8").write(page + "\n")

# ---------- vista previa ----------
FORM = '''<div class="sm-form"><div class="sm-in">Nombre</div><div class="sm-in">Correo o WhatsApp</div><div class="sm-in">¿Qué necesitas?</div><div class="sm-in sm-in-l">Cuéntanos tu idea</div><div class="sm-send">Enviar</div></div>'''
prev = re.sub(r'<div class="wp-block-group sm-form">.*?</div>\n<!-- /wp:group -->', FORM, page, flags=re.S)
prev = prev.replace('src="foto-ignacio.jpg"', 'src="foto-ignacio.jpg"')
css = open("estilos-solis-media.css", encoding="utf-8").read()
WPBASE = """
.wp-block-columns{display:flex;gap:2em}.wp-block-buttons{display:flex;flex-wrap:wrap;gap:.6em}
.wp-block-button__link{display:inline-block;text-align:center;cursor:pointer}
.wp-block-image img{max-width:100%;height:auto}
.wp-block-details summary{cursor:pointer}
body{margin:0;background:#fff}
"""
def page_html(fonts):
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Landing Solís Media</title>
{fonts}<style>{WPBASE}
{css}</style></head><body>{prev}</body></html>'''
GF = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
F = "node_modules/@fontsource/poppins/files"
LOCAL = "<style>" + "".join(f"@font-face{{font-family:Poppins;font-weight:{w};font-style:{s};src:url({F}/poppins-latin-{w}-{s}.woff2)}}" for w,s in [(300,'normal'),(400,'normal'),(500,'normal'),(800,'normal'),(300,'italic'),(800,'italic')]) + "</style>"
open("vista-previa-local.html","w",encoding="utf-8").write(page_html(LOCAL).replace("@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,800;1,300;1,800&display=swap');",""))
frag = f'<title>Landing Solís Media</title>{GF}<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,800;1,300;1,800&display=swap"><style>{WPBASE}\n{css}</style>{prev}'
open("vista-previa.html","w",encoding="utf-8").write(frag)
print("ok", len(page))
