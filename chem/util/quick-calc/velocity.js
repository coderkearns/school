const getVars = require("../getvars.js")

const u = require("../../formulas/velocity")

module.exports = () => {
  args = getVars({
    "t (celcius)": parseFloat,
    mw: parseFloat
  })

  let velocity = u(args["t (celcius)"]+273, args.mw)
  console.log(`u_rms = ${velocity} m/s`)
}
