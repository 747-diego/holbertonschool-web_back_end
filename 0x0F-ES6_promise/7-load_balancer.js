export default function loadBalancer(chinaDownload, USDownload) {
  const promiseDownload = Promise.race([chinaDownload, USDownload]);
  return (promiseDownload);
}
