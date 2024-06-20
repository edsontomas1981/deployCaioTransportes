let btnBusca = document.getElementById('btnBuscaRomaneio')

btnBusca.addEventListener('click',async()=>{
    let idBuscaRomaneio = document.getElementById('idRomaneio')
    let idRomaneio = document.getElementById('numRomaneio')
    if (idBuscaRomaneio.value != ""){
        let response  = await connEndpoint('/operacional/get_romaneio/', {idRomaneio:idBuscaRomaneio.value});
        console.log(response)
        // idRomaneio.textContent = idBuscaRomaneio.value

    }
})