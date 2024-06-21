let btnAddNf = document.getElementById('btnAddNf')

btnAddNf.addEventListener('click',async ()=>{
    let idDocumento = document.getElementById('idDocumento')
    let tipoDocumento = document.getElementById('tipoDocumento')
    let idRomaneio = document.getElementById('numRomaneio')

    if (idRomaneio != '' && tipoDocumento.value!= '' && idDocumento.value != '' ){
        let response  = await connEndpoint('/operacional/add_nota_manifesto/', {'tipoDocumento':tipoDocumento.value,
                                                                                'idDocumento':idDocumento.value,
                                                                                'idRomaneio':idRomaneio.textContent});
        let dados = prepara_dados_tbody(response.manifesto.nota_fiscal_fk)    
        popula_tbody_paginacao('navegacaoNfsRomaneio','romaneioNotas',dados,false,1,50,false,false)
    }else{
        msgAviso('Preencha todos os campos para prosseguir')
    }
})



