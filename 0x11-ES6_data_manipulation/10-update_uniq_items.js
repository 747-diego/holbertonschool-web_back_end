export default function updateUniqueItems(uniqueItem) {
  if (uniqueItem instanceof Map) throw (TypeError('Cannot process'));
  uniqueItem.forEach((entry, item) => {
    if (entry === 1) {
      uniqueItem.set(item, 100);
    }
  });
  return (uniqueItem);
}
