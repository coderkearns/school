/* Solution Formulas:

// Mass Percent
massPercent = ( massSolute / massTotal ) * 100

// Mole Fraction
moleFraction = molesSolute / molTotal

// Molality
m = molSolute / kgSolute

// Molarity
M = molSolute / literSolution
*/

function massPercent(massSolute, massTotal) {
  return (massSolute / massTotal) * 100
}

function moleFraction(molSolute, molTotal) {
  return molSolute / molTotal
}

function molality(molSolute, kgSolute) {
  return molSolute / kgSolute
}

function molarity(molSolute, literSolution) {
  return molSolute / literSolution
}

module.exports = {
  massPercent,
  // (massSolute, massTotal)

  moleFraction,
  // (molSolute, molTotal)

  molality,
  // (molSolute, kgSolute)

  molarity,
  // (molSolute, literSolution)
}
