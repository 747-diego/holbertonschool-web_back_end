export default function updateUniqueItems(uniqueItem) {
  if (uniqueItem instanceof Map) throw (TypeError('Cannot process'));
  uniqueItem.forEach((entry, item) => {
    if (entry === 1) {
      const mapItem = (item, 100);
      uniqueItem.set(mapItem);
    }
  });
  return (uniqueItem);
}
