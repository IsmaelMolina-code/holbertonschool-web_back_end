export default function returnHowManyArguments(...args) {
  let total = 0;
  args.forEach((arg) => { total += 1; });
  return total;
}
