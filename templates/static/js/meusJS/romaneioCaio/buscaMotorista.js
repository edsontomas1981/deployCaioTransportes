let cpfMotorista = document.getElementById('cpfMotoristaRomaneio')
let nomeMotorista = document.getElementById('nomeMotoristaRomaneio')
cpfMotorista.addEventListener('blur',async()=>{
    if(validateDocumentNumber(cpfMotorista.value)){
        let response  = await connEndpoint('/operacional/read_motorista/', {'cpfMotorista':cpfMotoristaRomaneio.value});
        if (response.status ==200){
            nomeMotorista.value = response.motorista.parceiro_fk.raz_soc
        }else{
            msgErro('Motorista não localizado')
            nomeMotorista.value = ""
        }
    }else{
        if(cpfMotorista.value != ''){
            msgErro('CPF Motorista Inválido')
        }
        
    }
    
})

document.getElementById('btnBuscaMotoristasRomaneio').addEventListener('click',()=>{
    msgAviso('Função em desenvolvimento')
    // openModal('mdlBuscaMotoristas')
})
