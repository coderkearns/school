const nonmetalIons = {
  "H-": "hydride",
  "N3-": "nitride",
  "O2-": "oxide",
  "F-": "fluoride",
  "H+": "hydrogen",
  "P3-": "phosphide",
  "S2-": "sulfide",
  "Cl-": "chloride",
  "As3-": "arsenide",
  "Se2-": "selenide",
  "Br-": "bromide",
  "Te2-": "telluride",
  "I-": "iodide",
}

const polyatomicIons = {
  NH3: "ammonia",
  "ClO4-": "perchlorate",
  "C2O4^2-": "oxalate",
  "NH4+": "ammonium",
  "ClO3-": "chlorate",
  "O2^2-": "peroxide",
  "H3O+": "hydronium",
  "ClO2-": "chlorite",
  "PO4^3-": "phosphate",
  "CH3COO-": "acetate",
  "ClO-": "hypochlorite",
  "HPO4^2-": "monohydrogen phosphate",
  "AsO4^3-": "arsenate",
  "CrO4^2-": "chromate",
  "H2PO4-": "dihydrogenphosphate",
  "BO3^3-": "borate",
  "Cr2O7^2-": "dichromate",
  "PO3^3-": "phosphite",
  "B4O7^2-": "tetraborate",
  "CN-": "cyanide",
  "SeO4^2-": "selenate",
  "BrO3-": "bromate",
  "OH-": "hydroxide",
  "SiO3^2-": "silicate",
  "BrO-": "hypobromite",
  "IO4-": "periodate",
  "SiF6^2-": "hexafl uorosilicate",
  "CO3^2-": "carbonate",
  "IO3-": "iodate",
  "SO4^2-": "sulfate",
  "HCO3-": "hydrogen carbonate (bicarbonate)",
  "IO-": "hypoiodite",
  "HSO4-": "hydrogen sulfate (bisulfate)",
  "MnO4-": "permanganate",
  "SO3^2-": "sulfi te",
  "NO3-": "nitrate",
  "HSO3-": "hydrogen sulfite (bisulfite)",
  "NO2-": "nitrite",
  "C4H4O6^2-": "tartrate",
  "S2O3^2-": "thiosulfate",
}

const commonAcids = {
  HC2H3O2: 'acetic acid',
  CH3COOH: 'acetic acid',
  HNO3: 'nitric acid',
  H2CO3: 'carbonic acid',
  H3PO4: 'phosphoric acid',
  HCl: 'hydrochloric acid',
  H2SO4: 'sulfuric acid'
}

const all = { ...nonmetalIons, ...polyatomicIons, ...commonAcids }

module.exports = {
  nonmetalIons,
  polyatomicIons,
  commonAcids,
  all,
}