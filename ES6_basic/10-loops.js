/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    let index = 0;
    const arr = array;
    for (const idx of array) {
      arr[index] = appendString + idx;
      index += 1;
    }
  
    return arr;
  }
