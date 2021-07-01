/*

ionization % = [H+] / [original acid] * 100

Ka = [H+]*[A-] / [original acid]

Kb = [OH-]*[B] / [original base]

EX:

HA -> H+ + A-

Assign vars: x

totalM-x     x         x
  HA     ->  H+    +   A-

Can we neglect x?
neglectable = abs( exponentOf(Ka) - exponentOf([originalAcid]) ) >= 3

If neglectable:
Ka = x^2 / [originalAcid]
x = sqrt(Ka*originalAcid)

To solve:
# From totalMolarity (M) and Ka to ionization %

Ka = [H+] + [A-] / M
Ka = x^2 / M - x
checkNeglect...
x = sqrt(M - Ka)

# From totalMolarity (M) and ionization % (ion) to Ka
x = ion/100 * M
Ka = x^2 / (M - x)


## If not neglectable!:

x^2 = Ka*(totalM - x)

x = (-a + sqrt(a^2 + 4*a*b)) / 2
or
x =(-a - sqrt(a^2 + 4*a*b)) / 2

*/

const sqrt = require("../util/sqrt")

const parseExp = num => parseInt(num.toExponential().split("e")[1])

function checkNeglect(num1, num2) {
  return Math.abs(parseExp(num1) - parseExp(num2)) >= 3
}

function ionization(totalM, Ka) {
  let neglectable = checkNeglect(Ka, totalM)
  if (neglectable) {
    let x = sqrt(totalM - Ka)
    return {
      x,
      ion: (x / totalM) * 100,
    }
  } else {
    let x1 = (-Ka + sqrt(Math.pow(Ka, 2) + 4 * Ka * totalM)) / 2
    let x2 = (-Ka - sqrt(Math.pow(Ka, 2) + 4 * Ka * totalM)) / 2
    let x = [x1, x2]
    return {
      x: x.map(a => a.toExponential()),
      ion: x.map(x => (x / totalM) * 100).map(a=>a.toExponential()),
    }
  }
}

function Ka(totalM, ion) {
  let x = (ion / 100) * totalM
  return {
    x,
    Ka: Math.pow(x, 2) / (totalM - x),
  }
}


module.exports = {
  checkNeglect,
  ionization,
  Ka,
}
