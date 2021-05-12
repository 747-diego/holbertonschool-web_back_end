export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  const dividend = (numerator / denominator);
  return (dividend);
}
