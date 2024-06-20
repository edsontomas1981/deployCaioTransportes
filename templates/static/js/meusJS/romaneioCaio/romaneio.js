const romaneioExiste = ()=>{
    let romaneio = document.getElementById('numRomaneio')
    if (romaneio.textContent == ''){
        msgErro('Antes de continuar Selecione um Romaneio')
        return 
    }
    alert('continua')
    return romaneio.textContent
    
}