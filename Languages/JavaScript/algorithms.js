// Popular Algorithms in JavaScript

// Bubble Sort
function bubbleSort(arr) {

var len = arr.length;
  for (var i = len-1; i >= 0; i--) {
    for (var j = 1; j <= i; j++) {
      if (arr[j-1] > arr[j]) {
        var temp = arr[j-1];
        arr[j-1] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
}


// Test Cases
console.log(`${bubbleSort([5,3,8,2,1,4])}`);
console.log(`${bubbleSort([20,20,31,56,1,12,12])}`);
