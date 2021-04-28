
## Ellipse

The set of all points in a plane where the sum of the distances from two special points, called focus points, is equal.

Every ellipse has two axes of symmetry. The parts of the axes of symmetry which lie inside the ellipse are called the major and minor axes.

### Class

`::__init__`
- `major_axis_1`: the start of th major axis, in the form of a Point
- `major_axis_2`: the end of th major axis, in the form of a Point
- `focus_point_1`: one of the focus points, a Point
- `focus_point_2`: the other focus point, a Point
- `center`: the center of the ellipse, a Point

`.h`: The x of the center point

`.k`: The y of the center point

`.a`: Half the major axis's length

`.c`: Half the distance between the focus points

`.b`: The square root of `a^2 -  c^2`

`.type`: Returns "horizontal" or "vertical"

`.equation`: Returns the equation for the ellipse

### Special Points
The focus points, or foci, lie on the major axis.
Consequently, the major axis is a longer segment whose distance is `2a`, whereas the minor axis is the shorter segment whose distance is `2b(a > b)`.
The distance between the foci is `2c`.
There is a special relationship between `a`, `b` and `c` in an ellipse. self relationship, involving the Pythagorean theorem, is `b^2 = a^2 - c^2`

### Equation
The equation of an ellipse with a horizontal major axis and center `(h, k)` is:
```
(x - h)^2    (y - k)^2
—————————— + —————————— = 1
   a^2          b^2
```

The equation of an ellipse with a vertical major axis and center `(h, k)` is:
```
(x - h)^2    (y - k)^2
—————————— + —————————— = 1
   b^2          a^2
where b^2 = a^2 - c^2
```

### How to tell it's type
If `b > a`: This is a horizontal ellipse.
If `a > b`: This is a vertical ellipse.


