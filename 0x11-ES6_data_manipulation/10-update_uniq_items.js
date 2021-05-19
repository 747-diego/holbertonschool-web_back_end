export default function updateUniqueItems(uniqueItem) {
  if (uniqueItem instanceof Map) throw (Error('Cannot process'));
  uniqueItem.forEach((mapItem, entry) => {
    const quantity = mapItem === 1;
    if (quantity) {
      uniqueItem.set(entry, 100);
    }
  });
  return (uniqueItem);
}
