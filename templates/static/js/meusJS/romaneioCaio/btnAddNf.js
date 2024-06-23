let btnAddNf = document.getElementById('btnAddNf')

btnAddNf.addEventListener('click',async ()=>{
    let idDocumento = document.getElementById('idDocumento')
    let tipoDocumento = document.getElementById('tipoDocumento')
    let idRomaneio = document.getElementById('numRomaneio')

    if(idRomaneio.value != ''){
        if (idRomaneio != '' && tipoDocumento.value!= '' && idDocumento.value != '' ){
            let response  = await connEndpoint('/operacional/add_nota_manifesto/', {'tipoDocumento':tipoDocumento.value,
                                                                                    'idDocumento':idDocumento.value,
                                                                                    'idRomaneio':idRomaneio.textContent});
            
            if(response.status === 'success'){
                prepara_dados_tbody(response.manifesto.nota_fiscal_fk) 
            }else{
                msgErro(response.message)
            }

        }else{
            msgAviso('Preencha todos os campos para prosseguir')
        }
    }else{
        msgAviso('É necessário salvar ou selecionar um romaneio.')
    }
})



