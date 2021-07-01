/*

H2O -> H+ + OH-

Kw always equals = [H+][OH-] = 1e-14

# Thus, to find [H+] or [OH-]:

1e-14 = [H+][OH-]

[H+] = 1e-14 / [OH-]
[OH-] = 1e-14 / [H+]

*/

const Kw = 1e-14

function H(OH) {
  return Kw / OH
}
function OH(H) {
  return Kw / H
}

module.exports = { Kw, H, OH }
