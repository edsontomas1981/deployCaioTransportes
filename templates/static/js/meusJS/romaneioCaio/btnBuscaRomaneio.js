let btnBusca = document.getElementById('btnBuscaRomaneio')

btnBusca.addEventListener('click',async()=>{
    let idBuscaRomaneio = document.getElementById('idRomaneio')
    let idRomaneio = document.getElementById('numRomaneio')
    let cpf = document.getElementById('cpfMotoristaRomaneio')
    let nomeMotorista = document.getElementById('nomeMotoristaRomaneio')
    let modelo = document.getElementById('modeloVeiculoRomaneio')
    let placa = document.getElementById('placaVeiculoRomaneio')

    if (idBuscaRomaneio.value != ""){
        let response  = await connEndpoint('/operacional/get_romaneio/', {idRomaneio:idBuscaRomaneio.value});
        if (response.status == 200){
            idRomaneio.textContent = response.manifesto.id
            cpf.value = response.manifesto.motorista_fk.parceiro_fk.cnpj_cpf
            nomeMotorista.value = response.manifesto.motorista_fk.parceiro_fk.raz_soc
            placa.value = response.manifesto.veiculo_fk.placa
            modelo.value = response.manifesto.veiculo_fk.modelo
            let dados = prepara_dados_tbody(response.manifesto.nota_fiscal_fk)  
        }else{
            msgErro('Manifesto não encontrado !')
            idRomaneio.textContent = ''
            cpf.value = ''
            nomeMotorista.value = ''
            placa.value = ''
            modelo.value = ''
        }   
    }
})