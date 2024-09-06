const foto = document.getElementById("foto")
const imagem = document.getElementById("imagem")


foto.addEventListener("mouseover", () => {
    imagem.style.width = "20vw"
    imagem.style.boxShadow = "5px 5px 15px white"
    
    
    /*img {
        border-radius: 50%;
        box-shadow: 5px 5px 15px var(--preto);
        cursor: pointer;
        }*/
})
    
foto.addEventListener("mouseout", () => {
    imagem.style.width = "auto"
    imagem.style.boxShadow = "5px 5px 15px var(--preto)"


    /*img {
        border-radius: 50%;
        box-shadow: 5px 5px 15px var(--preto);
        cursor: pointer;
    }*/
    
})
