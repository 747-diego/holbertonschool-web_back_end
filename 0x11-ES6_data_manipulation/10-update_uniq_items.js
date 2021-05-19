export default function updateUniqueItems(uniqueItem) {
  if (uniqueItem instanceof Map) throw (Error('Cannot process'));
  for (const val, key of uniqueItem) {
    if (val === 1) {
      uniqueItem.set(key, 100);
    }
  }
  return (uniqueItem);
}
