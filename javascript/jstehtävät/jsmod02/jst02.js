let members = prompt("How many participants? Give a number")
const namelist = []
members = parseInt(members)

for (members === 0; members--;){
    console.log(members)
    name = prompt("Name your participants in order, one per prompt.")
    namelist.push(name)
    //document.getElementById("namelist").appendChild(name)
}


    let list = document.getElementById("participants");
    for (i = 0; i < namelist.length; ++i) {
        let li = document.createElement('li');
        li.innerText = name[i];
        list.appendChild(li);
    }