// Search Name
function submitSearch() {
    let name = document.getElementById("username");
    let username = name.value

    fetch(`/api/member?username=${username}`, {
        method: "GET",
        credentials: "include",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then(function (response) {
            response.json().then(function (data) {
                let result = data.data
                if (result !== null) {
                    let searchResult = document.querySelector(".searchResult")
                    searchResult.className = "searchResult"
                    let nameDiv = document.createElement("div")
                    nameDiv.className = "nameDiv"
                    let name = document.createTextNode(`${result.username}  ( ${result.userId} )`)

                    //clear out searchresult first
                    let clear = document.querySelector(".searchResult")
                    while (clear.firstChild) {
                        clear.removeChild(clear.firstChild)
                    }

                    //then append
                    searchResult.appendChild(nameDiv)
                    nameDiv.appendChild(name)
                } else {
                    let searchResult = document.querySelector(".searchResult")
                    searchResult.className = "searchResult"
                    let nameDiv = document.createElement("div")
                    nameDiv.className = "nameDiv"
                    let error = document.createTextNode("????????????????")

                    //clear out searchresult first
                    let clear = document.querySelector(".searchResult")
                    while (clear.firstChild) {
                        clear.removeChild(clear.firstChild)
                    }

                    //then append
                    searchResult.appendChild(nameDiv)
                    nameDiv.appendChild(error)
                }
            })
        })
}


//Change Name
function submitChange() {
    let change = document.getElementById("changeName");
    let changeName = change.value

    let newName = {
        "name": changeName
    }
    // console.log(newName)

    fetch(`${window.origin}/api/member`, {
        method: "PATCH",
        credentials: "include",
        body: JSON.stringify(newName),
        cache: "no-cache",
        headers: new Headers({
            "Content-Type": "application/JSON"
        })
    })
        .then(function (response) {
            response.json().then(function (response) {
                // console.log(response)
                if (response.ok) {
                    let changeResult = document.querySelector(".changeResult")
                    changeResult.className = "changeResult"
                    let newNameDiv = document.createElement("div")
                    newNameDiv.className = "newNameDiv"
                    let changed = document.createTextNode(`更新暱稱為 ${newName.name}`)

                    //clear out changeResult first
                    let clear = document.querySelector(".changeResult")
                    while (clear.firstChild) {
                        clear.removeChild(clear.firstChild)
                    }

                    //then append
                    changeResult.appendChild(newNameDiv)
                    newNameDiv.appendChild(changed)
                }
                else {
                    let changeResult = document.querySelector(".changeResult")
                    changeResult.className = "changeResult"
                    let nameDiv = document.createElement("div")
                    nameDiv.className = "nameDiv"
                    let error = document.createTextNode("????????????????")

                    //clear out searchresult first
                    let clear = document.querySelector(".changeResult")
                    while (clear.firstChild) {
                        clear.removeChild(clear.firstChild)
                    }

                    //then append
                    changeResult.appendChild(nameDiv)
                    nameDiv.appendChild(error)
                }
            })

        })
}