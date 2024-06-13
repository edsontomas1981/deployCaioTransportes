const getStatusLabel = (status) => {
    switch (status) {
        case 1:
            return '<label class="badge badge-danger">Pendente</label>';
        case 2:
            return '<label class="badge badge-warning">Em Progresso</label>';
        case 3:
            return '<label class="badge badge-success">Concluído</label>';
        case 4:
            return '<label class="badge badge-secondary">Cancelado</label>';
        case 5:
            return '<label class="badge badge-info">Em Espera</label>';
        default:
            return '<label class="badge badge-primary">Desconhecido</label>';
    }
};

const prepara_dados_nfs = (result)=>{
    let dados = []
    result.forEach(element => {
        const statusHTML = getStatusLabel(element.status);
        dados.push({
                    id:element.id,
                    nf:element.num_nf,
                    remetente:truncateString(element.remetente.raz_soc,15),
                    destinatario:truncateString(element.destinatario.raz_soc,15),
                    origem:truncateString(element.remetente.endereco_fk.bairro,7),
                    destino:truncateString(element.destinatario.endereco_fk.bairro,7),
                    volume:element.volume,
                    peso:element.peso,
                    valorNfe:element.valor_nf,  
                    status:statusHTML
                })
        });
    return dados
}

document.getElementById('modalNumNf').addEventListener('click',async ()=>{
    let response = await connEndpoint('/operacional/updateNfStatusNf/', {'idNf':document.getElementById('txtIdNumNf').value,
                                                                        'numNf':document.getElementById('cmbStatus').value,
    });

    console.log(response)

})

const umBotao = (element)=>{
    openModal('modalAlteraNotas')
    document.getElementById('txtIdNumNf').value=element
}
document.addEventListener('DOMContentLoaded',async ()=>{
    let botoes = {
        mostrar: {
            classe: "btn-success text-white",
            texto: '<i class="fa fa-window-restore" aria-hidden="true"></i>',
            callback: umBotao
        },
        excluir: {
            classe: "btn-danger text-white",
            texto: '<i class="fa fa-print" aria-hidden="true"></i>',
          //   callback: enviarMensagemWebSocket
        }
    };

    let response = await connEndpoint('/operacional/readNfs/', {});
    let dadosTbody = response.nfs
    let dadosParametrizados = prepara_dados_nfs(dadosTbody)
    console.log(dadosParametrizados)
    popula_tbody_paginacao('paginacaoTodasNfs','relatorioNfs',dadosParametrizados,botoes,1,20,false,false)
})

