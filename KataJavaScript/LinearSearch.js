// Linear search is the most basic search algorithm. It is a method for finding a target value within a list.
export default function linearSearch(haystack, needle) {
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle) {
      return i;
    }
  }
  return -1;
}
