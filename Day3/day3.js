import fs from "fs";

const exampleInPath = "Day3-Input.txt";
const actualInPath = "./inputs/d3a1.txt";
const lines = fs.readFileSync(exampleInPath, "utf-8").trim().split("\r\n");
const noDigitOrDot = /[^0-9.]/g;
const noDigit = /[^0-9]/g;
const digitRegx = /[0-9]/g;
const symbolIndexes = getSymbolIndexes();
const numberIndices = {};

lines.forEach((str, row) => {
  for (let col = 0; col < str.length; col++) {
    const char = str[col];
    if (/\d/.test(char)) {
      const numberStart = col;
      while (col < str.length && /\d/.test(str[col])) {
        col++;
      }
      const numberEnd = col - 1;
      const number = str.substring(numberStart, numberEnd + 1);

      if (!numberIndices[number]) {
        numberIndices[number] = [];
      }

      numberIndices[number].push({
        start: { row, col: numberStart },
        end: { row, col: numberEnd },
      });
    }
  }
});

function getSymbolIndexes() {
  let symbolResult = [];

  for (let rowNumber = 0; rowNumber < lines.length; rowNumber++) {
    const line = lines[rowNumber];
    for (let colomNumber = 0; colomNumber < line.length; colomNumber++) {
      const char = line[colomNumber];

      if (noDigitOrDot.test(char)) {
        symbolResult.push({ rowNumber, colomNumber, symbol: char });
      }
    }
  }
  return symbolResult;
}

export function partOne() {
  console.log("hallooooo");
  console.log(lines);
  return inputArray;
}

console.log(lines);
console.log(symbolIndexes);

console.log(numberIndices);

const keys = Object.keys(numberIndices);
keys.forEach((key) => {
  console.log(numberIndices[key]);
});

// function getLines(file){
//     const path = `inputs/${file}`;
//     fs.readFile(path, 'utf8', (err, data)=>{
//         if (err) {
//             console.error(err);
//             return;
//         }

//         return data.split('\n');
//     })
// }
