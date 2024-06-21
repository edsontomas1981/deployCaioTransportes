let placaRomaneio = document.getElementById('placaVeiculoRomaneio')
let modelo = document.getElementById('modeloVeiculoRomaneio')
placaRomaneio.addEventListener('blur',async()=>{

    if(placaRomaneio.value.trim() != '' ){
        let response  = await connEndpoint('/operacional/read_veiculo_placa/', {'placa':placaRomaneio.value});
        console.log(response)
        if (response.status ==200){
            modelo.value = response.veiculo.modelo
        }else{
            msgErro('Veículo não localizado')
            modelo.value = ""
        }
    }
})

document.getElementById('btnBuscaVeiculosRomaneio').addEventListener('click',()=>{
    msgAviso('Função em desenvolvimento')
    // openModal('mdlBuscaMotoristas')
})