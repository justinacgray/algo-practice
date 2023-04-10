const alphabet = "abcdefghijklmnopqrstuvwxyz";
const vowels = "aeiou";


// const removeNonAlphanumeric = (string) => {
//   console.log("does this work")
//   return string.replace(/[^a-z0-9]/gi, '');
// }

const wordSum = (word) =>{
  // lowercase and make sure it's a letter
  let validWord = word.replace(/[^a-z]/gi, '').toLowerCase()

  let wordArr = []

  wordArr = validWord.split('')

  console.log("NEW WORD", validWord)
  console.log("ARRAYYY", wordArr)
}


wordSum('*-abc')

