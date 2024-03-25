// Crystal Balls Problem
// O(sqrt(n))
function twoCrystalBall(arr) {
  // Calculate the number of floors
  const jumpLength = Math.floor(Math.sqrt(arr.length));
  let i = 0;

  // Leaping through the array
  for (; i < arr.length; i += jumpLength) {
    if (arr[i] === 1) {
      break;
    }
  }

  // Going back to the previous floor
  i -= jumpLength;

  for (let j = i; j < i + jumpLength; j++) {
    if (arr[j] === 1) {
      return j;
    }
  }

  return -1;
}

// Test Array
let myArray = [0, 0, 0, 1, 1, 1, 1, 1];
console.log(twoCrystalBall(myArray));
