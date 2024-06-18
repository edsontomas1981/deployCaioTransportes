let cpfMotorista = document.getElementById('cpfMotoristaRomaneio')
let nomeMotorista = document.getElementById('nomeMotoristaRomaneio')
cpfMotorista.addEventListener('blur',async()=>{
    if(cpfMotorista.value.trim() == '' ){
        msgAviso("Por favor, selecione um motorista antes de prosseguir.")
        nomeMotorista.value = ""
        return
    }
    let response  = await connEndpoint('/operacional/read_motorista/', {'cpfMotorista':cpfMotoristaRomaneio.value});
    if (response.status ==200){
        nomeMotorista.value = response.motorista.parceiro_fk.raz_soc
    }else{
        msgErro('Motorista não localizado')
        nomeMotorista.value = ""
    }
})

document.getElementById('btnBuscaMotoristasRomaneio').addEventListener('click',()=>{
    msgAviso('Função em desenvolvimento')
    // openModal('mdlBuscaMotoristas')
})
