let cpfMotorista = document.getElementById('cpfMotoristaRomaneio')
cpfMotorista.addEventListener('blur',async()=>{
    if(cpfMotorista.value.trim() == '' ){
        msgAviso("Por favor, selecione um motorista antes de prosseguir.")
        return
    }
    let response  = await connEndpoint('/operacional/read_motorista/', {'cpfMotorista':cpfMotoristaRomaneio.value});
    console.log(response)

})