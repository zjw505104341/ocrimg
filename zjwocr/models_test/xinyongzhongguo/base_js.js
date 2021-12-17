
//  npm install crypto-js
let CryptoJS = require("crypto-js");
function aesEncrypt(word,keyWord){
  // var keyWord = keyWord || "XwKsGlMcdPMEhR1B"
  var key = CryptoJS.enc.Utf8.parse(keyWord);
  var srcs = CryptoJS.enc.Utf8.parse(word);
  var encrypted = CryptoJS.AES.encrypt(srcs, key, {mode:CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7});
  return encrypted.toString();
}

// word     这个是坐标
// keyWord  接口返回的 secretKey

// console.log(aesEncrypt('[{"x":225,"y":107},{"x":164,"y":19},{"x":100,"y":100}]',
//     'zu72OIbf9AS2qthA'))
// 上面是第一次加密  // 点选的


console.log(aesEncrypt('{"x":12.5,"y":5}', 'zu72OIbf9AS2qthA'))
// 第一次加密 // 滑块,  x轴变化, y 轴不变



// console.log(aesEncrypt('3fa0dd7eb6d24341aa0917437f90adcf---[{"x":124,"y":79},{"x":186,"y":84},{"x":214,"y":99}]',
//     'Rebup0Rso9kfJjZD'))
// 上面是第二次加密