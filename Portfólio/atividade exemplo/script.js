const regex = /\d{11}/
const criar = document.getElementById('bt-icon')
const enviar = document.getElementById('bt-icon2')
const copia_div = document.getElementById('copiar')
const number = document.getElementById('numero')
const span_click = document.getElementById('click')

function check_number() {
    let numeros = ''
    for (let n of number.value) {
        switch (n) {
            case '(':
                numeros.replace('')
            case ')':
                numeros.replace('')
            case '-':
                numeros.replace('')
            case ' ':
                numeros.replace('')
                break;
            default:
                numeros += n;
        }
    }
    if (regex.test(numeros)) {
        number.classList.add('correct')
        number.classList.remove('error')
        return true
    } else {
        number.classList.add('error')
        number.classList.remove('correct')
        return false
    }
}


function create_link() {
    let numeros = ''
    for (let n of number.value) {
        switch (n) {
            case '(':
                numeros.replace('')
            case ')':
                numeros.replace('')
            case '-':
                numeros.replace('')
            case ' ':
                numeros.replace('')
                break;
            default:
                numeros += n;
              
        }
    }

    
    if (check_number()) {
        const link_copiar = `https://wa.me/${numeros}`
        copia_div.style.display = 'flex'
        span_click.style.display = 'flex'
        copia_div.innerText = link_copiar
        let format = `(${numeros.substring(0, 2)}) ${numeros.substring(2, 7)}-${numeros.substring(7, 12)}`
        number.value = format
    } else {
        copia_div.style.display = 'none'
        span_click.style.display = 'none'
    }
}

async function copy(){
    try{
        await navigator.clipboard.writeText(copia_div.innerText)
        span_click.innerText = 'Texto copiado para área de transferência'    
    } catch(error){
        alert('erro', error)
    }
}

number.addEventListener('input', check_number)
number.addEventListener('click', () => {
    if (span_click.style.display == 'flex' || copia_div.style.display == 'flex'){
        span_click.style.display = 'none'
        span_click.innerText = 'Clique no link para copiar'
        copia_div.style.display = 'none'
    }
})
criar.addEventListener('click', create_link)
enviar.addEventListener('click', create_link)
copia_div.addEventListener('click', copy)
enviar.addEventListener('click', () => {
    console.log(copia_div.innerText)
    if (check_number()){
        window.open(copia_div.innerText);
    } else {
        alert('Digite um número válido');
    }
});
