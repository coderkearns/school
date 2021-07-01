
## Conic Sections

All circles, ellipses, hyperbolas, and parabolas are conic sections.
They all share the same equation, so it can be difficult to tell the apart.
We use discriminants to tell the apart from one another.

### Equation of a Conic Section

The equation for a conic section is:
```
Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
```
where `A`, `B`, and `C` are not all 0.

### Discriminants

The discriminant of a conic section (using the above formula) can be calculated by using:
```
d = B^2 - 4AC
```
From there, you can tell the type of conic section using this table:
| Conic Section | Discriminant |
| ------------- | ------------ |
| Parabola      | `d = 0`      |
| Hyperbola     | `d > 0`      |
| Circle        | `d < 0, B = 0, A = C` |
| Ellipse       | `d < 0, B != 0` |
| Ellipse       | `d < 0, A != 0, C != 0, A != C` |

### Class Info

`::__init__(A, B, C, D, E, F)` <br/>
Create a new ConicSection. <br/>
A, B, C, D, E, and F are the same as in the equation.

`::discrimiant` <br/>
A property, which calulates the discrimiant. <br/>
It uses `B^2 - 4AC`

`::type` <br/>
Get the type of Conic Section. <br/>
It uses the table listed above, and return the class for that type of conic section.
