export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() {
    const size = this._size;
    return (size);
  }

  toString() {
    const location = this._location;
    return (location);
  }
}
