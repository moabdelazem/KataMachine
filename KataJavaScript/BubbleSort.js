// O(n^2)
function bubbleSort(arr) {
  for (let i = 0; i < arr.length; ++i) {
    for (let j = 0; j < arr.length - 1 - i; ++j) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

// Test Array
let myArray = [1, 3, 2, 4, 6, 5, 8, 7];
bubbleSort(myArray);
console.log(myArray);
