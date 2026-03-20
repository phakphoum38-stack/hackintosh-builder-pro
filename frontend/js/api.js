async function scan(){

let r = await fetch("/hardware/scan")

let data = await r.json()

document.getElementById("output").innerText =
JSON.stringify(data,null,2)

}

async function build(){

let r = await fetch("/efi/build")

let data = await r.json()

alert(data.status)

}
