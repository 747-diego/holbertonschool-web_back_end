export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    const code = this._code;
    return (`[object ${code}]`);
  }
}
