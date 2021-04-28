
from . import line, point, parabola, circle, ellipse

__all__ = ["line", "point", "parabola", "circle", "ellipse"]

__doc__ = "\n---\n\n".join([
    point.doc,
    line.doc,
    circle.doc,
    parabola.doc,
    ellipse.doc
])
