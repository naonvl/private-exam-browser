const userAgent = document.getElementById('userAgent');
const hiddenContent = document.getElementById('hiddenContent');
console.log()
if(navigator.userAgent != 'NATEPBROWSER/1.0'){
    userAgent.innerText = 'KAMU TIDAK MENGGUNAKAN PRIVATE BROWSER!!!';
} else {
    userAgent.innerText = 'KAMU BOLEH LANJUT';
    hiddenContent.style.display= 'block';
}