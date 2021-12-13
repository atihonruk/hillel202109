function autocomplete(elem) {
    elem.addEventListener("input", function(e) {
        val = this.value
        // check length
        fetch('/get-completions?' + new URLSearchParams({word: val}))
            .then(response => response.json())  // lambda response: response.json()
            .then(data => makeList(this, data))
    })

    function makeList(container, compl) {
        console.log(compl)
        div = document.createElement("div") // top level
        container.parentNode.appendChild(div)
        for (i=0; i < compl.length; i++) {
            title = compl[i].title
            e = document.createElement("div")
            div.appendChild(e)
            e.innerHTML += "<strong>" + title + "</strong>"
        }
    }
}
