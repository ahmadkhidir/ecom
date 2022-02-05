
HSBsValidation.init('.login-validate', {
    onSubmit: data => {
      data.event.preventDefault()
      const backendVar = new FormData(document.querySelector("#backendVar"));
      const formdata = new FormData(document.querySelector(".login-validate"));
      const csrf = formdata.get('csrfmiddlewaretoken')
      const url = backendVar.get('loginUrl')

      axios({
        method: "POST",
        url: url,
        data: formdata,
        headers: {'X-CSRFToken': csrf},
        mode: 'same-origin',
      }).then((response) => {
          if (response.data.status === "ok") {
            location.reload(true)
          } else {
            const bf = document.querySelector(".backend-feedback")
            bf.innerText = "Invalid username or password."
            setTimeout(() => {
              bf.innerText = ""
            }, 3000)
          }
        })
      }
    });

function addToCart(e) {
    const backendVar = new FormData(document.querySelector("#backendVar"));
    const csrf = backendVar.get('csrfmiddlewaretoken')
    const url = backendVar.get('cartQueryUrl')
    const pId = e.getAttribute("pId")
    const formdata = new FormData()
    formdata.append('p', pId)
    formdata.append('q', "in_cart")

    axios({
        method: "POST",
        url: url,
        data: formdata,
        headers: {'X-CSRFToken': csrf},
        mode: 'same-origin',
    }).then((response) => {
        const data = response.data.status
        if (data) {
            e.classList.remove("btn-outline-primary")
            e.classList.add("btn-primary")
            e.innerText = "Added to cart!" 
        }
        else {
            e.classList.remove("btn-primary")
            e.classList.add("btn-outline-primary")
            e.innerText = "Add to cart"
        }
    })
}

function emptyCart(e) {
    const t = document.querySelector("#offcanvasNavbarEmptyShoppingCart")
    const bd = document.querySelector(".offcanvas-backdrop")
    const backendVar = new FormData(document.querySelector("#backendVar"));
    const csrf = backendVar.get('csrfmiddlewaretoken')
    const url = backendVar.get('cartQueryUrl')
    const cartUrl = backendVar.get('cartUrl')
    t.classList.remove("show")
    bd.classList.remove("show")
    const formdata = new FormData()
    formdata.append('q', "empty_cart")

    axios({
        method: "POST",
        url: url,
        data: formdata,
        headers: {'X-CSRFToken': csrf},
        mode: 'same-origin',
    }).then((response) => {
        console.log(response.data.status)
        if (!response.data.status) {
            t.classList.remove("show")
            bd.classList.remove("show")
            location.assign(cartUrl)
        } else {
            t.classList.add("show")
            bd.classList.add("show")
        }
    })
}