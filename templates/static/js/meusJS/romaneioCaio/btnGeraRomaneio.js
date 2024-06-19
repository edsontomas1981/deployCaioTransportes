let btnGeraRomaneio = document.getElementById('btnGeraRomaneio')

btnGeraRomaneio.addEventListener('click',async ()=>{
    let cpf = document.getElementById('cpfMotoristaRomaneio')
    let placa = document.getElementById('placaVeiculoRomaneio')
    let response  = await connEndpoint('/operacional/create_romaneio/', {'placa':placa.value,'cpf':cpf.value});
    if (response.status){
        document.getElementById('numRomaneio').textContent = response.manifesto.id
    }
})