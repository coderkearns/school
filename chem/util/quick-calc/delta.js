const getVars = require("../getvars.js")

const {
  t,
  solutions: { molality },
} = require("../../formulas")
const { mol } = require("../../vars")

module.exports = () => {
  args = getVars({
    massSolute: parseFloat,
    mw: parseFloat,
    kgSolute: parseFloat,
    k: parseFloat,
  })

  let moles = mol(args.massSolute, args.mw)
  let m = molality(moles, args.kgSolute)
  let delta = t(m, args.k)
  console.log(`Delta = Δ ${delta}°`)
}
