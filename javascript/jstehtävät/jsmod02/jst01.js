const lista = []

for (let i = 0; i < 5; i++) {
    let item = prompt(`Anna ${i+1} luku`)
    lista.push(item)
    if (i === 4)
        for (let index = 4; index >= 0; index--){
            console.log(lista[index])
    }
}