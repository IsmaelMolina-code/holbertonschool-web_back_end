export default function returnHowManyArguments(...args) {
  let total = 0;
  args.forEach(() => { total += 1; });
  return total;
}
