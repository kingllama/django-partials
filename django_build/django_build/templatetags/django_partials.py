from django import template

register = template.Library()

@register.tag(name="include_part")
def include_part(parser, token):
    tag_name, partial_filename = token.split_contents()
    if partial_filename[0] == '"' or partial_filename[0] == "'":
        return partial_main_node(partial_filename[1:-1])
    else:
        return partial_main_node(partial_filename)

class partial_main_node(template.Node):
    def __init__(self, partial_filename):
        print type(partial_filename)
        self.partial_filename = partial_filename

    def render(self, context):
        print self.partial_filename
        t = context.template.engine.get_template(self.partial_filename)
        print context
        return t.render(template.Context({},autoescape=context.autoescape))