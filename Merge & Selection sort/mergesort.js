function selectionSort(arr) {
    // Traverse through all array elements
    for (let i = 0; i < arr.length; i++) {
        // Find the minimum element in remaining unsorted array
        let minIndex = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        
        // Swap the found minimum element with the first element
        if (minIndex !== i) {
            let temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    return arr;
}

// Example usage
let arr = [64, 25, 12, 22, 11];
let sortedArr = selectionSort(arr);
console.log("Sorted array:", sortedArr);
