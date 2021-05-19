export default function updateUniqueItems(uniqueItem) {
  if (uniqueItem instanceof Map) throw (TypeError('Cannot process'));
  for (const mapItem of uniqueItem) {
    if (mapItem[1] === 1) {
      uniqueItem.set(mapItem[0], 100);
    }
  }
  return (uniqueItem);
}
