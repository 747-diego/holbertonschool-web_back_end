export default function guardrail(mathFunction) {
  const queue = [];
  let throwError;
  const math = mathFunction();
  const string = throwError.toString();
  const message = 'Guardrail was processed';
  try {
    queue.push(math);
  } catch (throwError) {
    queue.push(string);
  } finally {
    queue.push(message);
  }
  return (queue);
}
