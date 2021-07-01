/*

pH = -log [H+]
pOH = -log [OH-]

# undoing from pH or pOH as p:
[H or OH] = 10^-p

*/

const log = Math.log10

function pH(M) {
  return -(log(M))
}

function pOH(M) {
  return -(log(M))
}

function undo(p) {
  return Math.pow(10, -p)
}

module.exports = { pH, pOH, undo }