let members = prompt("How many participants? Give a number")
const namelist = []
members = parseInt(members)

for (members === 0; members--;){
    console.log(members)
    name = prompt("Name your participants in order, one per prompt.")
    namelist.push(name)
    namelist.sort()
    //document.getElementById("namelist").appendChild(name)
}


    let list = document.querySelector("#participants");

    for (let i = 0; i < namelist.length; ++i) {
            let li = document.createElement('li');
            //li.innerText = name[i];
            list.appendChild(li);
            li.innerText = namelist[i];
            console.log(namelist[i])
    }