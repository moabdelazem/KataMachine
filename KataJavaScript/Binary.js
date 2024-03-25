// Binary Search Algorithim
// is it Ordered?

/* 
    Psuedo Code
    1. Find the middle of the array
    2. Compare the middle value to the target value
    3. If the middle value is equal to the target value, return the index of the middle value
    4. If the middle value is less than the target value, repeat the search on the right half of the array
    5. If the middle value is greater than the target value, repeat the search on the left half of the array
    6. If the target value is not found, return -1
*/

function binSearch(hayStack, needle) {
  let low = 0;
  let high = hayStack.length - 1;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);

    if (needle === hayStack[mid]) {
      return mid;
    } else if (needle > hayStack[mid]) {
      low = mid + 1;
    } else {
      high = mid;
    }
  }

  return -1;
}

// Test Array
// O(log n) => O(3) => O(1)
let myArray = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(binSearch(myArray, 8));
console.log(binSearch(myArray, 1));
console.log(binSearch(myArray, 5));
