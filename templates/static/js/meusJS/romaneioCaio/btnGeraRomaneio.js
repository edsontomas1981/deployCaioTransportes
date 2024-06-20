let btnGeraRomaneio = document.getElementById('btnGeraRomaneio')

btnGeraRomaneio.addEventListener('click',async ()=>{
    let nomeMotorista = document.getElementById('nomeMotoristaRomaneio')
    let modelo = document.getElementById('modeloVeiculoRomaneio')

    let cpf = document.getElementById('cpfMotoristaRomaneio')
    let placa = document.getElementById('placaVeiculoRomaneio')

    if (nomeMotorista.value !='' && modelo.value !=''){
        let response  = await connEndpoint('/operacional/create_romaneio/', {'placa':placa.value,'cpf':cpf.value});
        if (response.status){
            document.getElementById('numRomaneio').textContent = response.manifesto.id
            cpf.value = response.manifesto.id

        }
    }else {
        msgAlerta('Preencha os campos obrigatorios')
    }
}) 