/* for form submission */

const alertBox = document.getElementById('alert-box')
const form = document.getElementById('p-form')


const f_name = document.getElementById('id_name')
const email = document.getElementById('id_email')
const phone = document.getElementById('id_phone')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

const url = ''

const handleAlerts = (type, text) => {
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
    ${text}
    </div>`
}

form.addEventListener('submit',e => {
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('name', f_name.value)
    fd.append('email', email.value)
    fd.append('phone', phone.value)

    $.ajax({
        type: "POST",
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function (response) {
            console.log(response)
            const sText = `<div>
            <h4>OKAY</h4>
            <p>With your educational background, 
            you can apply for further studies.</p>
        </div>`
            handleAlerts('success', sText)
            setTimeout(() =>{
                alertBox.innerHTML = ''
                f_name.value = ''
                email.value = ''
                phone.value = ''

            }, 3000)
        },
        error: function (error) {
            console.log(error)
            handleAlerts('danger', 'oops..something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})



console.log(form)

