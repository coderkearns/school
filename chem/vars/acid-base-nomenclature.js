const nomenclatureList = {
  1: {
    regex: /(.*)ide/gi,
    func: (name) => `hydro ${removeChars(name, "ide")}ic acid`,
  },
  2: {
    regex: /(.*)ite/gi,
    func: (name) => `${removeChars(name, "ite")}ous acid`,
  },
  3: {
    regex: /(.*)ate/gi,
    func: (name) => `${removeChars(name, "ate")}ic acid`
  }
}

const undoList = {
  1: {
    regex: /hydro (.*)ic acid/gi,
    func: (name) => `${removeChars(name, ["hydro ", "ic acid"])}ite`,
  },
  2: {
    regex: /(.*)ous acid/gi,
    func: (name) => `${removeChars(name, "ous acid")}ite`,
  },
  3: {
    regex: /(.*)ic acid/gi,
    func: (name) => `${removeChars(name, "ic acide")}ate`,
  },
}

function toNomenclature(name) {
  for (let i in nomenclatureList) {
    if (nomenclatureList[i].regex.test(name)) {
      return nomenclatureList[i].func(name)
    }
  }
}

function fromNomenclature(name) {
  for (let i in undoList) {
    console.log(i)
    if (undoList[i].regex.test(name)) {
      console.log(name)
      return undoList[i].func(name)
    }
  }
}

function removeChars(str, chars) {
  if (Array.isArray(chars)) {
    for (let i of chars) {
      str = str.replaceAll(i, "")
    }
  } else {
    str = str.replaceAll(chars, "")
  }
  return str
}

module.exports = {
  toNomenclature,
  fromNomenclature
}