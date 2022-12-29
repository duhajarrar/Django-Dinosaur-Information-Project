from atexit import register
from django.utils.html import escape, mark_safe
@register.simple_tag(takes_context=True)
def dino_list(context, title):
    output = [f"<h2>{title}</h2><ul>"]
    for dino in context["dinosaurs"]:
        output.append(f"<li>{escape(dino)}</li>")
    output.append("</ul>")
    output = "".join(output)
    context["weight"] = "20 tons"
    return mark_safe(output)